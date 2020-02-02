a,b = 502,94278
res = 0
if b % a == 0 or a % b == 0:
    res = max(a,b)
elif a % 3 == 0 and b % 3 == 0:
    res = (a*b)/3
elif a % 2 == 0 and b % 2 == 0:
    res = a*b/2
elif a % 3 != 0 or b % 3 != 0:
    res = a*b
elif a % 2 != 0 or b % 2 != 0:
    res = a*b
print(int(res))