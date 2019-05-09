

'''
def print_me(number):
    print(number)
'''
# print_me(34)


def even_numbers(numbers):
    '''
     for i in range(1, 21):
        if i % 2 == 0:
            print(i)
    '''
    counter = 0
    item = 1
    list = []
    while counter < numbers:
        if item % 2 == 0:
            counter = counter + 1
            list.append(item)
        item = item + 1
    return list


print(even_numbers(10))
