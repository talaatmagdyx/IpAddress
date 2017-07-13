import ipaddress as ip


net4 = ip.ip_network('2.2.2.0/28')
net = net4.netmask

net1 = str(net4.netmask)
print(net)
print(net1)