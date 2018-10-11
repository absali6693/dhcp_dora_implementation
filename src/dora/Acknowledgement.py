import struct
import socket
import sys
sys.path.append("./src")
from dchp_message_generator import dhcp_message

## DHCP acknowledgement
def discovery_acknowledgement():
    operation_code = 2
    hardware_type = 1
    hardware_address_length = 6
    transaction_identifier = 1200
    client_IP_address = '0.0.0.0'
    your_IP_address = '192.168.20.20'
    server_IP_address = '192.168.20.1'
    gateway_IP_address = '0.0.0.0'
    client_hardware_address= 'fe:1d:20:1c:f6:8d'
    DHCACK = dhcp_message(operation_code,
                    hardware_type,
                    hardware_address_length,
                    transaction_identifier,
                    client_IP_address,
                    your_IP_address,
                    server_IP_address,
                    gateway_IP_address,
                    client_hardware_address
                    )

    test = socket.inet_ntoa(DHCACK[12:16])
    print('Sanity Check (1): ', test == '0.0.0.0')
    test = socket.inet_ntoa(DHCACK[16:20])
    print('Sanity Check (2): ', test == '192.168.20.20')
    test = socket.inet_ntoa(DHCACK[20:24])
    print('Sanity Check (3): ', test == '192.168.20.1')