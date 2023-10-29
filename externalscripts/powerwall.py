import pypowerwall
import sys
import hashlib
import os

# Optional: Turn on Debug Mode
# pypowerwall.set_debug(True)


# Credentials for your Powerwall - Customer Login Data
password=sys.argv[3]
email=sys.argv[2]
host = sys.argv[1]       # Address of your Powerwall Gateway
timezone = sys.argv[4]   # Your local timezone

# Connect to Powerwall
pw = pypowerwall.Powerwall(host,password,email,timezone)



# JSON Payload
print("{")
print("'Firmware': '%s'," % pw.version())
print("'Uptime': '%s'," % pw.uptime())
print("'BatteryLevel': %s," % pw.level())
print("'PowerMetrics': %r," % pw.power())

print("'Grid': %r\n" % pw.grid(verbose=True))
print(",")
print("'Solar': %r\n" % pw.solar(verbose=True))
print(",")
print("'Battery': %r\n" % pw.battery(verbose=True))
print(",")
print("'Home': %r\n" % pw.home(verbose=True))

# Display Device Vitals
print(",")
print("'Vitals': %r\n" % pw.vitals())



# Display Alerts list with status: 0 inactive, 1 active
print(",")
print("'Alerts':")

	
# List of diabled alerts, to be considered as normal operation
alertsdisabledlist = ["POD_w110_SW_EOC", "SYNC_a001_SW_App_Boot", "PINV_a067_overvoltageNeutralChassis", "SYNC_a001_SW_App_Boot", "SYNC_a046_DoCloseArguments", "SYNC_a038_DoOpenArguments"]
	
alertslist = pw.alerts()

cleanlist = []
for alert in alertslist:
	# getting all alerts containing underscore and ignoring others (usually norma operations)
  if '_' in alert:
    if not any(x == alert for x in alertsdisabledlist):
      cleanlist.append(alert)


fileid = host + password

# encoding alertslist using encode()
# then sending to md5()
filenameenc = hashlib.md5(fileid.encode())

chachefilepath = "/tmp/zbx_pw_" + filenameenc.hexdigest() + ".tmp"

if not os.path.isfile(chachefilepath):
  cachefile = open(chachefilepath, "w")
  cachefile.close()

cachefile = open(chachefilepath, "r") 

newalert = False
filealerts = cachefile.read()
cachefile.close()


filealertslist = filealerts.split(",")

if (len(filealertslist) > 1 and filealertslist[0] == ""):
  filealertslist.pop(0)

for cleanalert in cleanlist:
  if not any(x == cleanalert for x in filealertslist):
  	newalert = True
  	filealertslist.append(cleanalert)


if newalert:
  cachefile = open(chachefilepath, "w")
  cachefile.write(','.join(filealertslist))
  cachefile.close()

if (len(filealertslist) == 1 and filealertslist[0] == ""):
  filealertslist.pop(0)

print("[");
firstitem = True
for curralert in filealertslist:
  if any(x == curralert for x in cleanlist):
    alarmset = 1
  else:
    alarmset = 0
  if firstitem:
    print("{ '" + curralert + "': " + str(alarmset) + " }")
  else:
    print(", { '" + curralert + "': " + str(alarmset) + " }")
  firstitem = False
print("]");



# Display String Alerts for LLD discovery rule
print(",")
print("'AlertsDiscovery':")
print("[");
firstitem = True
for curralert in filealertslist:
  if firstitem:
    print("{ 'code': '" + curralert + "', 'status': " + str(alarmset) + " }")
  else:
    print(",{ 'code': '" + curralert + "', 'status': " + str(alarmset) + " }")
  firstitem = False
print("]");






# End JSON
print("}")
