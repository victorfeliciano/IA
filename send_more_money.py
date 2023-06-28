from itertools import permutations

def solve_cryptarithmetic():
    for S in range(1, 10):
        for E in range(10):
            if E == S:
                continue
            for N in range(10):
                if N == S or N == E:
                    continue
                for D in range(10):
                    if D == S or D == E or D == N:
                        continue
                    for M in range(1, 10):
                        if M == S or M == E or M == N or M == D:
                            continue
                        for O in range(10):
                            if O == S or O == E or O == N or O == D or O == M:
                                continue
                            for R in range(10):
                                if R == S or R == E or R == N or R == D or R == M or R == O:
                                    continue
                                for Y in range(10):
                                    if Y == S or Y == E or Y == N or Y == D or Y == M or Y == O or Y == R:
                                        continue
                                    send = 1000 * S + 100 * E + 10 * N + D
                                    more = 1000 * M + 100 * O + 10 * R + E
                                    money = 10000 * M + 1000 * O + 100 * N + 10 * E + Y

                                    if send + more == money:
                                        return (send, more, money)

    return None

solution = solve_cryptarithmetic()
if solution:
    send, more, money = solution
    print("Send =", send)
    print("More =", more)
    print("Money =", money)
else:
    print("Não foi encontrada uma solução válida.")

