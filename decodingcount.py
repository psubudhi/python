def count_decodings(digits):
    n = len(digits)
    print[0]
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1 if digits[0] != "0" else 0
    for i in range(2, n + 1):
        if digits[i - 1] != "0":
            dp[i] += dp[i - 1]
        if digits[i - 2:i] >= "10" and digits[i - 2:i] <= "26":
            dp[i] += dp[i - 2]
    return dp[n]

digits = "123"
count = count_decodings(digits)
print(f"The number of possible decodings of {digits} is {count}")

