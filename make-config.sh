#!/bin/bash

dir=$( dirname "${BASH_SOURCE[0]}" );

echo "Starting installation.";
echo "";

echo "Setting up the mail account from which to send emails";
echo "If you have a gmail address, you may have to enable a security setting on your account to allow third party apps to access it.";
echo "You can also create an application specific password if your provider allows it";
read -p "Provide your email address : " email;
echo "";
echo "Provide the password of your email account (the password is only accessible by root)"; 
read -s password;
echo "";

read -p "Provide a SMTP server name and port (for example smtp.gmail.com:587 for gmail addresses) : " server;
echo "";

echo "Writing the settings to the configuration file.";
echo "" >> /etc/ssmtp/ssmtp.conf;
echo "FromLineOverride=YES" >> /etc/ssmtp/ssmtp.conf;
echo "" >> /etc/ssmtp/ssmtp.conf;
echo "AuthUser=$email" >> /etc/ssmtp/ssmtp.conf;
echo "" >> /etc/ssmtp/ssmtp.conf;
echo "AuthPass=$password" >> /etc/ssmtp/ssmtp.conf;
echo "" >> /etc/ssmtp/ssmtp.conf;
echo "mailhub=$server" >> /etc/ssmtp/ssmtp.conf;
echo "" >> /etc/ssmtp/ssmtp.conf;
echo "UseSTARTTLS=YES" >> /etc/ssmtp/ssmtp.conf;

read -p "Provide the email addres of who you want the emails to be sent to : " $recipient;

sed -i "s/EMAIL@ADDRESS.COM/$recipient/" $dir/ssh_scan.sh;
echo "";

echo "A test email will be sent to $email.";
echo "";
echo "Your server for SSH Sentry has been correctly configured." | /bin/mail -s "SSH sentry configuration test" $email; 

if [ -f `which awk` ]
then
    echo "Copying awk.";
    cp `which awk` /bin;
else
    echo "Installing awk.";
    apt install mawk;
    cp `which awk` /bin;
fi

echo "";

if [ -f `which mail` ]
then
    echo "Copying mail.";
    cp `which mail` /bin;
else
    echo "Installing mailutils.";
    apt install mailutils;
    cp `which mail` /bin;
fi

echo "";

if [ -f `which ssmtp` ]
then
    echo "Copying ssmtp.";
    cp `which ssmtp` /bin;
else
    echo "Installing ssmtp.";
    apt install ssmtp;
    cp `which ssmtp` /bin;
fi

echo "";

if [ ! -d /var/log/ssh-log ];
then
    echo "Directory /var/log/ssh-log doesn't exist. Creating it.";
    mkdir /var/log/ssh-log;
    chmod 700 /var/log/ssh-log;
    echo "";
    echo "Creating file /var/log/ssh-log/ssh.scan";
    touch /var/log/ssh-log/ssh.scan;
    chmod 700 /var/log/ssh-log/ssh.scan;
else
    echo "Directory /var/log/ssh-log already exists. Updating permissions.";
    chmod 700 /var/log/ssh-log;
    touch /var/log/ssh-log/ssh.scan;
    chmod 700 /var/log/ssh-log/ssh.scan;
fi

echo "";

echo "Copying the script to /var/log/ssh-log.";
cp "$dir/ssh_scan.sh" /var/log/ssh-log;
chmod 700 /var/log/ssh-log/ssh_scan.sh;
echo "";

echo "Putting the script in the crontab and set it to execute every hour.";
echo "01 *    * * *   root    /bin/bash /var/log/ssh-log/ssh_scan.sh" >> /etc/crontab;
echo "";
echo "Installation complete";
