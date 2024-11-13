my_dict={'name':'Eltın John','age':22}
my_dict['age']=27
my_dict['adress']='Edirne'
print(my_dict)#{'name': 'Eltın John', 'age': 27, 'adress': 'Edirne'}
print(my_dict.get('age'))#aradığımız key dict'e yok ise output None olarak döner
