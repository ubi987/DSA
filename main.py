def func(s):
    freq_count = {}

    for char in str:
        freq_count[char] = freq_count.get(char, 0) + 1

    for i in range(len(str)):
        if freq_count[str[i]] == 1:
            return i

    return -1
str = "leetcode"
result = func(str)
print(result)