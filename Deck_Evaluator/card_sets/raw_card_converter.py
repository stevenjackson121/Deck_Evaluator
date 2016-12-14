import re


def shorten(name):
    name = name.replace("'", '')
    return ''.join(w[0].upper() + w[1:] for w in re.findall("[A-Za-z]*", name) if len(w) > 0)


def generate_school_levels(school_str, level_str):
    schools = [s.strip() for s in school_str.split(',')]
    if len(schools) == 1:
        level = int(level_str)
        return [{schools[0]: level}]
    elif '&' in level_str and 'or' not in level_str:
        levels = [l.strip() for l in level_str.split('&')]
        return [{s: l for s, l in zip(schools, levels)}]
    elif 'or' in level_str and '&' not in level_str:
        levels = [l.strip() for l in level_str.split('or')]
        return [{s:l} for s, l in zip(schools, levels)]
    else:
        return "Do this manually, complex nesting unsupported"

with open('generated_classes.py', 'w') as gen:
    with open('raw_cards.csv') as raw:
        for line in raw:
            name, metaclass, subtypes, schools, levels, casting_cost, reveal_cost = [s.strip() for s in line.split('\t')]
            out_str = "class %s(" % shorten(name)
            if metaclass == 'Attack':
                metaclass = 'AttackSpell'
            out_str += "metaclass=%s" % metaclass
            out_str += ", casting_cost=%s" % casting_cost
            if metaclass == 'Enchantment':
                out_str += ", reveal_cost=%s" % (reveal_cost or '0')
            out_str += ", school_levels=%s" % generate_school_levels(schools, levels)
            out_str += ", subtypes={%s}" % str(sorted(shorten(s) for s in subtypes.split(',')))[1:-1]
            out_str += "):\n    pass\n\n"

            gen.write(out_str)
            gen.flush()
