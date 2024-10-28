import stats

def test_max():
    ls = [4, 55, 7, 90,8.0, 2.1]
    assert stats.median(ls) <= max(ls)
    ls_1 = [4, 55, 7, 90,8.0, 2.1,-90]
    assert stats.median(ls_1) <= max(ls_1)
    ls_2 = [4, 55, 7, 90,8.0, 2.1,-90, 0.2]
    assert stats.median(ls_2) <= max(ls_2)
def test_min():
    ls = [4, 55, 7, 90,8.0, 2.1]
    assert stats.median(ls) >= min(ls)
    ls_1 = [4, 55, 7, 90,8.0, 2.1,-90]
    assert stats.median(ls_1) >= min(ls_1)
    ls_2 = [4, 55, 7, 90,8.0, 2.1,-90, 0.2]
    assert stats.median(ls_2) >= min(ls_2)
def test_median():
    assert stats.median([1,8,3]) == 3
    assert stats.median([1,2,3]) == 2
    assert stats.median([12,3,90]) == 12
