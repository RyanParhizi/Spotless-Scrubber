def Levenshtein_distance(a, b):
    if len(a) == 0:
        return len(b)
    elif len(b) == 0:
        return len(a)
    elif a[0] == b[0]:
        return Levenshtein_distance(a[1:], b[1:])
    else:
        return 1 + min(Levenshtein_distance(a[1:], b), Levenshtein_distance(a, b[1:]), Levenshtein_distance(a[1:], b[1:]))
