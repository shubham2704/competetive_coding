for _ in range(int(input())):
    def permute(nums):
        result = [[]]
        for n in nums:
            new = []
            for p in result:
                for i in range(len(p)+1):
                    new.append(p[:i] + [n] + p[i:])
                    result = new
        return result

    n = int(input())
    my_nums = list(map(int,input().split()))
    l = [str(x) for x in my_nums]
    res = permute(l)
    print(sum(int("".join(x)) for x in res))
