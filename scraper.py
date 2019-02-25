import matplotlib.pyplot as plt

with open('to_be_scraped.txt','r') as file:
	ir_data = {}
	red_data = {}
	for line in file:
		arra = line.strip('\n').split(',')
		if 'IR' in arra[2]:
			ir_data[arra[0]] = arra[1]
		if 'RED' in arra[2]:
			red_data[arra[0]] = arra[1]

	out_red = open('out_red.csv','w')
	out_ir = open('out_ir.csv','w')

	for i in ir_data.keys():
		out_ir.write(""+i+";"+ir_data[i]+"\n")

	for i in red_data.keys():
		out_red.write(""+i+";"+red_data[i]+"\n")

	out_red.close()
	out_ir.close()


 
raw_data = []

# for i in ir_data.keys():
#	raw_data.append(ir_data[i])

for i in red_data.keys():
	raw_data.append(red_data[i])
#	print(red_data[i])

#plt.plot(raw_data)


#plt.title("Diagramma")
#plt.xlabel("Tempo")
#plt.ylabel("Intensità")


#plt.show()