import math

while True:
    try:
        
        c = int(input())
        r = int(input())
        N = int(input())

        expected_profit = [0.0] * (N + 1)

        for d in range(N + 1):
            p = float(input())

            for q in range(N + 1):
                if q <= d:
                    profit = (r - c) * q
                else:
                    profit = r * d - c * q

                expected_profit[q] += p * profit

        best_q = 0
        best_profit = expected_profit[0]

        for q in range(1, N + 1):
            if expected_profit[q] > best_profit:
                best_profit = expected_profit[q]
                best_q = q

        print(best_q, math.floor(best_profit))

    except EOFError:
        break