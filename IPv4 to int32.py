import ipaddress

def ip_to_int32(ip):
    return int(ipaddress.ip_address(ip))

print(ip_to_int32("128.32.10.1"))