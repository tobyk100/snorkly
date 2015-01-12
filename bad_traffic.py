import dpkt

def land_attack(ip, tcp):
    if (ip.src == ip.dst and tcp.dport == tcp.sport):
        return (1.0, "Land attack is taking place!")
    else:
        return (0.0, "It's all good")

def check_bad_traffic(pkt):
    eth = dpkt.ethernet.Ethernet(pkt)
    ip = eth.data
    tcp = ip.data
    return land_attack(ip, tcp)
