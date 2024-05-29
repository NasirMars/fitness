import datetime
start_day = "2024-5-14"
start_distance = 6.5
cycle = 2
increasing_rate = 0.03
total_time = 54
day_array = []
distance_array = []
increasing_array = []

def time(start_day, cycle):
    date_obj=datetime.datetime.strptime(start_day, "%Y-%m-%d").date()
    plan_date=date_obj+datetime.timedelta(days=cycle)
    return(plan_date)

def distance(accumulate_distance, increasing_rate):
    increasing_distance = accumulate_distance*increasing_rate
    accumulate_distance = accumulate_distance+increasing_distance
    return(accumulate_distance, increasing_distance)



if __name__ == '__main__':
    numbers_of_cycle=int(total_time / cycle)
    accumulate_distance = start_distance
    day_array.append(start_day)
    distance_array.append(start_distance)
    increasing_array.append(0)

    for x in range(numbers_of_cycle):
        plan_date = time(start_day, (x+1)*cycle)
        day_array.append(plan_date.strftime('%Y-%m-%d'))
    for y in range(numbers_of_cycle):
        accumulate_distance, increasing_distance = distance(accumulate_distance, increasing_rate)
        distance_array.append(accumulate_distance)
        increasing_array.append(increasing_distance)
    for z in range(numbers_of_cycle+1):
        print("plan date:"+day_array[z]+"  plan distance:"+f"{distance_array[z]:.2f}"+"miles  increasing distance:"+f"{increasing_array[z]:.2f}"+"miles")
