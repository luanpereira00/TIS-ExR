import csv
import matplotlib.pyplot as plt

first = 0
second = 0
third = 0
city1 = ""
city2 = ""
city3 = "" 

def compareThird(comp, city):
	global third, city3
	if int(comp) > int(third):
		third=comp
		city3=city
		compareSecond(comp, city)

def compareSecond(comp, city):
	global third, second, city2, city3
	if int(comp) > int(second):
		third=second
		city3=city2
		second=comp
		city2=city
		compareFirst(comp, city)

def compareFirst(comp, city):
	global second, first, city2, city1
	if int(comp)> int(first):
		second=first
		city2=city1
		first=comp
		city1=city


file = open("./dados/Nascimentos_RN.csv", "rb")

reader = csv.reader(file, delimiter=';', quotechar=' ')

line = reader;
for line in reader:
	if "\"Total\"" not in line:
		if "\"240000 Municipio ignorado - RN\"" not in line:
			#stcity = sumArrayColumns(line, 17, 21)
			result = 0
			for i in range(17, 21):
				if line[i]=='-':
					line[i]=0
				result+=int(line[i])
			#print (result)
			compareThird(result, line[0])
print(city1)
print(city2)
print(city3)

#https://matplotlib.org/users/pyplot_tutorial.html
reader = csv.reader(file, delimiter=';', quotechar=' ')
plt.axis([2010, 2011, 2012, 2013, 2014])
for line in reader:
	if city1 in line:
		plt.plot([line[i]] for i in range(17, 21))
	if city2 in line:
		plt.plot([line[i]] for i in range(17, 21))
	if city3 in line:
		plt.plot([line[i]] for i in range(17, 21))

plt.show()
			

#print ("O municipio com maior queda entre 2013 e 2014 foi " +stcity)