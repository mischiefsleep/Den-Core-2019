To configure the program, run the following command :
sudo ./make-config.sh
And follow the instructions.

This will edit the ssh_scan.sh file with the correct email address,

Install the dependencies (mawk and mailutils) if necessary.

Create the log directory and move the files in the correct places.
Change permissions to files so the program is secure.

Add the script to the crontab so it gets executed every hour at xx:01.
