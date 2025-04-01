import datetime

from requests import get, post, delete

print(get('http://localhost:5000/api/jobs').json())

print(get('http://localhost:5000/api/jobs/1').json())

print(get('http://localhost:5000/api/jobs/999').json())
# новости с id = 999 нет в базе

print(get('http://localhost:5000/api/jobs/q').json())

print(post('http://localhost:5000/api/jobs', json={}).json())

print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 1}).json())

print(post('http://localhost:5000/api/jobs',
           json={'team_leader': 1,
                 'job': 'Текст новости',
                 'work_size': 10,
                 'collaborators': '1, 2, 3',
                 'start_date': datetime.datetime.now(),
                 'end_date': datetime.datetime.now()    ,
                 'is_finished': False}).json())

print(delete('http://localhost:5000/api/jobs/999').json())
# новости с id = 999 нет в базе

print(delete('http://localhost:5000/api/jobs/1').json())