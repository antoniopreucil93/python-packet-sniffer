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
        payload = {};

        hex_data, addr = socket_conn.recvfrom(65536)
        ethernet_data = get_ethernet_frame_payload(hex_data)

        eth_proto_num = ethernet_data["payload"][2]

        payload['ethernet_data'] = ethernet_data["payload"]

        if eth_proto_num == 8:
            internet_data = get_ipc4_packets(ethernet_data["data"])

            payload['internet_data'] = internet_data["payload"]

            int_proto_num = internet_data["payload"][1]
            int_raw_data = internet_data["data"]

            if int_proto_num == 1:
                icmp_data = get_icmp_packet(int_raw_data)
                payload['icmp_data'] = icmp_data['payload']
            if int_proto_num == 6:
                tcp_data = get_tcp_segment(int_raw_data)
                payload["tcp_data"] = tcp_data["payload"]
            if int_proto_num == 17:
                udp_data = get_udp_datagram(int_raw_data)
                payload["udp_data"] = udp_data["payload"]

            interface.add_trafic_record(format_output(payload))
        interface.update_view()

main()

