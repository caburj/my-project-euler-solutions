def rotations(num):
    num_str = str(num)
    for _ in range(len(num_str)):
        num_str = num_str[1:] + num_str[0:1]
        yield num_str
        