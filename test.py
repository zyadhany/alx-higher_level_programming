n, k = map(int, input().split())
arr = list(map(int, input().split()))


#Write your code

summ = 0

for i in arr:
    summ += (i <= k)

print(summ)
