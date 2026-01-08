# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, separator = ","):
    participants_first = set(participants_first_group.split(separator))
    participants_second = participants_second_group.split(separator)
    participants_common = list(participants_first.intersection(participants_second))
    participants_common.sort()
    return participants_common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, separator = "|"))