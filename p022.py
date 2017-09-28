from string import ascii_uppercase
equiv = dict(zip(list(ascii_uppercase), range(1, len(ascii_uppercase) + 1)))


with open('data_p022') as f:
    names = sorted([name.strip('"') for name in f.read().strip().split(',')])


def score(name):
    return sum(equiv[letter] for letter in name)


print(sum((i + 1) * score(name) for i, name in enumerate(names)))

for i, name in enumerate(names):
    print(i, name)
