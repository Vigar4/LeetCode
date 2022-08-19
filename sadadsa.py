def cc():
    k = 1235321
    text = str(k)
    l = True
    print(text)
    text = list(text)
    print(text[0])
    print(len(text))
    if len(text) % 2 == 0:
        for i in range(0, len(text) / 2):
            print(text[i])
            print(text[int(len(text) - i - 1)])
            if text[i] != text[len(text) - i - 1]:
                l = False
    else:
        for i in range(0, int(len(text) / 2 - 1)):
            if text[i] != text[len(text) - i - 1]:
                l = False

    print(l)


cc()

print(int(7 / 2))


def asdsad():
    n = [1, 3, 5, 7, 9]
    o = 5

    if o < n[0]:
        return 0

    if o > n[len(n) - 1]:
        return len(n)

    for i in n:
        if o == i:
            print('*****')
            return n.index(i) - 1

        if o > n[n.index(i)] and o < n[n.index(i) + 1]:
            print('-----')
            return n.index(i) + 1


asdsad()


def asdasdas():
    nums = [4, -6, 8, 9, 2, 0, 3, -3, -2, 0, 0]
    print(len(nums))
    nums = list(nums)

    rtype = [[]]
    v = 0
    if len(nums) == 0:
        rtype = []
        return rtype
    if len(nums) == 1 and nums[0] == 0:
        rtype = []

    for p in range(0, len(nums)):
        i = nums[p]

        for j in range(nums.index(i) + 1, len(nums)):
            m = nums[j]
            for k in range(nums.index(m) + 1, len(nums)):
                b = nums[k]
                if i + m + b == 0:
                    temp = [i,m,b]


                    rtype = [i, m, b]


    for kk in rtype:
        print(kk)


asdasdas()
