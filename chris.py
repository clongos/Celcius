convert = raw_input("[1]Celcius to Farenheit or [2]Farenheit to Celcius?: ")
if convert == "1":
    value = raw_input("Value to Celcius: ")
    value = float(value)*9/5+32
    print "Value to Farenheit: %s" % (value)
elif convert == "2":
    value = raw_input("Value to Farenheit: ")
    value = (float(value)-32)*5/9
    print "Value to Celcius: %s" % (value)
else:
    print "Invalid"
