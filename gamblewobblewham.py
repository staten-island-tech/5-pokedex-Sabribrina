def casino (quarters, first, second, third):
    num_plays = 0
    while quarters >= 1:
        if first < 35:
            num_plays += 1
            first += 1
            quarters -= 1
        if first == 35:
            quarters += 30
            first = 0
        if quarters == 0:
            print(num_plays)
        if second < 100:
            num_plays += 1
            second += 1
            quarters -= 1
        if second == 100:
            quarters += 60
            second = 0
        if quarters == 0:
            print(num_plays)
        if third < 10:
            num_plays += 1
            third += 1
            quarters -= 1
        if third == 10:
            quarters += 9
            third = 0
        if quarters == 0:
            print(num_plays)
    if quarters == 0:
        print(num_plays)
casino(48, 3, 10, 4)
casino(77, 4, 9, 3)