def getResult(arrival, street):
    # initialize num_cars
    prev = -1 # -1 if there is no car in the previous time, 0 means previous second, a car passed through main st, 1 means a car passed through 1st avenue
    # initialize an array [answer] of length num_cars
    time = 0 # the clock time
    # maintain a queue of car index, arrival time tuples for Main Street and 1st Avenue
    # mainStreetQueue
    # firstAveQueue
    for every car number, arrival time, and arrival street:
        add (car number, arrival time) to the queue corresponding to arrival street.
def pass_car_through_intersection(arrival_street, car_idx, passing_time):
    """
    "Passes" [car_idx] through the intersection, i.e., pop it from the queue that
    corresponds to [arrival_street] and update [answer] with [passing_time].
    """
    answer[car_idx] = passing_time
    arrival_street.popleft()
    while either queue is non-empty:
        # peek mainStreetQueue if the queue is nonempty else (null infinity)
        # peek firstAveQueue if the queue is nonempty else (null, infinity)
        # if one car arrives earlier than the other:
        # let xCar, xTime denote the car number and arrival time of the car that arrives earlier.
        # if xTime is less than time: # example: arrivals = [0,0,1,4], streets = [0,1,1,0]
 set xTime to time (mutate the queue)
 skip this iteration of the while loop
time = max(xTime, time)
set answer[xCar] <- time
pop xCar from the corresponding queue
set prev = 0 or 1 depending on which queue xCar came from
time <- time + 1
else if they arrive at the same time:
let xMain, xFirst denote the main an‍‍‌‍‍‌‌‍‍‌‌‍‌‍‌‌‌‌‌d first cars and xTime denote the arrival time.
if xTime > time:
 prev = -1 # if the current time is behind the next arrival time, then we can "travel ahead" in time.
if xTime < time:
set xTime to time for both cars xMain and xFirst
skip this iteration of the while loop
time = max(main_time, time)
if prev was -1 or 1:
answer[xFirst] <- time
pop xFirst from the corresponding queue
prev = 1
 time <- time + 1
elif prev == 0: # previous second, a car passed through main street
# do the same as above, except for xMain.
    return answer