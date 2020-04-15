import json

def to_json(func):
    def wrapped(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapped


@to_json
def get_data():
  return {
    'data': 42
  }

print(type(get_data()))  # вернёт '{"data": 42}'
