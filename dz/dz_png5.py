print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (((not x) or y or z) and ((not x) or (not z))) == 0:
                print(x, y, z)
# под столбцом где все 1 стоит x. под столбцом где 2 единицы стоит z. Осталя y, он под первым столбцом задания. ответ yzx