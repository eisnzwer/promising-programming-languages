print('a b c')
for a in range(2):
    for b in range(2):
        for c in range(2):
            if not((a or b) and (a != c)):
                print(a, b, c)