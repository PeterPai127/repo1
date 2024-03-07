for a in range(1, 10):
    for b in range(1, 10):
        if (a*b)<10:
            print(f'{a}x{b}={a*b}',end='  ')   # 如果 axb<10，讓結尾增加一個空白
        else:
            print(f'{a}x{b}={a*b}',end=' ')
    print('')