student_data={'id1':
             {'name': ['Sara'],
              'class': 5, 
              'subject':['English, Math, Science']},
'id2':
             {'name': ['Danial'],
              'class': 5, 
              'subject':['English, Math, Science']},
'id3':
             {'name': ['Sara'],
              'class': 5, 
              'subject':['English, Math, Science']},
'id4':
             {'name': ['Surya'],
              'class': 5, 
              'subject':['English, Math, Science']},           
}
results={}

for key, value in student_data.items():
    if value not in results.values():
        results[key]=value
print(results)