#Bytes
#b-літерал для оголошення байтової стрічки

example_bytes = b'hello'
print(type(example_bytes))

for element in example_bytes:
    print(element)

#example_bytes = b"Привіт"
example_string = 'Привіт'
print(type(example_string))
print(example_string)

encoded_string = example_string.encode(encoding="utf-8")
print(encoded_string)
print(type(encoded_string))

decoded_string = encoded_string.decode()
print(decoded_string)
