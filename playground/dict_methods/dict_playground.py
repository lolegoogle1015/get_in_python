student = {'name': "Oleh", 'age': "21", 'courses': ['Math', 'Python']}

student.update({'name': "oleh"})
print(student.get('name', 0), student)

print(student.pop('age'), student)
student.items()
student.keys()
student.values()
