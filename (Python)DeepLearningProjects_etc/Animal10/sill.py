import datetime
import time
t1 = datetime.datetime.now()
time.sleep(1)
t3 = datetime.datetime.now()
print("------->",(t3-t1).seconds)
print("furkan",end=" -> ")
print("tanteri")
# for i in range(20):
#     print(i)
# t2 = datetime.datetime.now()
# print("\n-----------------\n",(t2 - t1).microseconds)