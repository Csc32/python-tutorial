def sum(num1: int, num2: int):
    result = num1 + num2
    return result

print(sum(5,2))
print(sum(25,22))
print(sum(-5,22))
print("-"* 40)
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))
print(f(1))

