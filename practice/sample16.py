def summationForLoopIteration(n):
  total = 0

  for i in range(n + 1):
    # ローカルスコープから親の変数にアクセス
    total += i

  return total

print(summationForLoopIteration(10))
