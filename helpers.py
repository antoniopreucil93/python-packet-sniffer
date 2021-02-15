
def format_output(payload):
    dest_mac, src_mac, _ = payload["ethernet_data"]
    ttl, _, src_ip_addres, dest_ip_address = payload["internet_data"]
    icmp_type = payload["icmp_data"]
    src_port, dest_port, seq, ack = payload["tcp_data"]
    src_port, dest_port, size = payload["udp_data"]

    return  f"""Ethernet Layer: Source Mac Address: {src_mac}, Destination Mac Address: {dest_mac}\n"""\
            f"""======> Network Layer: Source IP Address: {src_ip_addres}, Destination IP Address: {dest_ip_address}, TTL: {ttl}\n\n"""\
            f"""======> ICMP Type: {icmp_type}"""\
            f"""===============> TCP Source Port: {src_port}, Destination Port: {dest_port}"""\
            f"""===============> UDP Source Port: {src_port}, Destination Port: {dest_port}"""