import ipaddress as ip


net4 = ip.ip_network('2.2.2.0/24')
net = net4.netmask

AddressesNum = net4.num_addresses
print(AddressesNum)

available_hosts = len(list(net4.hosts()))
print(available_hosts)

