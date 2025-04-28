import math

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


def cut_rod(p: list[int], n: int) -> int:
    """
    计算长度为 n 的钢条通过切割所能获得的最大收益。

    Args:
        p: 一个列表，p[i] 表示长度为 i 的钢条的价格。
        n: 钢条的总长度。

    Returns:
        长度为 n 的钢条的最大收益。
    """
    if n == 0:
        return 0
    q = -math.inf
    for i in range(1, n + 1):
        q = max(q, p[i] + cut_rod(p, n - i))
    return q


def memoized_cut_rod(p: list[int], n: int) -> int:
    """
    使用记忆化自顶向下方法计算切割长度为 n 的钢条的最大收益。

    Args:
        p: 一个列表，p[i] 表示长度为 i 的钢条的价格。
        n: 钢条的总长度。

    Returns:
        长度为 n 的钢条的最大收益。
    """
    r = [-math.inf] * (n + 1)
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p: list[int], n: int, r: list[int]) -> int:
    """
    辅助函数，实现记忆化递归计算。

    Args:
        p: 价格列表。
        n: 当前钢条长度。
        r: 存储已计算收益的列表。

    Returns:
        长度为 n 的钢条的最大收益。
    """
    if r[n] >= 0:
        return r[n]
    if n == 0:
        q = 0
    else:
        q = -math.inf
        for i in range(1, n + 1):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, r))
    r[n] = q
    return q


def bottom_up_cut_rod(p: list[int], n: int) -> int:
    """
    使用自底向上动态规划方法计算切割长度为 n 的钢条的最大收益。

    Args:
        p: 一个列表，p[i] 表示长度为 i 的钢条的价格。
        n: 钢条的总长度。

    Returns:
        长度为 n 的钢条的最大收益。
    """
    r = [0] * (n + 1)
    for j in range(1, n + 1):
        q = -math.inf
        for i in range(1, j + 1):
            q = max(q, p[i] + r[j - i])
        r[j] = q
    return r[n]


def extended_bottom_up_cut_rod(p: list[int], n: int) -> tuple[list[int], list[int]]:
    """
    使用自底向上动态规划方法计算切割长度为 n 的钢条的最大收益，
    并记录获得最大收益的切割方案。

    Args:
        p: 一个列表，p[i] 表示长度为 i 的钢条的价格。
        n: 钢条的总长度。

    Returns:
        一个元组，包含：
        - r: 一个列表，r[j] 存储长度为 j 的钢条的最大收益。
        - s: 一个列表，s[j] 存储获得长度为 j 的钢条最大收益的第一段切割长度。
    """
    r = [0] * (n + 1)
    s = [0] * (n + 1)
    for j in range(1, n + 1):
        q = -math.inf
        for i in range(1, j + 1):
            if q < p[i] + r[j - i]:
                q = p[i] + r[j - i]
                s[j] = i
        r[j] = q
    return r, s


def print_cut_rod_solution(p: list[int], n: int) -> None:
    """
    打印长度为 n 的钢条的最优切割方案。

    Args:
        p: 价格列表。
        n: 钢条的总长度。
    """
    (_, s) = extended_bottom_up_cut_rod(p, n)
    while n > 0:
        print(s[n], end=" ")
        n = n - s[n]
    print()


if __name__ == "__main__":
    print("自顶向下递归实现")

    for i in range(1, 11):
        rod_length = i
        max_revenue = cut_rod(p, rod_length)
        print(f"\t长度为 {rod_length} 的钢条的最大收益: {max_revenue}")

    print("带备忘的自顶向下法")

    for i in range(1, 11):
        rod_length = i
        max_revenue = memoized_cut_rod(p, rod_length)
        print(f"\t长度为 {rod_length} 的钢条的最大收益: {max_revenue}")

    print("自底向上法")

    for i in range(1, 11):
        rod_length = i
        max_revenue = bottom_up_cut_rod(p, rod_length)
        print(f"\t长度为 {rod_length} 的钢条的最大收益: {max_revenue}")

    print("重构解")

    for i in range(1, 11):
        rod_length = i
        print(f"\t长度为 {rod_length} 的钢条的重构解数组: ", end="")
        print_cut_rod_solution(p, rod_length)
