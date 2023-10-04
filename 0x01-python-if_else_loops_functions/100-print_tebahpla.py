#!/usr/bin/python3
for a in range(25, -1, -1):
    b = a + ord('A')
    if a % 2 == 1:
        b += 32
    print("{:c}".format(b), end="")
