# coding=utf-8
import json
import subprocess

# Open JSON file
with open("output.json", "r") as f:

    # Return JSON object
    data = json.load(f)

    for x in data:
            domain = x

    # Iterating through JSON
    count = 0
    #domain = "myclubgroup.co.uk"

    for dns_content in data[domain]['records']:
        if count == 0: 
             #print('spf' + '.' + str(domain))
            dns_name = ('spftest' + '.' + str(domain))
        else: 
             #print('spf{0}'.format(count) + '.' + str(domain))
             dns_name = ('spftest{0}'.format(count) + '.' + str(domain))

        #print(i)
        cf_command = ' -sr TXT ' + dns_name + ' "' + dns_content + '" 300'
        print(cf_command)

        #result = subprocess.run(["cloudflare-dns", cf_command])
        #print(result.stdout)

        count += 1

# pip install cloudflare-dns
# cloudflare-dns -sr TXT spftest.myclubgroup.co.uk "v=spf1 include:_spf.google.com -all"

