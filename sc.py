#program to calculate simple interest and compound interest

p=float(input("Enter principle amount"))
r=float(input("Enter the annual rate of interest"))
t=float(input("Enter time in number of years"))

si=p*r*t/100
ci=p*(1+r)**t-p

print("simple interest",si)
print("compound interest",ci)
