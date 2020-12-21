import csv,math
with open("data.csv") as f:
    reader = csv.reader(f)
    file_data = list(reader)


file_data = file_data[0]
print("File Data - ",file_data)

add = 0
num = []
for i in file_data:
    n_num = int(i)
    num.append(n_num)
    #print(num)

for i in num:
    add += i
    #print("Add = ",add)

print("Sum of values = ",add)
mean = add / len(num)
print("Mean = ",mean)


sub=[]
for i in num:
    s_sub = i - mean
    sub.append(s_sub)
    #print("sub = ",sub)


sqr = []
for i in sub:
    s_sqr = i**2
    sqr.append(s_sqr)
    #print("sqr = ",sqr)

total = 0
for i in sqr:
    total += i
    #print("Total = ",total)

print("Total after sqr= ",total)
div = total/len(num)
print("Ans after div = ",div)


sqrroot = math.sqrt(div)
print("Standard deviation = ",sqrroot)




    
