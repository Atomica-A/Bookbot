

def words_count(text):
    count = text.split()
    result = len(count)
    return result

def character_count(text):
    characters = list(text.lower())
    c_count = {}
    for c in characters:
        c_count[c] = c_count.get(c, 0) + 1
    return c_count

def report(c_count):
    sorted_c_count = dict(sorted(c_count.items(), key=lambda item: item[1], reverse=True))
    f_report = []
    for key, value in sorted_c_count.items():
        if key.isalpha():
            a = {"char": key, "num" : value}
            b = f"{a.get('char')}: {a.get('num')}"
            f_report.append(b)
    return '\n'.join(f_report)



