print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if(not(((not x)or y) and (not w) or not (z and not (y and w)))) == 0:
                    print(x, y, z, w)
# в задании есть условие с неповторяющимися строками, перепишу таблицу с эти условием.
# 0 0 0 1
# 0 1 0 1
# 0 1 1 1
# 1 1 1 1
