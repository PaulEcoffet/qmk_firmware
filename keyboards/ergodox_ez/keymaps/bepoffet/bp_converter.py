import re

keycodes = dict()
with open("bepo_alias.txt") as f:
    for line in f:
        try:
            alias, value = line.split()
            if value not in list(keycodes.values()):
                keycodes[value] = alias
            else:
                real_key = None
                for key, valueee in keycodes.items():
                    if valueee == value:
                        real_key = key
                        break
                if len(alias) < len(value):
                    keycodes[real_key] = alias
        except ValueError:
            pass

with open("keymap.c") as f:
    code = f.read()
for kc, bp in keycodes.items():
    code = re.sub(r'([, ]+)('+ re.escape(kc) + r')([, ]+)', r'\1' + re.escape(bp) + r'\3', code)

print(code)
