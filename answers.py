my_list = []
my_list.extend([10, 20, 30, 40])  
my_list[1] = 15 
my_list2 =[50,60,70]
my_list.extend(my_list2)
del my_list[-1]
sorted_list = sorted(my_list) 
index_of_30 = my_list.index(30)
print(index_of_30)
