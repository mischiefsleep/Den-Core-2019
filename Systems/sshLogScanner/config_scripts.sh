#!/bin/bash

# Guilhem Mizrahi 10/2019

function check_root(){
	if [[ $EUID -ne 0 ]]
	then
		echo "Script must be run as root";
		exit 1;
	else
		return 0;
	fi
}

function installs(){
	check_root;
	apt install ssmtp;
	apt install mailutils;
}

function configure_server(){
	check_root;
	conf=$1;
	echo "Configuring the mail server";
	read -p "What email should be the sender of alerts ? " email;
	echo "Provide a password for this email account (create an app specific and secure password in the security tab of your account)";
	read -s password;
	read -p "Provide a mailhub for your account (by default gmail uses smtp.gmail.com:587) " mailhub;
	echo "FromLineOverride=YES" > $conf;
	echo "AuthUser=$email" >> $conf;
	echo "AuthPass=$password" >> $conf;
	echo "mailhub=$mailhub" >> $conf;
	echo "UseSTARTTLS=YES" >> $conf;
}

function move_scripts(){
	check_root;
	echo "Copying the scripts to the correct destination";
	src=$1;
	dst=$2;
	cp $src $dst;
	chmod 700 $dst;
}

function edit_crontab(){
	check_root;
	min=$1;
	hour=$2;
	day=$3;
	week=$4;
	month=$5;
	script=$6;
	echo "Editing the crontab";
	echo "$min $hour $day $week $month root /bin/bash $script" >> /etc/crontab;
}
