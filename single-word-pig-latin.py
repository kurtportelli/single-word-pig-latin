def pig_latin(s):
    import re
    s = s.lower()
    if not s.isalpha():
        return None
    if not re.search(r'[aeiou]', s):
        return s + 'ay'
    if re.match(r'[aeiou]', s):
        return s + 'way'
    while not re.match(r'[aeiou]', s):
        s = s[1:] + s[0]
    return s + 'ay'
