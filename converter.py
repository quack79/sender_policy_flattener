# coding=utf-8
import json
import subprocess

# requires: pip install cloudflare-dns
# this script must only be run after spflat!

# get API token from CloudFlare, then 
# set CF_API_TOKEN in environment

with open("output.json", "r") as f:

    data = json.load(f)

    for x in data:
            domain = x

    count = 0

    for dns_content in data[domain]['records']:
        if count == 0: 
            dns_name = ('spf' + '.' + str(domain))
        else: 
             dns_name = ('spf{0}'.format(count) + '.' + str(domain))

        cf_command = 'cloudflare-dns -sr TXT ' + dns_name + ' "' + dns_content + '" 300'
        print(cf_command)

        result = subprocess.run(cf_command)
        #print(result.stdout)

        count += 1
