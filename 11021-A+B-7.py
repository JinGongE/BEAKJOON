import sys
n = sys.stdin.readline().rstrip()

for i in range(int(n)):
    a, b = sys.stdin.readline().split()
    print("Case #{}: ".format(i+1) + str(int(a)+int(b)))