def knapsack(w, *c_w):
    """
    задача о непрерывном рюкзаке
    w - вместимость рюкзака
    c_w - одна или несколько пар [стоимость предмета, вес предмета]

    возвращается стоимость самого дорогого рюкзака

    """
    c_w = list(c_w)
    for i in c_w:
        i.insert(0, i[0]/i[1])
    c_w = sorted(c_w, reverse=True)
    amount = 0
    while w:
        for i in c_w:
            if i[2] <= w:
                amount += i[1]
                w -= i[2]
            else:
                amount += w * i[0]
                w = 0
        break
    return '{:.3f}'.format(amount)

