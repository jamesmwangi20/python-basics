m = int(input("maths: "))
p = int(input("physics: "))
e = int(input("english: "))
k = int(input("kiswahili: "))
c = int(input("comp: "))





sum = m + p + e + k + c

average = sum/5



if average >= 0 and average <= 39:
    print("E")

if average >= 40 and average <= 50:
    print("D")

if average >= 51 and average <= 60:
    print("C")

if average >= 61 and average <= 70:
    print("B")

if average >=71 and average <=100:
    print("A")
else:
    print("invalid input")























