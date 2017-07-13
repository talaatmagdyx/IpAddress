import ipaddress as ip

CLASS_C_ADDR = '192.168.1.0'

if __name__ == '__main__':
    not_configured = True
    while not_configured:
        prefix = input("Enter the prefix (24-30): ")
        prefix = int(prefix)
        if prefix not in range(23,31):
            raise Exception("Prefix must be btw (24-30)")
        net_addr = CLASS_C_ADDR + '/' +str(prefix)
        print("network address : %s"%net_addr)
        try:
            network = ip.ip_network(net_addr)
        except:
            raise Exception("Failed to create network")
        print("This is prefix will give %s IP addresses"%network.num_addresses)
        print("Network configuration will be :")
        print("\t network address: %s"%str(network.netmask))
        print("\t Broadcast address : %s"%str(network.broadcast_address))
        first_ip , last_ip = list(network.hosts())[0],list(network.hosts())[-1]
        print("\t host IP addresses: from %s to %s "%(first_ip , last_ip))
        status = input("Is this configuration OK [Y/N]? ")
        status = status.lower()
        if status.strip() =='y':
            not_configured = False

