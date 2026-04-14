for i in range(1, 6):
    for j in range(1, 6):
        if i <= 6-j:
            if j % 2 == 0:
                print('*', end=' ')
            else:
                print(j, end=" ")
        else:
            print(' ', end=" ")

    print()
