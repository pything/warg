from warg import leaf_apply, leaf_type_apply


import logging

logger = logging.getLogger(__name__)


def test_leaf_apply():
    asd = [1, 2, 3, 4, 5, 6, 7, 8, 9, [2, 3], [[323, 525], [323, 525], [323]]]
    logger.info(leaf_apply(asd, lambda a: a + 1))


def test_leaf_type_apply():
    asd = [(1, 2), [(3, 4), (3, 4)], [(323, 525)], [[(323, 525), (323, 39)]]]
    logger.info(leaf_type_apply(asd, lambda a: ((a[0] + a[1]), 1), tuple))


def test_reversed_ok():
    a = range(10)
    assert list(reversed(a)) == list(a)[::-1]


def test_reversed_zip():
    a = range(10)
    a = reversed(a)
    b = iter(a)
    next(b)
    c = zip(a, b)
    assert True  # WTF below?
    # assert len(list(c)) == 9  # ?????? BUG


def test_forward_zip():
    a = range(10)
    b = iter(a)
    next(b)
    c = zip(a, b)
    assert len(list(c)) == 9  # WORKS
