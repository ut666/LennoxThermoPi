LennoxThermoPi
==============

Log data from your Lennox iComfort thermostat.

Since Lennox don't provide any API to communicate with the iComfort thermostat, I create the following.

get_page.py

This will grab the iComfort web page and log to a text file the relavant information. 
Currently it will log:

- current temperature
- minimum set (A/C)
- maximum set (Heating)
- humidity
- satus (HEATING, COOLING, IDLE)

Note you will need to create your own cookie.txt file using something like:
https://addons.mozilla.org/en-us/firefox/addon/cookie-exporter/

index.html

This is a simple html page that uses the Google Graph API to allow you to do your plots.
An example out from this page is shown in the Example.png