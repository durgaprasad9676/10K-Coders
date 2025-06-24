num=153
temp=num
power =len(str(num))
sum =0

while temp > 0:
    ld =temp%10 #3
    sum+=ld ** power
    temp=temp//10  #for reducing the digit
if sum == num:
    print("Armstrong number")
else:
    print("Not a Armstrong number")