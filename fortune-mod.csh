#!/bin/csh
# skip fortunes on cron mails.
tty -s
if ( $? == 0 ) then
	echo
	fortune -s
	echo
endif
