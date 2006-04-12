#!/bin/csh

tty -s
if ($status == 0) then
	echo
	fortune -s
	echo
endif
