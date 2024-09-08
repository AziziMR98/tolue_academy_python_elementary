import time

t = int(input("Enter time : "))

for i in range(1, t * 60):
    print(i)
    time.sleep(1)