def max_ice_cream(costs, coins):
    max_cost = max(costs)

    # Hitung frekuensi tiap harga
    count = [0] * (max_cost + 1)

    for cost in costs:
        count[cost] += 1

    bars = 0

    # Beli dari harga termurah
    for price in range(1, max_cost + 1):
        if count[price] == 0:
            continue

        # Banyak es krim yang bisa dibeli dengan harga ini
        can_buy = min(count[price], coins // price)

        bars += can_buy
        coins -= can_buy * price

    return bars


# Input
costs = list(map(int, input("Masukkan harga es krim: ").split()))
coins = int(input("Masukkan jumlah koin: "))

# Output
result = max_ice_cream(costs, coins)
print("Maksimum es krim yang bisa dibeli:", result)