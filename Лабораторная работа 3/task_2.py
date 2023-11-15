def find_common_participants(first_one, second_one, sep=","):
    gr1 = first_one.split(sep)
    gr2 = second_one.split(sep)
    here = list(set(gr1).intersection(gr2))
    here.sort()
    return here


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


print(find_common_participants(participants_first_group, participants_second_group, sep="|"))# TODO Провеьте работу функции с разделителем отличным от запятой


