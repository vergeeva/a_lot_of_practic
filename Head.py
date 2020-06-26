def nok(a_, b_):
    m = a_ * b_
    while a_ != 0 and b_ != 0:
        if a_ > b_:
            a_ %= b_
        else:
            b_ %= a_
    return m // (a_ + b_)


def division(aa, bb, cc, dd):
    if bb == dd:
        return aa + cc, bb
    else:
        return aa * (nok(bb, dd) // bb) + cc * (nok(bb, dd) // dd), nok(bb, dd)


def discount(v):  # Ищем скидочку
    if 1000 <= v < 2000:
        return 0.03
    elif 2000 <= v < 5000:
        return 0.05
    elif v >= 5000:
        return 0.07
    else:
        return 0


def control_str():
    str_ = input("Введите строку: ")
    if len(str_) > 10:
        str_ = str_[:10]
        return str_
    else:
        str_ = str_ + '*' * (10 - len(str_))
        return str_
