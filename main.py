def max_dragon_power(N):
    dp = [0] * (N + 1)
    dp[0] = 1  # Пустая стая имеет силу 1
    
    for i in range(1, N + 1):
        for k in range(1, min(7, i) + 1):
            dp[i] = max(dp[i], dp[i - k] * k)
    
    return dp[N]

# Чтение входных данных и вывод результата
if __name__ == "__main__":
    N = int(input())
    print(max_dragon_power(N))
