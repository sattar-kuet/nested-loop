data = [-1000000,-5,6,8,9,100,200,500]
n = len(data)
maximum = data[0]*data[1]

if maximum <data[n-1]*data[n-2]:
    maximum = data[n-1]*data[n-2]

print(maximum)