#Student: John Larson
#CMSC 441 -- Project 2 part b
#
# This code will generate two factors of an input modulus.  Directions for  
# use are provided directly above main.
# This code is intended for use with python 3.

import random
import time
	
def pollardpm1(n,a):
	foundFactor = False
	i = 2
	#loop until we get a hit
	while not foundFactor:
		#for this p-1 we are using an factorial exponent, by memoizing the
		#last value, we can just multiply i+1 instead of doing the factorial
		#each time
		newValue = pow(a,i,n)
		a = newValue
		i+=1
		GCD = gcd(newValue-1,n)
		#if GCD isn't 1, we have a winner
		if GCD != 1:
			foundFactor = True
			factor2 = n//GCD
			print("P - 1 Factors are: ",GCD," ",factor2)

			
def pollardRho(n):

	i = 1
	x1 = random.randint(0,n-1)
	k = 2
	y = x1
	d = 1
	#loop until we get a GCD !=1
	while d == 1:
		i+=1
		#using x^2 + 1 instead of x^2 - 1
		x1 = (x1**2 + 1) % n
		d = gcd(y - x1, n)
		#as long as the factor isnt 1 or itself we have a new factor
		if d != 1 and d!= n:
			factor2 = n//d
			print("PolRho Factors are: ",d," ",factor2)
			return d
		#increasing y for each multiple of 2
		if i == k:
			y = x1
			k = 2*k
	#this shouldn't occur, but safety is fun
	print("Failure")
	return
	
#based off pseudocode from http://maths-people.anu.edu.au/~brent/pd/rpb051i.pdf
def brent(n):
	#initializing variables
	y=random.randint(1, n-1)
	c=random.randint(1, n-1)
	m=random.randint(1, n-1)
	G=1
	r=1
	q=1
	#while GCDs are 1, we keep looping
	while G<=1:             
		x = y
		#starting at a small loop, but getting larger
		for i in range(1,r):
			#for some reason (pow(y,2,n)+c)%n is MUCH slower, likely due to
			#overhead or more complicated c code for a y^2
			y = ((y*y)%n+c)%n
		k = 0
		#if our k gets too big or we get a G greater than 1 we exit
		#a k>=r results in increasing r and looping again
		while not(k>=r or G>1):
			ys = y
			for i in range(min(m,r-k)):
				y = ((y*y)%n+c)%n
				q = q*(abs(x-y))%n
			G = gcd(q,n)
			k += m
		r *= 2
	#getting here means we have found a GCD higher than 1 if it's 
	#our modulus we have more work to do
	if G==n:
		while not G>1:
			ys = ((y*y)%n+c)%n
			G = gcd(abs(x-ys),n)

	factor2 = n//G
	print("Brent Factors are: ",G," ",factor2)
	return G  
	
#This code is simply the python library implementation of gcd(), for some
#reason I was getting errors when including it, so I just copied/pasted
def gcd(a, b):

    while b:
        a, b = b, a%b
    return a

# In order to use this code, simply input a desired modulus and make sure the
# factoring function you would like to use is commented in.  The time will
# also be displayed if the surrounding t1 and t2 are not commented out.
def main():
	#below input the desired modulus
	modulus = 545
	print("modulus:", modulus)
	
	#choose a factoring algorithm
	t1 = time.clock()
	pollardpm1(modulus,2)
	t2 = time.clock() - t1
	print(t2)

	t1 = time.clock()
	pollardRho(modulus)
	t2 = time.clock() - t1
	print(t2)

	t1 = time.clock()
	brent(modulus)
	t2 = time.clock() - t1
	print(t2)
	
main()