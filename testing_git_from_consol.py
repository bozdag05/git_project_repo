
def git_test(BPLA):
    for info in BPLA:
        return f'Название: {info.name}\n' \
               f'Скорость: {info.speed}\n' \
               f'МАКС Дистанция полёта: {info.max_distance}\n' \
               f'Паталок: {info.max_hight}\n' \
               f'Время полёта: {info.min_time} - {info.midle_time} - {info.max_time}'
