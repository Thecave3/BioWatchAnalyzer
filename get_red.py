# get from all color just red data

input_file = open("data/src/all_color.csv", "r")
out_file = open("data/output/red.csv", "w")

red_data = {}

for line in input_file:
    arr = line.strip("\n").split(",")
    if len(arr) < 3:
        pass

    if "RED" in arr[2]:
        red_data[arr[0]] = arr[1]
        #print(arr[1])
    else:
        print("Not used line: " + line)

for i in range(1,501):
    out_file.write("" + str(red_data[str(i)]) + "\n")

out_file.close()
