"""from datetime import datetime

def get_seconds():
    Return current second
    return datetime.now().second()
"""

def func_annotation(x: int, y: int) -> int: # x annotation y annotation  -> return type
    return x + y

print(func_annotation(10,11))
print(func_annotation('still', 'works'))
