#!/bin/sh
# skip fortunes on cron mails.
tty -s || exit 0

echo
fortune -s
echo
