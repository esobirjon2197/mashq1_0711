# 1-m
for i in range(1, 51):
    if i % 7 == 0:
        print(i)
        break


# 2-m
for i in range(100, 151):
    if i == 137:
        print(f"{i}-Parol topildi.")
        break


# 3-m
sum = 0
for i in range(1, 10):
    sum += i
    if sum >= 20:
        break
print(sum)


# 4-m
kop = 1
for i in range(1, 21):
    kop *= i
    if kop >= 10000:
        break
print(kop)


