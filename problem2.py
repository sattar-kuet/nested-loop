data = [-1,-9,-8,10,11,12,13]
n = len(data)
maximum = data[n-1]*data[n-2]*data[n-3]
if data[0]*data[1]*data[n-1]>maximum:
    maximum = data[0]*data[1]*data[n-1]

print(maximum)


