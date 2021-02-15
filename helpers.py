
def format_output(ethernet_data, network_data):
    dest_mac, src_mac, prototype = ethernet_data
    print(network_data)
    src_ip_addres, dest_ip_address, ttl = network_data
    return  f"""Ethernet Layer: Source Mac Address: {src_mac}, Destination Mac Address: {dest_mac}, Prototype: {prototype}\n"""\
            f"""========> Network Layer: Source IP Address: {src_ip_addres}, Destination IP Address: {dest_ip_address}, TTL: {ttl}\n\n"""
