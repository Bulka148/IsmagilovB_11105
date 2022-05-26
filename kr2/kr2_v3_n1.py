#Вариант 3

import requests

name = input()

res = requests.get(f'https://api.domainsdb.info/v1/domains/search?domain={name}').json()
res = sorted(res['domains'], key=lambda e: e['create_date'])

with open('results.csv', 'w') as f:
    for r in res:
        f.write(r['domain'] + ' ' +  r['update_date'] + ' ' + r['create_date'] + '\n')
