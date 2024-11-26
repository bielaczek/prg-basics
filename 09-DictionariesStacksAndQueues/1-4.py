person = {
   "name": "Jan",
   "surname": "Bielecki",
   "age": 21,
   "hobby": ["conputer games","sudoku"],
   "married": False,
   "phone":{"landline":"123444321","mobile":"777888999"}
   }

print(person['name'])
print(person['hobby'])

for key, value in person.items():
    print(f'{key} : {value}')

person['surname'] = "Nowak"
person['married'] = not person['married']
person['gender'] = "Male"
person['hobby'].append("bicycle")
person['phone']['work'] = '313131444'

for key, value in person.items():
    print(f'{key} : {value}')