import csv
file = open("./dados/Nascimentos_RN.csv", "rb")

reader = csv.reader(file, delimiter=';', quotechar=' ')
#lineAux = reader.next()
biggest = 0
city = ""
#print ("\"Total\"")
for line in reader:
	if "\"Total\"" not in line:
		if "\"240000 Municipio ignorado - RN\"" not in line:
			#line = [w.replace('-', '0') for w in line]
			if line[20] == '-':
				line[20] = '1'
			#print line[0]+" = "+line[21] + "/" + line[20]
			if int(line[21]) / int(line[20]) > biggest:
				biggest = int(line[21]) / int(line[20])
				city = line[0]
				#print city

print ("O municipio com maior queda entre 2013 e 2014 foi " +city)