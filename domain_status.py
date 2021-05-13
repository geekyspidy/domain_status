import re
import sys
import requests

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
        print(domain+" -> "+str(r.status_code))
    except requests.ConnectionError:
        print(domain+" -> failed to connect")
    
