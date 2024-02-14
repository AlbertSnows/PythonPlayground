def nth(arr, index):
    if arr and len(arr) > index:
        return arr[index]
    else:
        return None


def first(arr):
    return nth(arr, 0)


def rest(seq):
    if len(seq) <= 1:
        return []
    return seq[1:]
