from secrets import token_hex

#CHARACTERS = (string.ascii_uppercase + string.digits)

def gen_key(parts=4, chars_per_part=8):
    return '-'.join(token_hex(chars_per_part//2) for _ in range(parts)).upper()

