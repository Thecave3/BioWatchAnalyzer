from scipy import signal

with open('data/src/data.csv', 'r') as file:
    ir_data = {}
    red_data = {}
    for line in file:
        arra = line.strip('\n').split(',')

        if 'IR' in arra[3]:
            ir_data[arra[0]] = arra[2]
        if 'RED' in arra[3]:
            red_data[arra[0]] = arra[2]

    out_red = open('data/output/out_red.csv', 'w')
    out_ir = open('data/output/out_ir.csv', 'w')

    for i in ir_data.keys():
        # "" + i + ";" +
        out_ir.write(ir_data[i] + "\n")

    for i in red_data.keys():
        # "" + i + ";" +
        # logged = math.log(float(red_data[i]))
        out_red.write(str(red_data[i]) + "\n")

    cwtmatr = signal.cwt(red_data, signal.ricker,red_data)

    with open("data/output/test.csv", "w") as output:
        for i in cwtmatr:
            output.write(i + "\n")
    output.close()

    out_red.close()
    out_ir.close()

raw_data = []

for i in red_data.keys():
    raw_data.append(red_data[i])
