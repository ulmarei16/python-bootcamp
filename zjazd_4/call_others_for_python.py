import os

# x=os.system("dir")   #<-- jaki program ma uruchomic /#<-- po uruchomieniu tego program python sie zatrzymuje, az czlowiek nie zamknie tego uruchomionego programu
# y=os.system("ping www.wp.pl")
# # print(x)
# print(y)

# z = os.popen("ipconfig").decode()
# print(z)

import subprocess
p = subprocess.call("notepad.exe")
p2 = subprocess.Popen("notepad.exe") #<-- to uruchamia program i można robić coś innego jak on jest otwarty
print("zzzzzz")