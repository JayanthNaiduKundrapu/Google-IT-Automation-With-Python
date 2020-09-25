#!/usr/bin/env python3
import os
import requests
path = os.path.expanduser('/') + '/data/feedback/'
for file in os.listdir(path):
        data = {}
        with open(os.path.join(path,file), 'r') as f:
                lines = f.readlines()
                data['title'] = lines[0].strip()
                data['name'] = lines[1].strip()
                data['date'] = lines[2].strip()
                data['feedback'] = lines[3].strip()
        response = requests.post('http://35.192.50.101/feedback/',json = data)
        if not response.ok:
                raise Exception('POST failed with status code {}'.format(response.status_code))
        print('Successfully added feedback')


