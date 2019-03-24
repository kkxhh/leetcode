
# 生活日常之蔬菜购买

# Description

# Rahul wanted to purchase vegetables mainly brinjal, carrot and tomato. There are N different vegetable sellers in a line. Each vegetable seller sells all three vegetable items, but at different prices. Rahul, obsessed by his nature to spend optimally, decided not to purchase same vegetable from adjacent shops. Also, Rahul will purchase exactly one type of vegetable item (only 1 kg) from one shop. Rahul wishes to spend minimum money buying vegetables using this strategy. Help Rahul determine the minimum money he will spend.

# Input

# First line indicates number of test cases T. Each test case in its first line contains N denoting the number of vegetable sellers in Vegetable Market. Then each of next N lines contains three space separated integers denoting cost of brinjal, carrot and tomato per kg with that particular vegetable seller.

# Output

# For each test case, output the minimum cost of shopping taking the mentioned conditions into account in a separate line.

# Constraints:1 <= T <= 101 <= N <= 100000 Cost of each vegetable(brinjal/carrot/tomato) per kg does not exceed 10^4

# Sample Input 1
'''
1
3
1 50 50
50 50 50
1 50 50
'''
# Sample Output 1

# 52

def solve( nums):
 
    dp1=0
    dp2=0
    dp3=0
    old1=dp1
    old2=dp2
    old3=dp3
    for i in nums:
        dp1=i[0]+min(old2,old3)
        dp2=i[1]+min(old1,old3)
        dp3=i[2]+min(old1,old2)
        old1,old2,old3=dp1,dp2,dp3
    return min(dp1,dp2,dp3)


T=int(input())
while T!=0:
    T-=1
    N=int(input())
    price=[]
    for _ in range(N):
        price.append([int(i) for i in input().split()])

    print(solve(price))