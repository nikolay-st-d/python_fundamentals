def loading_bar(loading_num):
    percent_char = '%'
    point_char = '.'
    if loading_num == 100:
        print('100% Complete!')
        print(f'[{percent_char * 10}]')
    else:
        print(f'{loading_num}% [{percent_char * (int(loading_num) // 10)}{point_char * (10 - int(loading_num // 10))}]')
        print('Still loading...')


loading_number = int(input())
loading_bar(loading_number)