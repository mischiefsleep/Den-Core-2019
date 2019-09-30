#!/bin/bash

# Guilhem Mizrahi 09/2019

bin="/bin";
log_file="/var/log/auth.log";
alert_log="/var/log/ssh-log/ssh.scan";
email="EMAIL@ADDRESS.COM";

echo "Log since $(date +"%Y-%m-%d    %T" -d "1 hour ago")">$alert_log;

hour=$($bin/date +"%s" -d "1 hour ago");

mapfile -t result <<< $($bin/awk -v awkvar=$HOSTNAME 'BEGIN { FS=awkvar; OFS="|" } /ailed|ailure/ {print $1,$2}' $log_file);

count=0;

for i in "${result[@]}"
do
    IFS="|" read entry_time message <<< $i;
    et=$($bin/date -d "$entry_time" +"%s");
    if [ $et -ge $hour ]
    then
        ((count++));
        echo "$entry_time | $message">>$alert_log;
    fi
done

echo "$count failures detected";

if [ $count -gt 5 ]
then
    echo "Send alert sms to number";
    mail -s "SSH alert" $email <<< "There were $count failed attempts to connect to $HOSTNAME since $($bin/date +"%T")";
    cp $alert_log $alert_log$hour;
else
    echo "";
fi
