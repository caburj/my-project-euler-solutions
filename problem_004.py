"""
"""

for i in xrange(999, 900, -1):
    for j in xrange(999, 900, -1):
        prod = i * j
        prod = list(str(prod))
        if ''.join(prod) == ''.join(reversed(prod)):
            print ''.join(prod)
            break
