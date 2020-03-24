# Redshift start scripts

This script is done in two parts in order to start redshift without using geoclue
which I find to be buggy and resource intensive.

it checks if you have an internet connection then proceeds to run the python
script to get your location (latitude, longitude) if you have one, otherwise it
keeps waiting till you have one.

Once this is done, the script starts redshift with the right coordinates
(lat, lon).

This script can be run at boot in your config file for i3

## Task list
- [X] bash script
- [X] python script
- [X] test on my system
