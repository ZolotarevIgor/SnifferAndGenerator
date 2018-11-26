from scapy.all import sniff
import sys

options = ["ip", "icmp", "udp", "tcp"]

finish = False
if not set(sys.argv[1:]).issubset(set(options)):
    print("Invalid arguments")
else:
    while not finish:
        filter = " or ".join(sys.argv[1:])
        packets = []
        try:
            print("Start sniffing")
            packets = sniff()
        except KeyboardInterrupt:
            pass
        with open("traffic.log", "a") as file:
            for i in packets:
                file.write(i.show2(dump=True) + "\n\n")
        print(f"Packets sniffed: {len(packets)}")
        print("Continue? y/n")
        cont = input()
        if cont is 'n' or cont is 'N':
            finish = True
        else:
            finish = False