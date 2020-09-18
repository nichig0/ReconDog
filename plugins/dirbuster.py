import sys
import json
import os
import requests


def dirbuster(inp):
	arr=[]
	url=inp
	wordlist="/libs/wordlist.txt"
	try:
		if url[:7] != 'http://':
			url="http://"+url
		r=requests.get(url)
		if r.status_code == 200:
			print('Host is up.')
		else:
			print('Host is down.')
			return
		if os.path.exists(os.getcwd() + wordlist):
			fs=open(os.getcwd()+wordlist,"r")
			for i in fs:
				scanned_path = (url + "/" + i).replace("\n", "")
				rq=requests.get(url+"/"+i)
				if rq.status_code == 200:
					print(f"{scanned_path} -- 200 OK")
					arr.append(str(url+"/"+i))
				else:
					print(f"{scanned_path} -- 404 Not Found")
			fs.close()
			print("output".center(100,'-'))
			l=1
			for i in arr:
				print(l, "> ", i)
				l+=1
		else:
			print(wordlist + " don't exists in the directory.")
	except Exception as e:
		print(e)

