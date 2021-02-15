import struct
import socket

def get_ethernet_frame_payload(raw_data):
    dest_mac, src_mac, prototype = struct.unpack('6s 6s H', raw_data[:14])
    return (
        format_mac_address(dest_mac),
        format_mac_address(src_mac),
        prototype,
        raw_data[14:]
    )

def format_mac_address(bytes_address):
    return ':'.join('{:02x}'.format(byte) for byte in bytes_address).upper()


def format_output(ethernet_data, network_data):
    dest_mac, src_mac, prototype = ethernet_data
    ttl, src_ip_addres, dest_ip_address = network_data
    return f"""Ethernet Layer: Source Mac Address: {src_mac}, Destination Mac Address: {dest_mac}, Prototype: {prototype}\nNetwork Layer: Source IP Address: {src_ip_addres}, Destination IP Address: {dest_ip_address}, TTL: {ttl}\n\n"""
