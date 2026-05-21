def count_character_frequency(name):
    freq = {}
    for ch in name:
        if ch == ' ':
            continue
        lower_ch = ch.lower()
        freq[lower_ch] = freq.get(lower_ch, 0) + 1
    return freq