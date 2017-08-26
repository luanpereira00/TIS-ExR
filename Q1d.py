import csv
import matplotlib.pyplot as plt

file = open("./dados/Nascimentos_RN.csv", "rb")
reader = csv.reader(file, delimiter=';', quotechar=' ')

line = reader;
mossoro=""
parnamirim=""
natal=""
caico=""
first=""
for line in reader:
	if "\"Municipio\"" in line:
		mossoro = line
	if "\"240800 Mossoro\"" in line:
		mossoro = line
	if "\"240800 Mossoro\"" in line:
		mossoro = line
	if "\"240810 Natal\"" in line:
		natal = line
	if "\"240325 Parnamirim\"" in line:
		parnamirim = line
	if "\"240200 Caico\"" in line:
		caico = line
		

print(mossoro)
print(natal)
print(parnamirim)
print(caico)

plt.axis([[first[i]] for i in range(1, len(first)-1)])
plt.plot([mossoro[i]] for i in range(1, len(mossoro)-1))
plt.plot([natal[i]] for i in range(1, len(natal)-1))
plt.plot([parnamirim[i]] for i in range(1, len(parnamirim)-1))
plt.plot([caico[i]] for i in range(1, len(caico)-1))

plt.show()
