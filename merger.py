# give all color file, creates a new file merged.csv with red data / ir data
input_file = open("data/src/all_color.csv", "r")
out_file = open("data/output/merged.csv", "w")

ir_data={}
red_data={}
for line in input_file:
    arr = line.strip("\n").split(",")
    if len(arr) < 3:
        print("invalid line: "+line)
        pass

    if "RED" in arr[2]:
        red_data[arr[0]] = arr[1]
    elif "IR"in arr[2]:
        ir_data[arr[0]] = arr[1]
    else:
        print("Not used line: " + line)

for i in range(15,1501):
    ir_elem = float(ir_data[str(i)])
    red_elem = float(red_data[str(i)])
    division = red_elem/ir_elem
    out_file.write("" + str(division) + "\n")
    print(""+str( ir_elem) +"/"+str(red_elem)+" = " +str(division))

input_file.close()
out_file.close()
