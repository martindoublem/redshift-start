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
loc=$(python location.py)
redshift -l $loc
