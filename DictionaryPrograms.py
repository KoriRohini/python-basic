data = {'rohini': 32, 'sayama': 55, 'vasu': 67}

print(data['sayama'])
print(data.get('roo', 'user not found'))

data.pop('rohini')
del data['sayama']