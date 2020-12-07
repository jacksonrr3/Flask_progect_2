import json

from data import teachers, goals

with open('data_base.json', 'w') as jf:
    db = {'goals': goals, 'teachers': teachers}
    json.dump(db, jf)
    print()

