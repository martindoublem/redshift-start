#!/bin/sh

validateConnection () {
    a=`wget -q -O - checkip.dyndns.org | sed -e 's/[^[:digit:]\|.]//g'`
    echo $a
}

connection=$(validateConnection)

while [ ! $connection ]
do
  sleep 5
  connection=$(validateConnection)
done
python write_conf.py
redshiftgui --min
