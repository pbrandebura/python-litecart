

list = ['a', 'b', 'c']
list2 = ['a', 'c']
list3 = [x for x in list if x not in list2]
print('to jest lista: ' + str(list3))