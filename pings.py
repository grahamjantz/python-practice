# import subprocess

# ips = [
#     ['A', '198.41.0.4'], 
#     ['B', '199.9.14.201'], 
#     ['C', '192.33.4.12'], 
#     ['D', '199.7.91.13'], 
#     ['E', '192.203.230.10'], 
#     ['F', '192.5.5.241'], 
#     ['G', '192.112.36.4'], 
#     ['H', '198.97.190.53'], 
#     ['I', '192.36.148.17'], 
#     ['J', '192.58.128.30'], 
#     ['K', '193.0.14.129'], 
#     ['L', '199.7.83.42'], 
#     ['M', '202.12.27.33']
# ]

# for name, ip in ips:
#     print(f'Now pinging name server {name}')
#     result = subprocess.run(['ping', ip], stdout=subprocess.PIPE)
#     print(result.stdout.decode('utf-8'))

import os

ips = [
    ['A', "198.41.0.4"], 
    ['B', '199.9.14.201'], 
    ['C', '192.33.4.12'], 
    ['D', '199.7.91.13'], 
    ['E', '192.203.230.10'], 
    ['F', '192.5.5.241'], 
    ['G', '192.112.36.4'], 
    ['H', '198.97.190.53'], 
    ['I', '192.36.148.17'], 
    ['J', '192.58.128.30'], 
    ['K', '193.0.14.129'], 
    ['L', '199.7.83.42'], 
    ['M', '202.12.27.33']
]

for i in ips:
    print('Now pinging name server', i[0])
    comm = 'ping ' + i[1]
    os.system(comm)
    pass