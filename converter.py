# coding=utf-8
import json

# Open JSON file
f = open('result.json')
 
# Return JSON object
data = json.load(f)
 
# Iterating through JSON
count = 0
domain = "myclubgroup.co.uk"

for i in data["myclubgroup.co.uk"]['records']:

    if count == 0: print('spf' + '.' + str(domain))
    else: print('spf{0}'.format(count) + '.' + str(domain))

    print(i)
    count += 1
 
# Close JSON file
f.close()