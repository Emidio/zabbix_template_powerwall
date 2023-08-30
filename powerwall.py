import pypowerwall
import sys

# Optional: Turn on Debug Mode
# pypowerwall.set_debug(True)

# Credentials for your Powerwall - Customer Login Data
password=sys.argv[3]
email=sys.argv[2]
host = sys.argv[1]               # Address of your Powerwall Gateway
timezone = "Europe/Rome"  # Your local timezone

# Connect to Powerwall
pw = pypowerwall.Powerwall(host,password,email,timezone)

# Raw JSON Payload Examples
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

# Display String Data
print(",")
print("'String': %r\n" % pw.strings())
print("}")