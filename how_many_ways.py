'''
字符A-Z可以编码为0-25。"A"->"0", "B"->"1", ..., "Z"->"25"
现在输入一个数字序列，计算有多少种方式可以解码成字符A-Z组成的序列。
例如：
输入：19
输出：2  --->BJ T
输入：258
输出：2  --->CFI  ZI
输入：0219 -->ACBJ  AVJ  ACT
输出：3
'''


def how_many_ways():
    str = input("输入:")

    count = 1  # 起步一种
    lens = len(str)
    for i in range(lens):
        if i == lens - 1:
            break
        if (int(str[i]) * 10 + int(str[i + 1])) > 9 and (int(str[i]) * 10 + int(str[i + 1])) <= 25:
            count += 1
        else:
            continue
    print(count)


if __name__ == "__main__":
    how_many_ways()
