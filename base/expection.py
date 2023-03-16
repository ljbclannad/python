try:
    # print(10/0)
    1 + [1,2]
except ZeroDivisionError as err:
    print('err:{}'.format(err))
except Exception as err:
    print('exception:{}'.format(err))    