
def git_test(BPLA):
    for info in BPLA:
        return f'{info.name}\n' \
               f'{info.speed}\n' \
               f'{info.max_distance}\n' \
               f'{info.max_hight}\n' \
               f'{info.min_time} - {info.midle_time} - {info.max_time}'
