def get_valid_number():
    while True:
        try:
            num = int(input("Enter a number between 3 and 9: "))
            if 3 <= num <= 9:
                return num
            print("Invalid input. Please enter a number between 3 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 3 and 9.")

def generate_personal_code(student_id, keyword):
    if not keyword:
        return f"-{student_id}-"
    first = keyword[0].upper()
    last = keyword[-1].upper()
    return f"{first}-{student_id}-{last}"

def count_character_frequency(name):
    freq = {}
    for ch in name:
        if ch == ' ':
            continue
        lower_ch = ch.lower()
        freq[lower_ch] = freq.get(lower_ch, 0) + 1
    return freq

def find_unique_vowels_consonants(text):
    vowels = set('aeiou')
    unique_vowels = set()
    unique_consonants = set()
    for ch in text:
        if ch == ' ':
            continue
        lower_ch = ch.lower()
        if lower_ch.isalpha():
            if lower_ch in vowels:
                unique_vowels.add(lower_ch)
            else:
                unique_consonants.add(lower_ch)
    return unique_vowels, unique_consonants

def check_balanced_brackets(expression):
    stack = []
    matching = {')': '(', ']': '[', '}': '{'}
    for ch in expression:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack:
                return False
            top = stack.pop()
            if matching[ch] != top:
                return False
    return not stack

def process_keyword_queue(keyword):
    queue = list(keyword)
    print("Queue Processing:")
    while queue:
        ch = queue.pop(0)
        print(f"Processing: Analyse {ch}")

def print_number_pattern(n):
    print("Number Pattern:")
    for i in range(1, n + 1):
        row = ' '.join(str(x) for x in range(1, i + 1))
        print(row)

def recursive_digit_sum(student_id):
    id_str = str(student_id)
    if len(id_str) == 1:
        return int(id_str)
    return int(id_str[0]) + recursive_digit_sum(id_str[1:])

def display_summary(student_id, full_name, keyword, number, bracket_expr,
                    personal_code, freq_dict, vowels_set, consonants_set,
                    is_balanced, digit_sum):
    print("\n" + "=" * 40)
    print("Personal Pattern Toolkit - Summary")
    print("=" * 40)
    print(f"Personal Code: {personal_code}")
    print("\nCharacter Frequency (Full Name, ignoring spaces, case‑insensitive):")
    for ch in sorted(freq_dict.keys()):
        print(f"  {ch}: {freq_dict[ch]}")
    vowels_str = ', '.join(sorted(vowels_set)) if vowels_set else "none"
    consonants_str = ', '.join(sorted(consonants_set)) if consonants_set else "none"
    print(f"\nUnique Vowels: {vowels_str}")
    print(f"Unique Consonants: {consonants_str}")
    print(f"\nBalanced Brackets: {'Yes' if is_balanced else 'No'}")
    print(f"\nRecursive Digit Sum of Student ID: {digit_sum}")
    print("=" * 40)

def main():
    print("Personal Pattern Toolkit")
    print("-" * 30)

    student_id = input("Enter Student ID: ")
    full_name = input("Enter Full Name: ")
    keyword = input("Enter Keyword: ")
    number = get_valid_number()
    bracket_expr = input("Enter bracket expression: ")

    personal_code = generate_personal_code(student_id, keyword)
    freq_dict = count_character_frequency(full_name)
    vowels_set, consonants_set = find_unique_vowels_consonants(keyword)
    is_balanced = check_balanced_brackets(bracket_expr)
    process_keyword_queue(keyword)          # prints queue output
    print_number_pattern(number)            # prints number triangle
    digit_sum = recursive_digit_sum(student_id)

    display_summary(student_id, full_name, keyword, number, bracket_expr,
                    personal_code, freq_dict, vowels_set, consonants_set,
                    is_balanced, digit_sum)

if __name__ == "__main__":
    main()