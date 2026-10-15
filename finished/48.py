LENGTH = 1000

### naive
result = 0
for i in range(1, LENGTH + 1):
    result += i**i

print(f"Last 10 digits: {str(result)[-10:]}")

### ok lol naive worked just fine
