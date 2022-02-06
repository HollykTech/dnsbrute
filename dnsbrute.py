import dns.resolver

try:
	Rs=dns.resolver.query('bancocn.com', 'A')
	for R in Rs:
		print("bancocn.com", R)
except Exception as erro:
	print(erro)
