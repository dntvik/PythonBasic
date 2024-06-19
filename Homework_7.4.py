def common_elements():
    l1 = set(range(0, 100, 3))
    l2 = set(range(0, 100, 5))
    l3 = l1.intersection(l2)
    return l3


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
