def parse(rn):
    ans = 0
    init = list(rn)

    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    prev = None
    for r in init:
        ans += values[r]

        if r == 'V' and prev == 'I':
            ans -= 2
        elif r == 'X' and prev == 'I':
            ans -= 2
        elif r == 'L' and prev == 'X':
            ans -= 20
        elif r == 'C' and prev == 'X':
            ans -= 20
        elif r == 'D' and prev == 'C':
            ans -= 200
        elif r == 'M' and prev == 'C':
            ans -= 200

        prev = r

    return ans
