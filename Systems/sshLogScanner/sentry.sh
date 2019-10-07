#!/bin/bash

# Guilhem Mizrahi 10/2019

source $(pwd)/ssh_scan.sh;
source $(pwd)/ssh_scanner.conf;

arg_parser $log_file $alert_log $email_alert $threshold $period;
log_parser $log_file $alert_log $period;
trigger_alert $alert_log $threshold $email_alert;
