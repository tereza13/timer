import time

def second_countdown(h, m, s):
    for i in range(s-1, -1, -1):
        print(f"{h}:{m}:{i}")
        time.sleep(1)

def my_timer(hour, minute, second):
    print(f"Starting count down \n{hour}:{minute}:{second}")
    time.sleep(1)
    second_countdown(hour,minute, second)
    if(minute>0):
        while(minute>0):
            minute-=1
            second=60
            second_countdown(hour,minute,second)
    if(hour>0 and minute==0):
        while(hour>0):
            hour-=1
            minute+=60
            while(minute>0):
                minute-=1
                second=60
                second_countdown(hour,minute,second) 

#Gettin user input
timer_input = input("Insert time to count down (h:m:s) ")

#Splitting the input into hours, minutes and seconds
timer_components = timer_input.split(':')
hours = int(timer_components[0])
minutes = int(timer_components[1])
seconds = int(timer_components[2])

#Checking format correctness
if(hours >= 24 or minutes >= 60 or seconds >= 60):
    print("Please insert valid time")
else:
    my_timer(hours, minutes, seconds)

print("Countdown is over")