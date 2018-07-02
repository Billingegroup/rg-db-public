from pprint import pprint

import pandas as pd

unis = ['montreal',
        'Vanderbilt University',
        'University of Wisconsin - Milwaukee',
        'Arizona State University',
        'Ohio University - Main Campus',
        'University of Illinois at Urbana-Champaign',
        'Northwestern University',
        'Lehigh University',
        'Rutgers, The State University of New Jersey',
        'Drexel University',
        'University of California - Davis',
        'Kent State University',
        'California Institute of Technology']

regolith_info = {'city': 'Institution_City',
                 'name': 'Institution_Name',
                 'state': 'Institution_State',
                 'zip': 'Institution_Zip'}

df = pd.read_csv('Accreditation_04_2017.csv')
data = df.to_dict('index')

output = {}

for u in unis:
    for n, d in data.items():
        if u.lower() == d.get('Institution_Name', '').lower():
            dd = {'country': 'USA', 'aka': []}
            dd.update({k: data[n][v] for k, v in regolith_info.items()})
            if len(dd['name'].split('University')[0]) > 1:
                dd['aka'].append(dd['name'].split('University')[0].strip())
                dd['aka'].append(dd['name'].split('University')[0].strip().lower())
            data_id = dd['name'].split('University')[0].split(',')[0].strip().lower().replace(' ', '_')
            if data_id == '':
                data_id = dd['city'].lower()
            if data_id == 'champaign':
                data_id = 'uiuc'
            if data_id == 'california_institute_of_technology':
                data_id = 'caltech'
            output.update({data_id: dd})
pprint(output)
from ruamel.yaml import YAML

yaml = YAML()
with open('unis.yaml', 'w') as f:
    yaml.dump(output, f)
