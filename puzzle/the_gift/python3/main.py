oods = int(input())
gift = int(input())

budget = [int(input()) for i in range(oods)]
shares = []

if sum(budget) < gift:
    print("IMPOSSIBLE")
else:
    budget.sort()
    
    for i in range(oods):
        share = min(budget[i], gift // (oods - i))
        gift -= share
        shares.append(str(share))
    
    print("\n".join(shares))
