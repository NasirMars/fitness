#CODER/コーダー:Mars/マーズ

import datetime
import matplotlib.pyplot as plt

start_day = "2024-05-14"   #いつ計画を開始したいですか? (xxxx-xx-xx) /When do you want to start your plan?
start_distance = 6.5   #どのくらいの距離からトレーニングを始めたいですか? /What distance you want to begin traning?
cycle = 2  #各実行には何日かかりますか? /How many days for each run?
increasing_rate = 0.03  #実行するたびにどのくらいの速度を上げたいですか? /What rate you want to incresing after each run?
total_time = 54  #何日間のトレーニングを予定していますか? /How many day you plan for traning ?
language = 'English' #日本語/English
unit = 'miles'  #キロ/マイル/km/miles、

start_day_chart = start_day[5:]
day_array = []
training_time_array = []
day_chart_array = []
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

def display(language, unit, times):
    if language=='English' or language=='english':
        if unit=='miles' or unit=='mile':
            print("plan date:"+day_array[
                z]+"  compound training "+times+"  plan distance:"+f"{distance_array[z]:.2f}"+"miles  increasing distance:"+f"{increasing_array[z]:.2f}"+"miles")
        elif unit=='km':
            print("plan date:"+day_array[
                z]+"  compound training "+times+"  plan distance:"+f"{distance_array[z]:.2f}"+"km  increasing distance:"+f"{increasing_array[z]:.2f}"+"km")
    elif language=='日本語' or language=='Japanese' or language=="japanese":
        if unit=='miles' or unit=='mile' or unit=='マイル':
            print("計画日:"+day_array[
                z]+"  compound training "+times+"  計画走行距離:"+f"{distance_array[z]:.2f}"+"マイル  増加した距離::"+f"{increasing_array[z]:.2f}"+"マイル")
        elif unit=='km' or unit=='キロ':
            print("計画日:"+day_array[
                z]+"  compound training "+times+"  計画走行距離:"+f"{distance_array[z]:.2f}"+"キロ  増加した距離::"+f"{increasing_array[z]:.2f}"+"キロ")



if __name__ == '__main__':
    numbers_of_cycle=int(total_time / cycle)
    accumulate_distance = start_distance
    day_array.append(start_day)
    day_chart_array.append(start_day_chart)
    distance_array.append(start_distance)
    increasing_array.append(0)

    for x in range(numbers_of_cycle):
        plan_date = time(start_day, (x+1)*cycle)
        day_array.append(plan_date.strftime('%Y-%m-%d'))
        day_chart_array.append(plan_date.strftime('%m-%d'))
    for y in range(numbers_of_cycle):
        accumulate_distance, increasing_distance = distance(accumulate_distance, increasing_rate)
        distance_array.append(accumulate_distance)
        increasing_array.append(increasing_distance)
    if language == 'English' or language == 'english':
        print("Here is the compound training plan generated for you.")
    elif language == '日本語' or language == 'Japanese' or language == "japanese":
        print("こちらがあなたのために生成されたcompound traningプランです。")
    for z in range(numbers_of_cycle+1):
        training_time_array.append(z+1)
        display(language, unit, times=str(z+1))

    # plt.plot(day_chart_array, distance_array)
    plt.plot(training_time_array, distance_array)
    # print(training_time_array)
    plt.xlabel("time")
    plt.ylabel("distance")
    plt.title("COMPOUND TRANING CHART")
    plt.show()

