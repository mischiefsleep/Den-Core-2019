To configure the program, run the following command :\
sudo ./make-config.sh\
And follow the instructions.

This will perform the following operations :
1. Setup the mail account from which to send the alerts
2. Send a test email to this address
3. Edit the ssh_scan.sh file with the correct email address of the recipient
4. Install the dependencies (mawk and mailutils) if necessary.
5. Create the directories in which to keep the alert logs and move the script in this directory
6. Update the permissions to secure the script
7. Add an entry in the crontab so the scripts gets executed every hour

In the end the structure looks like the following\
/var/log/ssh-log/\
&nbsp;&nbsp;&nbsp;&nbsp;├── ssh.scan\
&nbsp;&nbsp;&nbsp;&nbsp;├── ssh.scan1569596461\
&nbsp;&nbsp;&nbsp;&nbsp;├── ssh.scan1569600061\
&nbsp;&nbsp;&nbsp;&nbsp;├── ssh.scan1569603661\
&nbsp;&nbsp;&nbsp;&nbsp;└── ssh_scan.sh\

