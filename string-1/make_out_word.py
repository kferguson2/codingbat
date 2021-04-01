def make_out_word(out_string, word):
    """Given an "out" string length 4, such as "<<>>", and a word
    return a new string where the word is in the middle of the out string, e.g. "<<word>>". """
    if len(out_string) != 4:
        raise ValueError('out_string has to have length of 4')
    out_beg = out_string[:2]
    out_end = out_string[2:4]
    return f'{out_beg}{word}{out_end}'


print(make_out_word('<<>>', 'Yay')) # <<Yay>>
print(make_out_word('<<>>', 'WooHoo')) # <<WooHoo>>
print(make_out_word('[[]]', 'word')) # [[word]]
# print(make_out_word('[[]', 'word')) # ValueError: out_string has to have length of 4