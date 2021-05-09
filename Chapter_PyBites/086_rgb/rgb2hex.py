def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
       boundaries (0, 255) and returns its converted hex, for example:
       Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    if not all(0 <= n <= 255 for n in rgb) or len(rgb) != 3:
        raise ValueError
    return "#" + "".join(f"{n:02x}" for n in rgb).upper()

#[f"{n:02x}" for n in (255,255,255)] this will return a list
#"".join(f"{n:02x}" for n in (192,192,192)) to return it as a string and get string methods
#"#"+"".join(f"{n:02x}" for n in (192,192,192)).upper()