import csv
file = open("./dados/Nascimentos_RN.csv", "rb")
reader = csv.reader(file, delimiter=';', quotechar=' ')

biggest = 0;
posix = 1;
for line in reader:
	if "\"240810 Natal\"" in line:
		for i in range(1, len(line)-1):
			if biggest< line[i]:
				biggest=line[i]
				posix=i;

file.close()

file = open("./dados/Nascimentos_RN.csv", "rb")
line = file.readline()
line = line.split(';')
print "O ano com o maior numero de nascimentos em Natal eh " + line[posix]