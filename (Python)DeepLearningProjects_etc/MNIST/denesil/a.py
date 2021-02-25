# import sys
# dropout=float(sys.argv[1])
# #print('a= ',dropout*10)
import os
dropout=0.10
os.system('cls')

while dropout<1:
    komut="python mnist_graph.py "+str(dropout)
    os.system(komut)
    dropout+=0.025
    temp="{:.3f}".format(dropout)
    dropout=float(temp)
