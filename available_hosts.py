import ipaddress as ip


net4 = ip.ip_network('2.2.2.0/24')
net = net4.netmask

available_hosts = list(net4.hosts())

print(available_hosts)

host1 = available_hosts[0]
print(host1)
host14 = available_hosts[0:4]
print(host14)
host2 = available_hosts[-1]
print(host2)
host1040 = available_hosts[10:40]
print(host1040)