import re
import time
from urllib.request import urlopen
import time
import colorama
from colorama import init,Fore,Back,Style

ids = [["互娱", 2555, 21.325], ["完美", 2624, 15.912]]
init(autoreset=True)
red_color = '\033[1;31m'
green_color = '\033[1;32m'

while 1:
    try:
        hour = time.localtime().tm_hour
        min = time.localtime().tm_min
        wday = time.localtime().tm_wday
        for id in ids:
            if (hour == 9 and min >= 30 and min <= 59) or (hour == 10) or (hour == 11 and min >= 0 and min <= 30) or ( hour >= 13 and hour < 15):
                url1 = 'http://qt.gtimg.cn/q=sz%06d' % id[1]
                #print(now)
                myURL1 = urlopen(url1)
                content1 = myURL1.read().decode('GBK')
                row1 = re.findall('^v_(sh|sz)\d{6}\="(.*)";',content1)
                if len(row1) == 1:
                    cols = row1[0][1].split('~')
                    if float(cols[3]) > (id[2]) :
                        print(red_color + cols[1], red_color + ":", red_color + cols[3], end=" ---- ")
                    else:
                        print(green_color + cols[1],green_color + ":",green_color + cols[3], end=" ---- ")
            else:
                print("停止", end=" ---- ")
        print("")
        time.sleep(5)
    except:
        print("except")
        time.sleep(5)