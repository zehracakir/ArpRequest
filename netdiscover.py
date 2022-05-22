import argparse
import scapy.all as scapy
class ARGPing():

    def __init__(self):
        print("******ARPping STARTING******")

    def getUserInput(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-i','--ipaddress',type=str,help="Enter ip address")
        args = parser.parse_args()
        if args.ipaddress != None:
            return args
        else:
            print(args.ipaddress)


    def arpRequest(self,ip):
        arp_request_packet = scapy.ARP(pdst=ip)
        broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        combined_packet = broadcast_packet/arp_request_packet
        answered_list, unanswered_list = scapy.srp(combined_packet, timeout=1)
        answered_list.summary()



if __name__=="__main__":
    argPing = ARGPing()
    ip_Range=argPing.getUserInput()
    argPing.arpRequest(ip_Range.ipaddress)