#!/usr/bin/env/python
import scapy.all as scapy
import argparse
def get_arguments():
    parser=argparse.ArgumentParser()
    parser.add_argument("-t","--target",dest="target",help="Target IP/IP Range.")
    options=parser.parse_args()
    return options
def scan(ip):
    arp_req=scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast=broadcast/arp_req
    answered_list=scapy.srp(arp_req_broadcast,timeout=1,verbose=False)[0]

    clients_list=[]
    
    for element in answered_list:
        client_dict={"ip":element[1].psrc,"mac":element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list
def print_res(result_list):
    print("IP\t\t\tMAC Address\n---------------------------------------------------")
    for client in result_list:
        print(client["ip"]+"\t\t"+client["mac"])

    
options=get_arguments()
scan_res=scan(options.target)
print_res(scan_res)
