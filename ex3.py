


file = open("test.txt", 'r')
print(file.read())
file.close()

file = open("test.txt", 'w')
file.write("bvjhasbjkbvsabjbasdv\nkhafsihiashhasff\nuyguaysgug")
file.close()

file = open("test.txt", 'a')
file.write("\nRahul")
file.close()

'''
file = open("test.txt", 'r')
print(file.read())
file.close()
'''


'''
file = open("test.txt", 'w')
file.truncate()
file.close()
'''


file = open("test.txt", 'r')
print(file.readline())
file.close()

file = open("test.txt", 'r')
for line in file:
    print(line)
file.close()
