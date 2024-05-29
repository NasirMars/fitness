import datetime
import matplotlib.pyplot as plt

start_day="2024-05-14"
start_distance=6.5
increasing_rate=0.03
current_training=8
total_time=52

display_day=0
rest_day=1
recovery_day=0
cycle = 0
c = 0
r = 0

language='English'
unit='miles'

start_day_chart = start_day[5:]
day_array = []
training_time_array = []
distance_array = []
increasing_array = []
accumulate_array = []

all_day_array = []

day_chart_array = []
distance_chart_array = []

def time(start_day, cycle):
    date_obj=datetime.datetime.strptime(start_day, "%Y-%m-%d").date()
    plan_date=date_obj+datetime.timedelta(days=cycle)
    return(plan_date)

if __name__ == '__main__':
    distance=start_distance
    distance_array.append(distance)
    distance_chart_array.append(distance)
    accumulate_array.append(distance)
    increasing_array.append(0)

    for x in range(total_time):
        plan_date=time(start_day, x)
        all_day_array.append(plan_date.strftime('%Y-%m-%d'))


    while display_day < total_time:
        cycle += 1
        plan_date=time(start_day, display_day)
        day_array.append(plan_date.strftime('%Y-%m-%d'))
        day_chart_array.append(plan_date.strftime('%Y-%m-%d'))
        if distance > 8:
            cycle += 1
            increasing_rate=0.051
            recovery_day = 1
            plan_date=time(start_day, display_day+1)
            day_array.append(plan_date.strftime('%Y-%m-%d'))
            increasing_array.append(0)
            distance_array.append(3)
        display_day=display_day+rest_day+recovery_day+1
        rest_day = int((distance-1) // 7+1)
        increased_distance = round(distance * increasing_rate, 2)
        increasing_array.append(increased_distance)
        distance = distance + increased_distance
        distance_chart_array.append(round(distance, 2))
        accumulate_array.append(round(distance+accumulate_array[-1], 2))
        distance_array.append(round(distance, 2))
    accumulate_array.pop()
    distance_chart_array.pop()
    for p in range(cycle):
        if distance_array[p] != 3:
            print("plan date:"+day_array[
                p]+"  compound training "+str(c+1)+"  plan distance:"+f"{distance_array[p]:.2f}"+" miles  increasing distance:"+f"{increasing_array[p]:.2f}"+" miles  accumulate distance:"+f"{accumulate_array[c]:.2f}"+" miles")
            c += 1
        else:
            print("plan date:"+day_array[
                p]+"  recovery training "+str(r+1)+"  plan distance:"+f"{distance_array[p]:.2f}"+" miles")
            r += 1
    # print(day_chart_array)
    # print(accumulate_array)
    # print(distance_chart_array)
    print(all_day_array)

    plt.figure(figsize=(10, 6))
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.plot(day_chart_array, distance_chart_array)
    # plt.plot(training_time_array, distance_array)
    # print(training_time_array)
    plt.xlabel("time")
    plt.ylabel("distance")
    plt.title("COMPOUND TRANING CHART")
    plt.show()

