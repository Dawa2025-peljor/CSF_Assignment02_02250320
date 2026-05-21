def recursive_digit_sum(student_id):
    id_str = str(student_id)
    if len(id_str) == 1:
        return int(id_str)
    return int(id_str[0]) + recursive_digit_sum(id_str[1:])