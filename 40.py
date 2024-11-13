keys={'a','b','c','d','e'}
value=['new']
my_list=dict.fromkeys(keys,value)
value.append(2)
print (my_list)#{'c': ['new', 2], 'e': ['new', 2], 'a': ['new', 2], 'd': ['new', 2], 'b': ['new', 2]}