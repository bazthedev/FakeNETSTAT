import os
import msvcrt
from time import sleep
import random
from platform import node

codes = ["ESTABLISHED", "TIME_WAIT", "SYN_SENT", "ESTABLISHED", "CLOSE_WAIT", "ESTABLISHED"]

ver = 1.0
big = random.randint(200, 300)

def cls():
  os.system("cls")
print("Please insert the Disk Labelled Microsoft Windows 10 Networking Disk #4 into Drive A: and press any key to continue...")
msvcrt.getch()
print("\n")
print("Active Connections")
print("  Proto   Local Address   Foreign Address   State")
for i in range(1, big):
  print("  " + "TCP" + "  " + f"127.0.0.1:{random.randint(10000, 80000)}" + "  " + f"{node()}:{random.randint(10000, 80000)}" + "  " + f"{random.choice(codes)}")
  sleep(random.uniform(0.01, 0.1))
sleep(2)
print("")
print("Press any key to terminate all foreign connections...")
msvcrt.getch()
print("")
print("Terminating...")
sleep(0.5)
print("")
print("Foreign Address" + "   " + "State")
print("")
for i in range(1, big):
  print(f"{node()}:{random.randint(10000, 80000)}" + "    " +  "TERMINATED")
  sleep(random.uniform(0.01, 0.1))

sleep(2)
print("")
print("Successfully terminated {} connections to foreign addresses, any malicious addresses (hackers) would have been terminated.".format(big))
