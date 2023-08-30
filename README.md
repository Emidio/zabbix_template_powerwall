# Zabbix Template for Tesla Powerwall

This is a very simple way to monitor your SolaEdge inverter directly without relying on the SolarEdge website. Information are not complete, and this work is really simple and rough - I just needed it to debug my system, quick and dirty.


Install on zabbix server pypowerwall (python needed, install it if missing):

https://github.com/jasonacox/pypowerwall

pip3 install pypowerwall

You need to copy the two scripts in your externalscripts zabbix folder, adjust timezone in powerwall.py and path in powerwall.sh.

Import Zabbix template. Create a new host (doesn't matter interface, I set SNMP), assign the template, set the correct macros:

{$PWL_ADDRESS}    Powerwall local IP adddress.
{$PWL_EMAIL}      Your Tesla registration email.
{$PWL_PASSWORD}   Your Powerwall password (not the web one, the one to access Powerwall directly using it's LAN/WiFi IP address - should be last 5 characters of serial or password printed on the sticker). Refer ro this document: https://www.tesla.com/support/energy/powerwall/own/connecting-network

You can try using a browser and loggin in to the Powerwall IP address.

Tested using Zabbix 6.2, Tesla Powerwall 2 and SolarEdge HD-Wawe SE6000H. Dashboards in Grafana using Zabbix plugin by Alexander Zobnin.
