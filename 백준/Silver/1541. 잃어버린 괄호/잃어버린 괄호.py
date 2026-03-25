expression = input().strip()

parts = expression.split('-')

# 첫 번째 덩어리는 더해주고
result = sum(map(int, parts[0].split('+')))

# 그 뒤 덩어리들은 전부 더해서 빼기
for part in parts[1:]:
    result -= sum(map(int, part.split('+')))

print(result)