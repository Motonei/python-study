my_dict={
    'name':'Abigael Letina',
    'Gender':'female',
    'age':45,
    'city':'Nairobi'
    
    

}


print(my_dict['Gender'])
print(my_dict['age'])
# update and add age
my_dict['age']=40
print(my_dict)
# add new property
my_dict['occupation']='Software developer'
print(my_dict)
my_dict['county']='nyeri'

print(my_dict)
my_dict['county']='kisii'

print(my_dict)
my_dict.pop("age")
print(my_dict)
