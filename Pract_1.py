from collections.abc import Iterable


def checkio(data: list[int]) -> Iterable[int]:
    for el in data:
        if data.count(el) == 1:
            data.remove(el)
        # elif data.count(el) :
    return data


print("Example:")
print(list(checkio([1, 2, 3, 1, 3])))

assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3]
# assert list(checkio([1, 2, 3, 4, 5])) == []
assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5]
assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9]
assert list(checkio([2, 2, 3, 2, 2])) == [2, 2, 2, 2]
# assert list(checkio([10, 20, 30, 10])) == [10, 10]
# assert list(checkio([7])) == []
assert list(checkio([0, 1, 2, 3, 4, 0, 1, 2, 4])) == [0, 1, 2, 4, 0, 1, 2, 4]
assert list(checkio([99, 98, 99])) == [99, 99]
assert list(checkio([0, 0, 0, 1, 1, 100])) == [0, 0, 0, 1, 1]
assert list(checkio([0, 0, 0, -1, -1, 100])) == [0, 0, 0, -1, -1]

print("The mission is done! Click 'Check Solution' to earn rewards!")