from scapy.all import sendp
from scapy.layers.inet import IP, UDP
from tkinter import Tk, Label, Entry, TOP, W, Button, RIGHT
from functools import partial

def send_packet(root):
    dst ='192.168.1.39'
    src = None
    dport = 22
    sport = 22
    data = ''
    slaves = root.pack_slaves()
    try:
        dst, dport = slaves[1].get().split(':')
        dport = int(dport)
    except:
        slaves[-1].config(text = 'Error parse dest')
    try:
        src, sport = slaves[3].get().split(':')
        sport = int(sport)
    except:
        slaves[-1].config(text = 'Error parse src')
    data = slaves[5].get()
    p=IP(dst=dst, src = src)/UDP(dport=dport, sport = sport)/data
    try:
        sendp(p)
    except:
        slaves[-1].config(text = 'Error sending') 

root = Tk()
root.title('UDP Generator')
root.geometry('140x160')
Label(root, text = 'Destination IP:port').pack(side = TOP, anchor = W)
dest_entr = Entry(root)
dest_entr.pack(side = TOP, anchor = W)
Label(root, text = 'Source IP:port').pack(side = TOP, anchor = W)
src_entr = Entry(root)
src_entr.pack(side = TOP, anchor = W)
Label(root, text = 'Data').pack(side = TOP, anchor = W)
data_entr = Entry(root)
data_entr.pack(side = TOP, anchor = W)
Button( root, text='Send', command=partial(send_packet, root) ).pack( side = TOP, anchor = W)
Label(root, text = '').pack(side = RIGHT, anchor = W)
root.mainloop()
