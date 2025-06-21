import sys 

no = 11 
print(sys.getsizeof(no))

print(type(no))
no1 = 11.87
print(sys.getsizeof(no1))
print(type(no1))
no2 = True  
print(sys.getsizeof(no1))
print(type(no2))
no5 = [11,23,2,2,3]
print(type(no5))
print(sys.getsizeof(no5))
no6 = (11,22,33,44,55)
print(type(no6))
no7 = {11,22,33,44,55}
print(type(no7))
print(sys.getsizeof(no7))
no8 = {"PPA" : 21000, "LB" : 25000, "LSP" : 26000}
print(type(no8))
print(sys.getsizeof(no8))
no9 = None
print(type(no9))
print(sys.getsizeof(no9))
no10 = "ashish"
print(type(no10))
print(sys.getsizeof(no10))

print(no5[0])


