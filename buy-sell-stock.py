def max_profit(prices):
    cur_max,max_so_for=0,0
    for i in range(1,len(prices)):
        cur_max=max(0,cur_max+prices[i]-prices[i-1])
        max_so_for=max(max_so_for,cur_max)
    return max_so_for

print(max_profit([6,1,3,3,6,7]))