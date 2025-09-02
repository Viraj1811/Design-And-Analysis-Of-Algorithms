def power(base, exponent):
    result = 1
    for i in range(exponent):
            result = base * result
    return result

print(power(2,3))

# recursive approach for both negative and positive numbers
def power_re(base, exponent):
    result = 1
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power_re(base, -exponent)
    else:
        result = base * power_re(base, exponent - 1)
        return result

print(power_re(2,-3))
