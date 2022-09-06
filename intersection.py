"""
IMC
- If in the previous second, no car passed through the intersection, then the first car in the queue for 1st Avenue goes first. 
- If in the previous second, a car passed through the intersection on 1st Avenue, then the first car in the queue for 1 st Avenue goes first. 
- If in the previous second, a car passed through the intersection on Main Street, then the first car in the queue for Main Street goes first. 
Passing through the intersection takes 1 second. For each car, find the time when they will pass through the inter‍‍‌‍‍‌‌‍‍‌‌‍‌‍‌‌‌‌‌section. 
"""
from time import time


def getResult(arrival, street):
    main_street = []
    first_ave = []
    n = len(arrival)
    # time_car = []
    res = [None] * n 
    flag = -1
    cur_time = 0
    # pre_time = -1
    
    for i in range(len(arrival)):
        if street[i] == 0:
            main_street.append((arrival[i], i))
        else:
            first_ave.append((arrival[i], i))
            
    while main_street or first_ave:
        temp = (float("inf"), float("inf"))
        temp2 = (float("inf"), float("inf"))
        if main_street: 
            temp = main_street[0] 
            
        if first_ave:
            temp2 = first_ave[0]
            
        if cur_time < temp[0] and cur_time < temp2[0]:
            cur_time = min(temp[0], temp2[0])
        # print(cur_time)
        # print(temp[0])
        # print(temp2[0])
        # print("#####")
        # main: temp   first: temp2
          
        if temp[0] < temp2[0]:
            while main_street:
                if main_street[0][0] > cur_time:
                    break
                a = main_street.pop(0)
                res[a[1]] = cur_time
                
                # pre_time = cur_time
                cur_time += 1
        else:
            while first_ave:
                if first_ave[0][0] > cur_time:
                    break
                a = first_ave.pop(0)
                res[a[1]] = cur_time
                
                # pre_time = cur_time
                cur_time += 1
                
    return res
    
    # 2s   3s
    #  1   0, 1       
            
    #  0    
               
               
        
        
        
    return res
"""
arrive[n]: an array of n integers the value at index i is the time in seconds when the ith car arrives at the inersections. 
if arrive[i] = arrive[j] and i < j, then car i arrives before car j.

street[n]: an array of n integers where the value  at index i is the steet on which the ith car is travling: 0 for main stree and 1 for 1st street

return: an array of n integers where the value at index i is the time when the i th car will pass through the intersection.
""" 
    
arrival = [0,0,1,4]
street = [0,1,1,0]

arrival2 = [0,1,1,3,3]
street2 = [0,1,0,0,1]

arrival3 = [0,0,1,4,5]
street3 = [0,1,1,0,1]

print(getResult(arrival, street))  #2014
print(getResult(arrival2, street2)) # 02143
print(getResult(arrival3, street3)) 
