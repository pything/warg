from warg import leaf_apply, leaf_type_apply


def test_leaf_apply():
    asd = [1, 2, 3, 4, 5, 6, 7, 8, 9, [2, 3], [[323, 525], [323, 525], [323]]]
    print(leaf_apply(asd, lambda a: a + 1))


def test_leaf_type_apply():
    asd = [(1, 2), [(3, 4), (3, 4)], [(323, 525)], [[(323, 525), (323, 39)]]]
    print(leaf_type_apply(asd, lambda a: ((a[0] + a[1]), 1), tuple))
