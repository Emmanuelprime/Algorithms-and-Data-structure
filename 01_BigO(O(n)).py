"""This code demonstrates that time of executionis not a good factor for considering good or bad code since
diffrent systems execute at different times.

    The code also shows that increasing the number of inputs(O(n)) in this case,(items in array) probably changes thetime of 
    execution."""
"""In summary,the number of operations(no of times in the loop) is proportional to the number of inputs(n)"""
import time

array = ['nemo']

array2 = ['ray','ada','tim','josh','nemo']

def findNemo(array):
    t0 = time.time() # gets the time stamp it enters the function
    for i in range(len(array)):
        if array[i] =='nemo':
            print('found nemo!')
    t1 = time.time() # gets the time stamp it finished execution
    print("it took",str((t1-t0)*1000)+"sec") 

findNemo(array=array2)

"""Therefore this code has a BIG O notation of O(n) or Linear time"""
