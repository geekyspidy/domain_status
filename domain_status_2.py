import re
import sys
import requests
import json

from requests.api import request
from requests.models import Response

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


f = open(sys.argv[1])
file_data = f.read()
domain_list1 = re.findall(
    r'[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9]?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]', file_data)
domain_list2 = []
for domain in domain_list1:
    if domain not in domain_list2:
        domain_list2.append(domain)

open('domains.txt', 'w').close()

with open('domains.txt', 'w') as domains:
    for domain in domain_list2:
        domains.write('%s\n' % domain)

#print(domain_list2)

for domain in domain_list2:
    try:
        r = requests.head("https://"+domain)
        # print(domain+" -> "+str(r.status_code))
        if (r.status_code >= 200 or r.status_code < 500):
            # res = requests.get("https://"+domain)
            res = r.headers
            if ("X-Frame-Options" in r.headers):
                print domain+" -> "+str(r.status_code)+ " -> "+ res['X-Frame-Options']
            else:
                print domain+" -> "+str(r.status_code)+ " -> "+ bcolors.WARNING+ "X-Frame-Options header is missing" + bcolors.ENDC
    except requests.ConnectionError:
        continue
        # print(domain+" -> failed to connect")
    
