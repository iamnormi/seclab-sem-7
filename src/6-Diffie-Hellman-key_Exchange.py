#Diffie-Hellman Key Exchange
from random import randint

if __name__ == '__main__':

	# Both the persons will be agreed upon the
	# public keys G and P
	# A prime number P is taken
	#P = 23
	P = int(input("Enter a Prime Number..: "))

	# A primitive root for P, G is taken
	#G = 9
	G = int(input("Enter a Primitive root..: "))


	#print('The Value of P is :%d'%(P))
	#print('The Value of G is :%d'%(G))

	# Alice will choose the private key a
	#a = 4
	a = int(input("The Private Key a for Alice is.. : "))
	#print('The Private Key a for Alice is :%d'%(a))

	# gets the generated key
	x = int(pow(G,a,P))

	# Bob will choose the private key b
	#b = 3
	#print('The Private Key b for Bob is :%d'%(b))
	b = int(input("The Private Key b for Bob is..: "))
	# gets the generated key
	y = int(pow(G,b,P))


	# Secret key for Alice
	ka = int(pow(y,a,P))

	# Secret key for Bob
	kb = int(pow(x,b,P))

	print('Secret key for the Alice is : %d'%(ka))
	print('Secret Key for the Bob is : %d'%(kb))
