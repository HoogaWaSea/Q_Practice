import re


def getResult(arrival, street):
    main_street = []
    first_ave = []
    time_car = []
    res = []
    
    for i in range(len(arrival)):
        time_car.append((arrival[i], i))
        cur_time, pre_car = 0, -1
        
        while len(time_car) != 0 or len(main_street) != 0 or len(first_ave) != 0:
            if len(time_car) == 0 and len(main_street) == 0:
                if time_car.pop(-1)[0] != cur_time:
                    pre_car = -1
                    cur_time = time_car.pop(-1)[0]
                
                while len(time_car) != 0 and time_car.pop(-1) == cur_time:
                        cur_time_car = time_car.pop(0)
                        
                        if street[cur_time_car[1]] == 0:
                            main_street.append(cur_time_car)
                        elif street[cur_time_car[1]] == 1:
                            first_ave.append(cur_time_car)
                            
                if pre_car == -1 or pre_car == 1 or len(main_street) == 0 and len(first_ave) != 0:
                    cur_first_avenue = []
                    cur_first_avenue.append(first_ave.pop(0))
                    res[cur_first_avenue[1]] = (cur_time+=1)
                    pre_car = 1
                    
                elif pre_car == 0 or len(main_street) == 0 and len(first_ave) == 0:
                    cur_main_street = []
                    cur_main_street.append(main_street.pop(0))
                    res[cur_main_street[1]] = (cur_time+=1)
                    pre_car = 0
                    

    return res
    
arrival = [0,0,1,4]
street = [0,1,1,0]

dgetResult(arrival, street)
