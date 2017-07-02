index = 3
result = 1
while index > 0:
    result *= index
    index -= 1
print(result)

index = 3
result = 1
def factorial(result, index):
    result *= index
    if index > 0:
        factorial(result, index-1)
    if index == 1:
        print(result)

factorial(result, index)