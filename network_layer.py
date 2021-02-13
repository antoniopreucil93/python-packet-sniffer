import struct
import socket

def get_ethernet_frame_payload(raw_data):
    dest_mac, src_mac, prototype = struct.unpack('6s 6s H', raw_data[:14])
    return (
        parse_mac_address(dest_mac),
        parse_mac_address(src_mac),
        prototype,
        raw_data[14:]
    )

def parse_mac_address(bytes_address):
    return ':'.join('{:02x}'.format(byte) for byte in bytes_address).upper()

def format_output(ethernet_data, network_data):
    dest_mac, src_mac, prototype = ethernet_data
    ttl, proto, src, dest = network_data
    return f"""Ethernet Layer: Source Mac Address: {src_mac}, Destination Mac Address: {dest_mac}, Prototype: {prototype}\nNetwork Layer: Source IP Address: {src}, Destination IP Address {dest}\n\n"""
