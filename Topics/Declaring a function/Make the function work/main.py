def closest_higher_mod_5(x):
    remainder = x % 5
    return \
        x if remainder == 0 \
        else x + (5 - remainder)

