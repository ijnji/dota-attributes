#!/usr/bin/env python3

import bs4
import json
import re
import urllib.request

loc = 'http://wiki.teamliquid.net/dota2/Hero_Roles'
roles = [
    'Carry',
    'Nuker',
    'Initiator',
    'Disabler',
    'Durable',
    'Escape',
    'Support',
    'Pusher',
    'Jungler',
    'Complexity',
]

req = urllib.request.urlopen(loc).read()
soup = bs4.BeautifulSoup(req, 'html.parser')

heroes = {}
for role in roles:
    for n in range(1, 4):
        q = ' %s %s' % (n*'■', role)
        th = soup.find(string=re.compile(q))
        entries = th.parent.parent.find_next_sibling('tr').find_all('a')
        for e in entries:
            name = e.attrs['title']
            if name not in heroes: heroes[name] = {}
            heroes[name][role] = n

with open('hero-attributes.json', 'w') as f:
    f.write(json.dumps(heroes, indent=2, sort_keys=True))
