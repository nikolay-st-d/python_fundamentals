from math import floor

exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

time_of_exam = exam_hour * 60 + exam_minutes
time_of_arrival = arrival_hour * 60 + arrival_minutes

if time_of_arrival > time_of_exam:
    print('Late')
elif 0 <= time_of_exam - time_of_arrival <= 30:
    print('On time')
elif time_of_exam - time_of_arrival > 30:
    print('Early')

if abs(time_of_exam - time_of_arrival) != 0:
    if 0 <= (time_of_exam - time_of_arrival) < 60:
        print(f"{time_of_exam - time_of_arrival} minutes before the start")
    elif time_of_exam - time_of_arrival >= 60:
        hours = floor((time_of_exam - time_of_arrival) / 60)
        minutes = (time_of_exam - time_of_arrival) % 60
        if 0 <= minutes < 10:
            print(f"{hours}:0{minutes} hours before the start")
        else:
            print(f"{hours}:{minutes} hours before the start")
    elif 0 <= time_of_arrival - time_of_exam < 60:
        print(f"{time_of_arrival - time_of_exam} minutes after the start")
    elif time_of_arrival - time_of_exam >= 60:
        hours = floor((time_of_arrival - time_of_exam) / 60)
        minutes = (time_of_arrival - time_of_exam) % 60
        if minutes < 10:
            print(f"{hours}:0{minutes} hours after the start")
        else:
            print(f"{hours}:{minutes} hours after the start")
