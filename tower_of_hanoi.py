def move(f,t):
    print("move disc from {} to {}!!!".format(f,t))

def hanoi(n,f,h,t):
    if n == 0:
        pass
    else:
        hanoi(n-1, f, t, h) # n - number of disks; f - from position; h - helper position; t - target position;
        move(f,t)
        hanoi(n-1, h, f, t)

print(hanoi(0, "A", "B", "C"))
