#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
from datetime import datetime
import os
import textwrap


file_path = 'info.json'
if not os.path.exists(file_path):
    with open(file_path, 'w') as file:
        event_date = datetime.today()
        event_date = event_date.replace(year=event_date.year + 1, month=3, day=22, hour=11, minute=0)
        event_date = event_date.replace(day=event_date.day + 5 - event_date.weekday())
        file.write(textwrap.dedent('''
        {{
            "Sigma address": [
                "123 Main St",
                "Anywhere MI 00000-0000"
            ],
            "Event name": "Founders Day Brunch",
            "Event date and time": "{:%Y-%m-%d %H:%M}"
        }}
        '''.format(event_date)).lstrip())

file_path = 'donations.csv'
if not os.path.exists(file_path):
    with open(file_path, 'w') as file:
        csv.writer(file).writerows([
            ['Display name',         'Last name', 'Street',  'City',  'State',  'ZIP', 'Amount', 'Scholarships only'],
            ['FirstName1 LastName1', 'LastName1', 'Street1', 'City1', 'State1', 'ZIP1', 100,     'FALSE'],
            ['FirstName2 LastName2', 'LastName2', 'Street2', 'City2', 'State2', 'ZIP2', 200,     'TRUE']
        ])

directory_name = 'support'
if not os.path.exists(directory_name):
    os.makedirs(directory_name)
