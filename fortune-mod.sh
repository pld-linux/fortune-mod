#!/bin/sh
# skip fortunes on cron mails.
tty -s
if [ $? -eq 0 ]; then
	echo
	fortune -s
	echo
fi
