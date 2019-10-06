#!/bin/bash

# Guilhem Mizrahi 09/2019

function arg_parser(){
	echo "number of arguments [$#]";
	if [ "$#" -eq 5 ]
	then
		log_file=$1; 	# Set the path to the log file auth.log
		alert_log=$2;	# Set the path to where the new logs will be saved
		email=$3;	# Save the email to whom send the emails
		threshold=$4;	# Set the threshold over which an alert is sent
		period=$5;	# Set the period that will be parsed by the script
		echo "Variables set";
		echo -e "\tlog_file=[$log_file]";
		echo -e "\talert_log=[$alert_log]";
		echo -e "\temail=[$email]";
		echo -e "\tthreshold=[$threshold]";
		echo -e "\tperiod=[$period]";
		return 0;
	else
		echo "Usage [$0] wrong number of arguments.";
		echo "Please specify :";
		echo -e "\tthe path to the log_file";
		echo -e "\tthe path to the alert file";
		echo -e "\tthe email address to whom send the alerts";
		echo -e "\tthe threshold (number of failures over which to send the alerts)";
		echo -e "\tthe period in hours (time between two executions of the script, also how far back in time the script will look into the log file.";
		exit 1; 	# Don't continue execution if the parsing of arguments didn't work
	fi
}

function ssh_filter_function(){
		# This function will compare two values and return 0 if the first is greater than the second.
		# Typically in the case of scanning the ssh logs it is used to compare the timestamp of the line to the timestamp of one hour ago
		# For other logs, this function could be changed to adapt to the filtering criteria.
	entry_time_seconds=$1;
	compare_to=$2;
	echo "Compare [$entry_time_seconds] to [$compare_to]";
	if [ $entry_time_seconds -ge $compare_to ]
	then
		echo "Hit";
		return 0;
	else
		return 1;
	fi
}

function log_parser(){
	log_file=$1;
	alert_log=$2;
	period=$3;
	if [ -f $log_file ]	# Check if the log file exists
	then
		echo "log_parser running on file [$log_file]";
		hour=$(/bin/date +"%s" -d "$period hour ago"); 	# Define the time frame to parse the log file in seconds
		echo "Log since $(/bin/date +"%Y-%m-%d    %T" -d "$period hour ago")" | tee $alert_log;	
			# Write a header to the alert file and to the screen
		mapfile -t result <<< $(/bin/awk -v awkvar=$HOSTNAME 'BEGIN { FS=awkvar; OFS="|" } /ailed|ailure/ {print $1,$2}' $log_file);
			# Parse what is inside the log file, select only the lines that match "ailed" or "ailure";
			# split the selected lines over the hostname (this reflects how the auth.log file is written)
			# and saves the lines with the format first_part|second_part.
			# The first part holds the time stamp and the second part holds the error message.
		count=0;			# Initially the number of errors logged into the file is 0
		for i in "${result[@]}"		# For every line in the array of failures the script will log it into the alert file and count it
		do
    			IFS="|" read entry_time message <<< $i;
				# This parses the line and splits over the "|" character.
				# The first part it the time stamp, the second part is the error message
    			entry_time_seconds=$(/bin/date -d "$entry_time" +"%s");
				# Convert the time stamp in seconds to help with the comparison
			ssh_filter_function $entry_time_seconds $hour;
    			if [ $? -eq 0 ]
				# If the result of the filter function is 0 (meaning it filtered True)
    			then
				echo -e "$entry_time\t|\t$message" >> $alert_log;
					# Log the "timestamp	|	error message" to the alert log file
        			((count++));
					# Increment the counter
    			fi
		done
		echo "[$count] Failures detected";	# Output the number of failures detected
		#return $((count < 255 ? count : 255)); 
	fi
}

# TO DO : It would be useful to be able to make the filter function (inside the awk command line 45) into a standalone function. Right now it is a regex /ailed|ailure/ that can match pretty well the SSH log file but to make this program usable for a different log file it would need some engineering.

function trigger_alert(){
	alert_log=$1;
	threshold=$2;
	email=$3;	
	count=$(/usr/bin/wc -l < $alert_log);
	echo "[$count] lines in the log file";
	if [ $(/usr/bin/wc -l < $alert_log) -gt "$threshold + 1" ]
	then
    		/bin/mail -s "SSH alert" $email <<< "There were [$count] failed attempts to connect to [$HOSTNAME] detected on [$(/bin/date +"%T")]";
		if [ "$?" -eq 0 ] # Check if the mail command worked
		then
    			echo "Send alert sms to [$email]" | tee -a $alert_log; # Write to the file that an alert has been sent
		else
    			echo "Couldn't send alert sms to [$email]" | tee -a $alert_log; # Write to the file that an alert has been sent
			echo "Check your configuration file /etc/ssmtp/ssmtp.conf or the email address [$email].";
		fi		
		hour=$(/bin/date +"%s");
    		/bin/cp $alert_log $alert_log$hour; # In any case, copy the log file
		return 1;	
	else
		return 0;
	fi
}

arg_parser "$@";
log_parser "$1" "$2" "$5";
trigger_alert "$2" "$4" "$3";
