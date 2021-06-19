import csv 
with open('Data.csv', newline=  '' )as f:
    reader = csv.reader(f)
    data = list(reader)
data.pop(0)
newData=[]
for i in range(len(data)):
    num = data[i][1]
    newData.append(float(num))
n = len(newData)
newData.sort()
if n%2==0:
    m1 = float(newData[n//2])
    m2 = float(newData[n//2 +1])
    sumHeight = m1+ m2
    medianHeight = sumHeight/2
else:
    medianHeight = float(newData[n//2])
print(medianHeight)