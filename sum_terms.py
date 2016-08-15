def series_sum(n):
    """Return the sum of a series up to the nth term."""
    if n == 0:
        return '0.00'
    sum = 0
    for i in range(n):
        sum += 1 / ((3 * i) + 1)
    return '{0:.2f}'.format(round(sum, 2))
