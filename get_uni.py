from pprint import pprint

import pandas as pd

us_states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


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
            data_id = dd['name'].split('University')[0].split(',')[0].strip().lower().replace(' ', '')
            dd['zip'] = str(dd['zip'])
            if 'state' in dd['name'].lower() and us_states[dd['state']] in dd['name']:
                data_id = ''.join([a[0] for a in dd['name'].split(' ')]).lower()
            if 'University of ' in dd['name']:
                data_id = (''.join([a[0] for a in dd['name'].split(' of ')])+dd['city']).lower()
            # DIRTY HACK
            if 'University of Illinois' in dd['name']:
                data_id = 'uiuc'
            if dd['name'] == 'California Institute of Technology':
                data_id = 'caltech'
            if 'rutgers' in dd['name'].lower():
                data_id = 'rutgers'
            if 'u' not in data_id:
                data_id += 'u'
            output.update({data_id: dd})
pprint(output)
from ruamel.yaml import YAML

yaml = YAML()
with open('unis.yaml', 'w') as f:
    yaml.dump(output, f)
