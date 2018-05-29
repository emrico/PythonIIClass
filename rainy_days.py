file = open("tmpprecip2012.dat","r")
rain_days = 0
precipitation = 0

for line in file:
    line_precip = float(line[9:13])
    if(line_precip > 0):
        rain_days += 1
        precipitation += line_precip
print("Rain Days = {:.2f}".format(rain_days))
print("Rain Amount = {:.2f}".format(precipitation))
