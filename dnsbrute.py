import dns.resolver
import time

def progress_bar(done):
	print("Carregando: [{0:50s}] {1:.1f}$".format('~' * int(done*50), done*100))

for n in range(101):
	progress_bar(n/100)
	time.sleep(1-n)

try:
	Rs=dns.resolver.query('bancocn.com', 'A')
	for R in Rs:
		print("bancocn.com", R)
except Exception as erro:
	print(erro)
