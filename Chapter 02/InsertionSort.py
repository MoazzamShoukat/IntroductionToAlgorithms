#!/usr/bin/env python
# coding: utf-8
# @moazzamshoukat


#Implementaion of Insertion Sort

#Defining a function
def insertionSort(a):
    
    #Traverse through a[1] to a[n]
    for j in (range(1, len(a))):
        
        #Storing & Setting up a key value for comparison
        key = a[j]
        i = j-1
        
        #Comparing the key value untill teh conditons meet
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i-1
        #Strori the key value at index
        a[i+1] = key
        
#Array
a = [2,3,4,6,7,9,11,3, 12, 11, 13,41,5, 6]

#Function Call
insertionSort(a)

#Sorted Array
for i in a:
    print (i)


# In[ ]:




