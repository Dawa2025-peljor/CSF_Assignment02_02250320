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
    # queue output already printed in its own function
    print(f"\nRecursive Digit Sum of Student ID: {digit_sum}")
    print("=" * 40)