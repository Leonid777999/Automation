reg_text = '''An Internet Protocol address (IP address) is a numerical label such as 192.168.1.254 
that is connected to a computer network that uses the Internet Protocol for communication.[1][2] 
An IP address serves two main functions: network interface identification and location addressing. 
Internet Protocol version 4 (IPv4) defines an IP address as a 32-bit number.[2] 
However, because of the growth of the Internet and the depletion of available IPv4 addresses,
 a new version of IP (IPv6), using 128 bits for the IP address, was standardized in 1998.[3][4][5] 
 IPv6 deployment has been ongoing since the mid-2000s'''

import re

reg_digit = re.findall(r"[\d]", reg_text)
print(reg_digit)

reg_ip = re.findall(r"IP\w+", reg_text)
print(reg_ip)

reg_whole = re.findall(r"128 bits(.+)", reg_text, re.DOTALL)
print(reg_whole)

reg_address = re.findall(r"\d{3}.\d{3}.\d{1}.\d{3}", reg_text)
print(reg_address)

reg_cut =
