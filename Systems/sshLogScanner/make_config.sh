#!/bin/bash

# Guilhem Mizrahi 10/2019

source $(pwd)/config_scripts.sh

check_root;
installs;
configure_server /etc/ssmtp/ssmtp.conf;
#move_scripts ssh_scan.sh /sbin/ssh_scan.sh;
edit_crontab "01" "*" "*" "*" "*" "/sbin/ssh_scan.sh";
