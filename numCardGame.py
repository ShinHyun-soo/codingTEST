n, m = map(int, input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))

  min_value = min(data)

  result = max(result, min_value)

print(result)

//\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\//

n, m = map(int, input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))

  min_value = 10001
  for a in data:
    min_value = min(min_value, a)       #여기 왜 a가 있지? -> data 원소, data가 [5 3 1 5] 면 네번 반복문 돌면서 a = 5 , a = 3, a = 1, a = 5 로 바뀜.(by.meansub)

    result = max(result, min_value)

print(result)
