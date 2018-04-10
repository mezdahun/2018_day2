def find_maxima(x):
    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 1, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    If in a local maximum several elements have the same value,
    return the rightmost index.
    Example:
    >>> x = [1, 2, 2, 2, 1]
    >>> find_maxima(x)
    [3]

    Input arguments:
        x -- 1D list of numbers

    Output:
        idx -- list of indices of the local maxima in x
    """

    idx = []
    up = False
    down = False
    for i in range(len(x)):
        if i == 0 or x[i-1] < x[i]:
            up = True
        elif x[i-1] > x[i]:
            up = False

        # if x[i-1] == x[i], no change

        if i+1 == len(x) or x[i+1] < x[i]:
            down = True
        elif x[i+1] > x[i]:
            down = False

        if up and down:
            idx.append(i)

    return idx
