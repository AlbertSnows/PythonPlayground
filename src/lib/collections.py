def nth(arr, index):
    if arr and len(arr) > index:
        return arr[index]
    else:
        return None


def first(arr):
    return nth(arr, 0)
