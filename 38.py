my_list={x:x*x for x in range(11)if x %2==1}
new_list=my_list.copy()
new_list.clear()
print(new_list)
print(my_list)