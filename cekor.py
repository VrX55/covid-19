import os,time
try:
	import requests
except:
	os.system('pip intsall requests')
	
ck = requests.Session()

def menu():
	os.system('clear')
	print('''
	\t[ COVID-19 Case Data ]
	[+] Author    : Vrx
	[+] Instagram : fajarid05_
	[+] Source Api: 'https://api.kawalcorona.com' ''')
	print('-'*55)
	banner()
def banner():
	print('''
	              [ Command ]
	[!] Prov : Melihat seluruh data di Provinsi
	[!] Indo : Melihat seluruh data di Indonesia
	[!] World: Melihat seluruh data di Dunia
	[!] Exit : Untuk Keluar
	''')
	print('')
	pilih = input('[?]command/> ')
	if pilih == 'Indo' or pilih == 'indo':
		indonesia()
	elif pilih == 'prov' or pilih == 'Prov':
		provinsi()
	elif pilih == 'world' or pilih == 'World':
		world()
	elif pilih == 'exit' or pilih == 'Exit':
		print('bye.....')
		time.sleep(2)
		exit()
	else:
		print()
		banner()
def indonesia():
	indonesia = ck.get('https://api.kawalcorona.com/indonesia')
	data = indonesia.json()
	negara = data[0]['name']
	positif = data[0]['positif']
	sembuh = data[0]['sembuh']
	mati = data[0]['meninggal']
	print('')
	print('[ Data Terkini Di Indonesia ]')
	print('-'*30)
	print()
	print('[*] Negara    : ',negara)
	print('[*] Positif   : '+ str(positif) + ' orang')
	print('[*] Sembuh    : '+ str(sembuh) + ' orang')
	print('[*] Meninggal : '+ str(mati) + ' orang')
	print('')
	input('[back]')
	menu()
def provinsi():
	url_prov = ck.get('https://api.kawalcorona.com/indonesia/provinsi')
	data_prov = url_prov.json()
	print()
	print('[ Data Di Setiap Provinsi Di Indonesia ]')
	print('-'*40)
	print('')
	for x in data_prov:
		nama_prov = (x['attributes']['Provinsi'])
		positif = (x['attributes']['Kasus_Posi'])
		sembuh = (x['attributes']['Kasus_Semb'])
		mati = (x['attributes']['Kasus_Meni'])
		print('[*] Provinsi  :',nama_prov)
		print('[*] Positif   : '+ str(positif) + ' orang')
		print('[*] Sembuh    : '+ str(sembuh) + ' orang')
		print('[*] Meninggal : ' + str(mati) + ' orang')
		print()
	print('[*] Total Provinsi :',len(data_prov))
	print()
	input('[back]')
	menu()
def world():
	positif = ck.get('https://api.kawalcorona.com/positif').json()
	sembuh = ck.get('https://api.kawalcorona.com/sembuh').json()
	mati = ck.get('https://api.kawalcorona.com/meninggal').json()
	ttl_positif = positif['value']
	ttl_sembuh = sembuh['value']
	ttl_mati = mati['value']
	print('')
	print('[ Data Kasus COVID-19 Di Seluruh Dunia ]')
	print('-'*30)
	print('[*] Total Positif   : '+ str(ttl_positif) + ' orang')
	print('[*] Total Sembuh    : '+ str(ttl_sembuh) + ' orang')
	print('[*] Total Meninggal : '+ str(ttl_mati) + ' orang')
	print()
	input('[back]')
	menu()

menu()
	