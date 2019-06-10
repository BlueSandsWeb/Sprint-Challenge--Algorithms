def test(n):
    sum = 0
    for i in range(n):
        i += 1
        # print("i: ", i)
        for j in range(i + 1, n):
            j += 1
            # print("j: ", j)
            for k in range(j + 1, n):
                k += 1
                # print("k: ", k)
                for l in range(k + 1, 10 + k):
                    l += 1
                    # print("l: ", l)
                    sum += 1
    return sum


# print(test(1))
# print(test(5))
# print(test(10))
# print(test(20))
# print(test(30))
# print(test(100))

count = 0


def bunnyEars(bunnies):
    global count
    count += 1
    print(count)
    if bunnies == 0:
        return 0

    return 2 + bunnyEars(bunnies-1)


print(bunnyEars(4))
