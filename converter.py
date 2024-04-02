# coding=utf-8
import json

# Open JSON file
with open("output.json", "r") as f:

    # Return JSON object
    data = json.load(f)

    for x in data:
            domain = x

    # Iterating through JSON
    count = 0
    #domain = "myclubgroup.co.uk"

    for i in data[domain]['records']:
        if count == 0: 
             #print('spf' + '.' + str(domain))
            start_dns = ('spf' + '.' + str(domain))
        else: 
             #print('spf{0}'.format(count) + '.' + str(domain))
             start_dns = ('spf{0}'.format(count) + '.' + str(domain))

        #print(i)
        cf_command = "cloudflare-dns " + start_dns + ' "' + i + '"'
        print(cf_command)
        count += 1
