def generate_personal_code(student_id, keyword):
    if not keyword:
        return f"-{student_id}-"
    first = keyword[0].upper()
    last = keyword[-1].upper()
    return f"{first}-{student_id}-{last}"