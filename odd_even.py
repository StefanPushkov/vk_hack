def is_odd(a: int):
    q = bool(a - ((a >> 1) << 1))
    return q
def check(a:int):
    answ = 0
    if is_odd(a):
        print('odd')
        answ = 'odd'
    else:
        print('Even')
        answ = 'Even'
    return answ




check(3)