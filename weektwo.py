my_list = []

#append 10, 20, 30, 40 to my_list
for i in range(10, 41, 10):
    my_list.append(i)

#insert 15 at the second position
my_list.insert(1, 15)
print(my_list)

#extend my_list with another list [50, 60, 70]
my_list.extend([50, 60, 70])
print(my_list)

#remove the last element
my_list.pop()

#sort in ascending order
my_list.sort()
print(my_list)

# find and print the index of 30
init_index = 0
for element in my_list:
    if element == 30:
        print(f'The index of 30 is {init_index}')
    else:
        init_index += 1
