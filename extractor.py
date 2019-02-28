from scipy.signal import butter, lfilter


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


input_file = open("data/src/data.csv", "r")
out_file = open("data/output/data_correct.csv", "w")

ir_data = {}
red_data = {}

for line in input_file:
    arr = line.strip("\n").split(",")
    if len(arr) < 3:
        pass

    if "IR" in arr[3]:
        ir_data[arr[0]] = arr[2]
    elif "RED" in arr[3]:
        red_data[arr[0]] = arr[2]
    else:
        print("Not used line: " + line)

for i in red_data.keys():
    division = float(red_data[i])/ float(ir_data[i])
    #division = butter_bandpass_filter(division, 0.93, 0.98, 5000)
    out_file.write("" + str(division) + "\n")

out_file.close()
