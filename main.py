REFLECTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
              1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
              2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
              3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
              4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ'}

ROTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
          1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
          2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
          3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
          4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
          5: 'VZBRGITYUPSDNHLXAWMJQOFECK',
          6: 'JPGVOUMFYQBENHZRDKASXLICTW',
          7: 'NZJHGRCXMYSWBOUFAIVLPEKQDT',
          8: 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
          'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
          'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'}

TYPE = {1: 17,
        2: 5,
        3: 22,
        4: 10,
        5: 0}

def reflector(symbol, n):
    return REFLECTORS[n][REFLECTORS[0].index(symbol)]

def rotor(symbol, n, reverse=False):
    if reverse:
        return ROTORS[0][ROTORS[n].index(symbol)]
    else:
        return ROTORS[n][ROTORS[0].index(symbol)]

def pairs_dict_create(pairs):
    if len(pairs.replace(" ", "")) % 2 != 0:
        return
    pdict = dict()
    for i in pairs.upper().split():
        if i[0] in pdict or i[1] in pdict:
            return
        pdict[i[0]] = i[1]
        pdict[i[1]] = i[0]
    return pdict

def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3, pairs=""):
    pdict = pairs_dict_create(pairs)
    if pdict == None:
        return "Извините, невозможно произвести коммутацию"
    res = ''
    rots = [rot1, rot2, rot3]
    shifts = [shift1, shift2, shift3]
    for sym in text:
        if sym.isalpha():
            sym = sym.upper()
            if sym in pdict:
                sym = pdict[sym]

            shifts[-1] = (shifts[-1] + 1) % len(ROTORS[0])
            if shifts[-1] == TYPE[rots[-1]]:
                shifts[-2] = (shifts[-2] + 1) % len(ROTORS[0])
            else:
                for i in range(len(rots) - 2, 0, -1):
                    if shifts[i] == TYPE[rots[i]] - 1:
                        shifts[i] = (shifts[i] + 1) % len(ROTORS[0])
                        shifts[i - 1] = (shifts[i - 1] + 1) % len(ROTORS[0])

            for rs in range(len(rots)):
                sym = ROTORS[0][(ROTORS[0].index(rotor(ROTORS[0][(ROTORS[0].index(sym) + shifts[len(shifts) - rs - 1]) % len(ROTORS[0])], rots[len(rots) - rs - 1], False)) - shifts[len(shifts) - rs - 1]) % len(ROTORS[0])]
            sym = reflector(sym, ref)
            for rs in range(len(rots)):
                sym = ROTORS[0][(ROTORS[0].index(rotor(ROTORS[0][(ROTORS[0].index(sym) + shifts[rs]) % len(ROTORS[0])], rots[rs], True)) - shifts[rs]) % len(ROTORS[0])]

            if sym in pdict:
                sym = pdict[sym]
            res += sym
    return res

print(enigma('AAAAAAA', 1, 2, 3, 2, 3, 2, 3))