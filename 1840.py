def maxBuilding(n, restrictions):
    restrictions.append([1, 0])

    has_n = False
    for pos, h in restrictions:
        if pos == n:
            has_n = True
            break

    if not has_n:
        restrictions.append([n, n - 1])

    restrictions.sort()

    m = len(restrictions)

    # Left -> Right
    for i in range(1, m):
        dist = restrictions[i][0] - restrictions[i - 1][0]

        restrictions[i][1] = min(
            restrictions[i][1],
            restrictions[i - 1][1] + dist
        )

    # Right -> Left
    for i in range(m - 2, -1, -1):
        dist = restrictions[i + 1][0] - restrictions[i][0]

        restrictions[i][1] = min(
            restrictions[i][1],
            restrictions[i + 1][1] + dist
        )

    print("\nRestrictions setelah propagasi:")
    for pos, h in restrictions:
        print(f"({pos}, {h})")

    ans = 0

    for i in range(1, m):
        x1, h1 = restrictions[i - 1]
        x2, h2 = restrictions[i]

        d = x2 - x1

        peak = (h1 + h2 + d) // 2

        print(f"\nInterval [{x1},{x2}] peak = {peak}")

        ans = max(ans, peak)

    return ans


# Test Case
n = 10

restrictions = [
    [5, 3],
    [2, 5],
    [7, 4],
    [10, 3]
]

print("\nAnswer =", maxBuilding(n, restrictions))