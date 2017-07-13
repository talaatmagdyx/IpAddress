import ipaddress as ip


net4 = ip.ip_network('2.2.2.0/24')
net = net4.netmask

subnets1 = list(net4.subnets())
print(subnets1)

supperSub = net4.supernet()
print(supperSub)