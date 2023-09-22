summa = 0
for i in range(1, 1_000_000_003, 3):
    if not (i % 10 == 7 or i % 10 == 4):
        summa += i
    #if i // 1_000_000 wfwefwe

print(summa)
