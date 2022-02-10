<<<<<<< HEAD
import dns.resolver

try:
	Rs=dns.resolver.query('bancocn.com', 'A')
	for R in Rs:
		print("bancocn.com", R)
except Exception as erro:
	print(erro)
=======
#!/usr/bin/python3

'''
            dnsbrute.py

         .-.         .-.
        (.`-'--< >--'-´.)
   __    \`           ´/    __
 .'._'-.__)'         '(__.-'_.'.
'(´  ``'--´           `--'´´  `)'
 `._     .             .     _.´
    ``''´               `''´´

             1kTech
'''

import dns.resolver, time, subprocess, os, tqdm, sys

def main():
	load()
	try:
		global domain
		domain=sys.argv[1]
		namearq=sys.argv[2]
	except:
		print("U can use too: dnsbrute <domain> [wordlist]\n")
		scriptauto()
	try:
		arq=open(namearq)
		global domainsub
		domainsub=arq.read().splitlines()
	except:
		print("Archive not found.")
		sys.exit(1)
	try:
		brute()
	except Exception as erro:
		print("Error:", erro)

def load():
	try:
		#fsize=os.path.getsize(r"dnsbrute.py")
		print("\n           dnsbrute.py")
		print("         .-.         .-.")
		print("        (.`-'--< >--'-´.)")
		print("   __    \`           ´/    __")
		print(" .'._'-.__)'         '(__.-'_.'.")
		print("'(´  ``'--´           `--'´´  `)'")
		print(" `._     .             .     _.´")
		print("    ``''´               `''´´")
		print("             1kTech\n")
		#for i in tqdm.tqdm(range(fsize)):
		#	time.sleep(0.0005)
	except Exception as error:
		print("Error:",error)

def scriptauto():
	global domain
	global domainsub
	domain=input("Set domain: ")
	wordlist=input("Set wordlist: ")
	try:
		arq=open(wordlist)
		domainsub=arq.read().splitlines()
	except:
		print("Archive not found.")
		sys.exit(1)
	try:
		brute()
	except Exception as erro:
		print("Error:", erro)

def brute():
	global domainsub
	print("Loading results\n---")
	for i in domainsub:
		domainsub=i+"."+domain
		try:
			Rs=dns.resolver.query(domainsub,"a")
			for R in Rs:
				print("Domain:",domainsub,"ip:",R)
		except:
			pass
	print("---")
	sys.exit(1)
main()
>>>>>>> 149e1cb (dnsbrute.py 1.0)
