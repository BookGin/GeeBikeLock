#!/usr/bin/env bash
stty -F /dev/ttyACM0 cs8 9600 igncr ignbrk -brkint -imaxbel -opost -onlcr -isig -icanon -iexten -echo -echoe -echok -echoctl -echoke noflsh -ixon -crtscts
mkfifo backpipe
cat /dev/ttyACM0 0<backpipe | nc bike.csie.org 5566 | tee backpipe
