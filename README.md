Sender Policy Flattener
=======================

To fix the more than 10 DNS lookups problem.

Solution? Follow the SPF records, query them, and create a condensed list of IP addresses.

#### But wait... What if the downstream records change?

Part of what the script does is that it creates a JSON file that keeps track of the last list of IP Addresses that your combination of SPF records had.

When the hashsum of your IP Addresses changes, it will send out an email (or just dump HTML if it can't find an email server) with a handy diff & BIND format for viewing what has changed, and promptly updating it.

You could theoretically extract the flat IP records from the resulting JSON file and automatically update your DNS configuration with it.

--- This is actually what I'm currently working on!!

--- Trying to use the output JSON along with [cloudflare-dns](https://github.com/ZigZagT/cloudflare-dns)

Installation
--------------------

#### Via git clone

```shell
git clone https://github.com/quack79/sender_policy_flattener.git
cd sender_policy_flattener
pip install poetry
poetry lock --no-update
poetry install
```

Usage
----------------

```
usage: spflat [-h] [-c CONFIG] [-r RESOLVERS] [-e MAILSERVER] [-t TOADDR]
              [-f FROMADDR] [-s SUBJECT] [-D SENDING_DOMAIN] [-d DOMAINS]
              [-o OUTPUT]

A script that crawls and compacts SPF records into IP networks. This helps to
avoid exceeding the DNS lookup limit of the Sender Policy Framework (SPF)
https://tools.ietf.org/html/rfc7208#section-4.6.4

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        Name/path of JSON configuration file
  -r RESOLVERS, --resolvers RESOLVERS
                        Comma separated DNS servers to be used
  -e MAILSERVER, -mailserver MAILSERVER
                        Server to use for mailing alerts
  -t TOADDR, -to TOADDR
                        Recipient address for email alert
  -f FROMADDR, -from FROMADDR
                        Sending address for email alert
  -s SUBJECT, -subject SUBJECT
                        Subject string, must contain {zone}
  -D SENDING_DOMAIN, --sending-domain SENDING_DOMAIN
                        The domain which emails are being sent from
  -d DOMAINS, --domains DOMAINS
                        Comma separated domain:rrtype to flatten to IP
                        addresses. Imagine these are your SPF include
                        statements.
  -o OUTPUT, --output OUTPUT
                        Name/path of output file
```

Command-line example

```shell
poetry run spflat -c settings.json
```

A ``settings_example.json`` config file is provided in the examples folder.


Example email format
--------------------
<img src='https://raw.githubusercontent.com/cetanu/sender_policy_flattener/master/example/email_example.png' alt='example screenshot'></img>
