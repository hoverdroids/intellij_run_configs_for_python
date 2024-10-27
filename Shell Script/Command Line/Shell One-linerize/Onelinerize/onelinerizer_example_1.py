from onelinerizer import onelinerize

# Onelinerizer doesn't seem to work because it uses reduce() which is not available in Python 3.8,
# This should work if ported to using "from functools import reduce" instead of "reduce" directly
# Going to try PyOneLiner instead

code = """
def add(x, y):
    return x + y
result = add(5, 3)
print(result)
"""

onelinerized_code = onelinerize(code)
exec(onelinerized_code)