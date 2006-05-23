#!/bin/sh
# skip fortunes on cron mails.
if tty -s; then
	echo
	fortune -s
	echo
fi
