"""def even_range(start, end):
    current = start
    while current < end:
        yield current
        current += 2

ranger = even_range(0, 10)

print(next(ranger))
print(next(ranger))
print(next(ranger))
print(next(ranger))
print(next(ranger))
"""
"""
def list_generator(list_obj):
    for item in list_obj:
        yield item
        print('After yielding {}'.format(item))

generator = list_generator([1,2,3,4,5,6,7,8])

for _ in range(5):
    print(next(generator))
"""

def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got: {}'.format(value))

        if not value: break
        total += value

generator = accumulator()

print(next(generator))

print('Accumulated: {}'.format(generator.send(1)))
print('Accumulated: {}'.format(generator.send(1)))
print('Accumulated: {}'.format(generator.send(1)))
print('Accumulated: {}'.format(generator.send(1)))
print(next(generator))
