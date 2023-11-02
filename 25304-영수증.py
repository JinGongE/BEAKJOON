x= int(input())
n = int(input())
total = 0
for i in range(n):
    a, b = input().split()
    total += int(a)*int(b)
if total == x:
    print("Yes")
else:
    print("No")