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
total = 0
for i in newData:
    total = total +i
meanHeight = total/n
print(meanHeight)
