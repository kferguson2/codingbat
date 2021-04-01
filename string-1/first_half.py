def first_half(string):
    """ Given a string of even length, return the first half. 
    So the string "WooHoo" yields "Woo". """
    if len(string) % 2 == 0:
        raise ValueError('string has to be of even length')
    index = int(len(string) / 2)
    return string[:index]

print(first_half('WooHoo')) # Woo
print(first_half('HelloThere')) # Hello
print(first_half('abcdef')) # abc
print(first_half('abcdefg')) # ValueError: string has to be of even length