rows = ()#get all element by td to , access as role in table

# data = dict()
data = {'Systotlic':[], 'Diastolic': [], 'Hear_rate': []}
for idx, val in enumerate(rows):
    cols = val #locators as tr
    data['Systotlic'].append(cols[-3].text)
    data['Diastolic'].append(cols[-2].text)
    data['Hear_rate'].append(cols[-1].text)
    
    