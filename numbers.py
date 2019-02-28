out_file = open("data/output/numbers.csv", "w")

for i in range(15,1501):
   out_file.write("" + str(i) + "\n")



out_file.close()