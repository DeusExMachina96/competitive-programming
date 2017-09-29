def solve(A,N):
  i = 0
  count = 0

  while i < N:
    count += 1
    pivot = A[i]
    while i < N and A[i] <= pivot + 4:
      i += 1

  return count

N = int(raw_input())
A = sorted(map(int,raw_input().split()))
print solve(A,N)