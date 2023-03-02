min_f = None

for x in range(-9, 9 + 1):
    function = x**2 - 6 * x + 3
    if min_f == None or function < min_f:
        min_x = x
        min_f = function

print(f"x = {min_x} y f(x) = {min_f}")
