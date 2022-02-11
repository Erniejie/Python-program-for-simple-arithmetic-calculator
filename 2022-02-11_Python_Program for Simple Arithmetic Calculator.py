# Python program for simple arithmetic calculator
#Computer Programming Tutor- Feb 8, 2022

def add(no1,no2):
    return no1 + no2

def subtract(no1,no2):
    return no1 - no2

def multiply(no1,no2):
    return no1*no2

def divide(no1,no2):
    return no1/no2

print("Please Press: OPTION Operation -\n"\
      "1.Add\n"\
      "2.Subtract\n"\
      "3.Multiply\n"\
      "4.Divide\n"\



      )




option = int(input("OPTION Operation form 1,2,3,4:"))

n1 = int(input("Input First Number:"))
n2 = int(input("Input Second Number:"))

if option == 1:
    print(n1,"+",n2, "=",
                           add(n1,n2)
           )

elif option == 2:
    print(n1,"-",n2, "=",
                           subtract(n1,n2)
           )

elif option == 3:
    print(n1,"*",n2, "=",
                           multiply(n1,n2)
           )

elif option == 4:
    print(n1,"/",n2, "=",
                           divide(n1,n2)
           )

else:
    print("Invalid Input")



    





