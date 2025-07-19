t1 = (1, 2, 3, 4, 5)
t1[0] = 1000  # This will raise an error because tuples are immutable
# t1[0:1]  # This will not raise an error, but it won't change the tuple
p1 = (1)  # This is not a tuple, it's just an integer