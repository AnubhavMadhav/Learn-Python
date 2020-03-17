'''Printed the value from a Function'''
# def average(a,b):
#     print("Average pf two numbers is :",(a+b)/2)
#
# average(10,20)
#
# '''Return the value from a Function'''
# def average2(a,b):
#     return (a+b)/2
#
# avg = average2(10,20)
# print(avg)

'''Using keywords arguments'''

def average(a,b):
    print(a)
    print(b)
    return (a+b)/2

print(average(b=10,a=20))           # this assigns value and the above printed variables are assigned the same values