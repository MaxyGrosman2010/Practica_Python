#Exercises 1
dog = {}
dog = {'name': 'Chapi', 'breed': 'Sharpei Chinese', 'legs': 4, 'age': '13'}
student = {'first_name': 'Maximiliano', 'last_name': 'Grosman', 'gender': 'Male', 'age': 29,
    'marital status': 'single', 'skills': ['Front-End', 'Back-End', 'Database', 'Communication', 'Leadership'],
    'country': 'Argentina', 'address': 'Capital'}
print(len(student))
print(type(student['skills']))
student['skills'].append('Soft Skill Training')
student['skills'].append('Node.JS')
keys = student.keys()
values = student.values()
tuple_dict = student.items()
del student['address']
del dog