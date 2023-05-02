
def is_usable_for_BAC(number_to_check):
    str_set_to_check = set(str(number_to_check))
    if number_to_check < 1000:
        str_set_to_check.add('0')

    if len(str_set_to_check) == 4:
        return True
    else:
        return False
