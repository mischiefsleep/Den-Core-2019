#!/bin/bash
#[ -e /etc/passwd ] && { echo "exists"; exit 0; }
for fn in $@; do
	echo ${fn}
done
