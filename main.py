import socket

from network_layer import *
from view import View
from internet_layer import *
from helpers import *
from transmission_layer import *

def main():
    interface = View()

    socket_conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(3))

    while True:
        hex_data, addr = socket_conn.recvfrom(65536)
        (dest_mac, src_mac, eth_proto_num, eth_raw_data) = get_ethernet_frame_payload(hex_data)

        if eth_proto_num == 8:
            (ttl, int_proto_num, src_ip_addres, dest_ip_address, int_raw_data) = get_ipc4_packets(eth_raw_data)

            if int_proto_num == 1:
                icmp_data = get_icmp_packet(int_raw_data)
                print(icmp_data)
            if int_proto_num == 6:
                tcp_data = get_tcp_segment(int_raw_data)
                print(tcp_data, ' tcp data')
            if int_proto_num == 17:
                udp_data = get_udp_datagram(int_raw_data)
                print(udp_data, ' udp data')


            context = format_output((dest_mac, src_mac, eth_proto_num), (src_ip_addres, dest_ip_address, ttl))
            interface.add_trafic_record(context)
        interface.update_view()

main()

