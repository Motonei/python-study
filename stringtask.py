#Q1
name=" JOHn"
name=name.strip()
print(name)
name=name.lower()
print(name)
#2a
sentence_one='The Dog Breed is German Shepherd'
print(sentence_one[8:23])
#2b
sentence_two='Defeats for the clinton forces,this was her moment of triump'
print(sentence_two[16:30])
# Q3
sen='The lazy dog;ran so fast;it hit the wall.'
sen=sen.split(';')
print(sen)
print(len(sen))
# Q4
first_name=' Joh.n'
last_name=' Do,e'
full_name=first_name+" "+last_name
print(full_name)
full_name=full_name.replace('.','').replace(',','')
print(full_name)
full_name=full_name.strip()
print(full_name)
# Q5
r = '["E","W","C"]'
result = r.replace('[', '').replace(']', '').replace('"', '').replace(',', '')
print(result)
