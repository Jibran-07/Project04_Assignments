import time

def countdown(t):
    while t > 0:
        mins = t // 60
        secs = t % 60
        print(f"{mins} min {secs} sec")
        time.sleep(1)
        t = t - 1
    print("Time's up!")


try:
    t = int(input("Enter time in seconds: "))
    if t > 0:
        countdown(t)
    else:
        print("Enter a number greater than 0.")
except:
    print("Please enter a valid number.")