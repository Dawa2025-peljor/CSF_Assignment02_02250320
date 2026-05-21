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