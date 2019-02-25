ir_file = open('out_ir.csv','r')
red_file = open('out_red.csv','r')

merged_file = open('merged.csv','w')

line_one = ir_file.readline()
line_two = red_file.readline()
try:
    while line_one and line_two:
        date_one = float(line_one.strip('\n').split(';')[1]) 
        date_two = float(line_two.strip('\n').split(';')[1])
        to_write =  date_two / date_one
        if to_write < 1 and to_write > 0.98:
            merged_file.write(str(to_write)+"\n")
        print to_write
        line_one = ir_file.readline()
        line_two = red_file.readline()
except IndexError as e:
    print "ERRORE"
    print line_one
    print line_two

merged_file.close()