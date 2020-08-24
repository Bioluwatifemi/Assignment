my_dict = {}
length = int(input('Enter a number: '))
for num in range(1, length+1):
    my_dict.update({num:num*num})
print(my_dict)
    
    
    
numbers = {2:4, 3:9, 4:16}
numbers2 = {}
your_num = int(input('Enter a number: '))
for key,value in numbers.items():
    numbers2.update({key*your_num:value*your_num})
print (numbers2)