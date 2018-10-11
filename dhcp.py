import struct
import socket
import sys
sys.path.append("./src")
from dchp_message_generator import dhcp_message
sys.path.append("./src/dora")
from Discovery import discovery_check
from Offer import discovery_offer
from Request import discovery_request
from Acknowledgement import discovery_acknowledgement
from dhcp_test import dhcp_test

dhcp_test()

## DHCP Discovery

discovery_check()

## DHCP offer

discovery_offer()

## DHCP request

discovery_request()

## DHCP acknowledgement

discovery_acknowledgement()