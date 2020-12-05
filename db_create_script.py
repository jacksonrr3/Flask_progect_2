from data import teachers
import json

with open('data_base.json', 'w') as jf:
    json.dump(teachers, jf)

