def function_with_uncommon_bug(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_bug(0, 0)
print(result)  # This will return 0, not an error