from random import *
import os
#import numpy as np
for j in range(1,251):
	data=[]
	print(j)
	ltr=randint(10,19)
	smtr=randint(1,8)
	mintr=randint(75,1200)
	maxtr=randint(2000,25000)
	sfe=randint(22,30)
	lfe=randint(35,75)
	feat=randrange(sfe,lfe,1)
	row=randrange(mintr,maxtr,1)
	text_file = open("dataset_{0:03d}.txt".format(j), "w")
	for i in range(1,row):
		tran=randint(smtr,ltr)+1
		s =''
		data=sample(range(1,feat),tran)
		for k in range(1,tran):
			s += str(randrange(1,feat,1)) + ' '
		s+='\n'
		text_file.write("%s" % s)
	
	text_file.close() 
