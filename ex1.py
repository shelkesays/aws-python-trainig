print("Hello World")
print(3)
print("Hello World.", "This is my first program")
print("This is second line. " + "I am testing this too")
print("Third line.", 4)
print("Fourth Line," + str(5))

a = 2
print(str(a)*2)
b = "R"
print(b*4)

c = 3.414
print(c)
print(int(c))
print(c%1)

d_list = [1, 2, 3]
d_list.append(4)
print(d_list)
print(d_list[3])

del d_list[0]

print(d_list)

f_dict = {'name': 'Rahul'}
f_dict['lastname'] = 'Shelke'
f_dict.update({'phone': '9876543210'})
print(f_dict)
f_dict.update({'phone': '1234567890'})
print(f_dict)

string = "This is {} test".format(a)
print(string)

string = "This is {0} and {1} test".format(a, b)
print(string)

string = "This is {a} and {b} test".format(b=c, a=a)
print(string)
