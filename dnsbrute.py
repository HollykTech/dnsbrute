#!/usr/bin/python3
'''
Brute Force DNS - Domain Name Server
- 1kTech
'''
import dns.resolver, time, subprocess, os, sys
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
		print("Brute Force DNS - Domain Name Server\n- 1kTech\n")
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
