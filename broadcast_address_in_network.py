import ipaddress as ip


net4 = ip.ip_network('2.2.2.0/23')
net = net4.netmask

net1 = str(net4.netmask)

n_address = net4.network_address
broadcast = net4.broadcast_address
print(n_address)
print(broadcast)
print(type(n_address))
print(type(broadcast))
