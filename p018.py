"""maximum path sum 1"""


from myfuncs import flat


def get_data():
    with open('data_p018') as f:
        dat = f.read().strip().split('\n')
        dat = [[int(x) for x in ls.split(' ')] for ls in dat]
    return dat


def implement_alg_from_so(dat):
    def func(a, b):
        return [a[i] + max(b[i], b[i+1]) for i in range(len(a))]
    for i in range(len(dat)-2, -1, -1):
        dat[i] = func(dat[i], dat[i+1])
    return dat[0][0]


class BinaryTree(object):
    def __init__(self, val):
        self._val = val
        self._left = None
        self._right = None

    def set_left(self, tree):
        self._left = tree

    def set_right(self, tree):
        self._right = tree

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right

    def get_val(self):
        return self._val


def create_btree(dat):
    nodes = [BinaryTree(val) for val in flat(dat)]
    start = 0
    for i in range(1, len(dat)):
        end = start + i
        n = 0
        for j in range(start, end):
            nodes[j].set_left(nodes[end+n])
            nodes[j].set_right(nodes[end+n+1])
            n += 1
        start = end
    return nodes[0]

max_total = 0
max_leaf = None

def maxsum(root, total):
    global max_total
    global max_leaf
    if root is not None:
        total = total + root.get_val()
        if total > max_total and root.get_left() is None and root.get_right() is None:
            max_leaf = root
            max_total = total
        maxsum(root.get_left(), total)
        maxsum(root.get_right(), total)


dat = get_data()
print implement_alg_from_so(dat)
