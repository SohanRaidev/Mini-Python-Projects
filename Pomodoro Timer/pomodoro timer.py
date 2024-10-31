import time

def pomodoro_timer(work_duration, break_duration, cycles):
    for i in range(cycles):
        print(f"Cycle {i + 1}/{cycles}: Work for {work_duration} minutes.")
        time.sleep(work_duration * 60)  
        print("Time for a break!")
        time.sleep(break_duration * 60) 
        print("Break is over! Let's get back to work.")


work_duration = int(input("Enter work duration in minutes: "))
break_duration = int(input("Enter break duration in minutes: "))
cycles = int(input("Enter number of cycles: "))

pomodoro_timer(work_duration, break_duration, cycles)
