from sys import argv
import numpy as np
import time
from fim import *
import os
support=[1,2,10,20,30,40,50,70,80]#support values to build dataset
final_class=[]
dlm=','
text_file = open("./final/final_dataset.txt", "w")
for file in os.listdir("E:/dm/dataset/new"):
    if file.endswith(".txt"):
        print("%s" % file)
        data = open(file, 'r')
        tracts = [[int(n) for n in line.split()] for line in data]
        ht=len(tracts)#height
        maxw=len(tracts[0])
        minw=len(tracts[0])
        wid=len(tracts[0])
        uni=[]
        for r in tracts:
        	for a in r:
        		uni.append(a)#all bought items
        	if(len(r)>=maxw):
        		maxw=len(r)#maxwidth
        	if(len(r)<=minw):
        		minw=len(r)#minwidth
        	wid=wid+len(r)
        wid=wid/ht#width
        mass=len(uni)#mass
        uni=np.array(uni)
        uni=np.unique(uni)
        span=len(uni)#span
        

        for i in support:
            start= time.process_time()
            for j in range(1,20):
                apriori(tracts, supp=i)
            end=time.process_time()
            ta=(end-start)/20
            start= time.process_time()
            for j in range(1,20):
                fpgrowth(tracts, supp=i)
            end=time.process_time()
            tf=(end-start)/20
            start= time.process_time()
            for j in range(1,20):
                eclat(tracts, supp=i)
            end=time.process_time()
            te=(end-start)/20
            tm=min(ta,te,tf)
            if(tm==ta):
            	best = '1,0,0'
            elif(tm==tf):
            	best = '0,1,0'
            elif(tm==te):
            	best = '0,0,1'
            s =''
            s += str(maxw)+dlm+str(minw)+dlm+str(ht)+dlm+str(wid)+dlm+str(mass)+dlm+str(span)+dlm+str(i)+dlm+best
            s+='\n'
            text_file.write("%s" % s)
text_file.close() 

##########################################################################################
#			final dataset is the target class value in order of dataset
#			[1,0,0] is apriori
#			[0,1,0] is fpgrowth
#			[0,0,1] is eclat