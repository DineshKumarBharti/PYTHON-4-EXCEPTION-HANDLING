# print(1)
# print(2)
# print(3)
# print("div:",4/0)
# print(5)
# print(6)

# OUTPUT- given error
# 1
# 2
# 3
# Traceback (most recent call last):
#   File "c:\Users\IT CARE\Desktop\PYTHON\PYTHON-EXCEPTION HANDLING\ExceptionHandling.py", line 4, in <module>  
#     print("div:",4/0)
#                  ~^~
# ZeroDivisionError: division by zero
#------------------------------------------------------------------------------------------------

# print(1)
# print(2)
# print(3)
# try:
#     print("div:",4/0)
# except:
#     print("Div by zero exception !!")
# print(5)
# print(6)

# OUTPUT
# 1
# 2
# 3
# Div by zero exception !!
# 5
# 6

#------------------------------------------------------------------------------------------


# print(1)
# print(2)
# print(3)

# print("div:",4/2)
# print(5)
# print(6)

# OUTPUT
# 1
# 2
# 3
# div: 2.0
# 5
# 6

#----------------------------------------- 

# print(1)
# print(2)
# print(3)
# a=10
# try:
#     print("div:",4/2)
#     try:
#         print(a)
#     except:
#          print("variable exception ..!")
#     print("No Any Exception...!!")
# except:
#        print("div")
# print(5)
# print(6)

# OUTPUT
# 1
# 2
# 3
# div: 2.0
#10
# variable exception ..!
# No Any Exception...!!
# 5
# 6

#--------------------------------------------

# print(1)
# print(2)
# print(3)
# a=10
# try:
#     print("div:",4/0)
#     try:
#         print(a)
#     except NameError:
#         print("variable exception ..!")
#     print("No Any Exception...!!")
# except ZeroDivisionError:
#        print("div by Zero Exception ..!!!")
# print(5)
# print(6)

# OUTPUT
# 1
# 2
# 3
# div by Zero Exception ..!!!
#10
# 5
# 6

#---------------------------------

# print(1)
# print(2)
# print(3)
# a=10
# try:
#     print("div:",4/0)
#     print(a)
#     print("No Any Exception...!!")
# except ZeroDivisionError:
#        print("div by Zero Exception ..!!!")
# except NameError:
#       print("variable Exception....!!!!")
# finally:
#     print(5)
#     print(6)

# OUTPUT
# 1
# 2
# 3
# div by Zero Exception ..!!!
# 5
# 6

#------------------------------------



#------------------------------------

print(1)
print(2)
print(3)
a=10
try:
    print("div:",4/2)
    print(a)
    print("No Any Exception...!!")
except ZeroDivisionError:
       print("div by Zero Exception ..!!!")
except NameError:
      print("variable Exception....!!!!")
else:
     print("NO Any Exception in try Block....!!!!!")
finally:
    print(5)
    print(6)

# OUTPUT
# 1
# 2
# 3
# div: 2.0
# 10
# No Any Exception...!!
# NO Any Exception in try Block....!!!!!
# 5
# 6