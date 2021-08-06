import simple_pb2

simple_message = simple_pb2.SimpleMessage()
simple_message.id = 323
simple_message.is_simple = True
simple_message.name = "Amir"

simple_list = simple_message.sample_list
print(simple_list)
simple_list.append(20)
simple_list.append(10)
print(simple_list)

print(f"Message is whole is: {simple_message}")

with open("simple.bin", "wb") as file:
    print("Write as binary")
    bytes_as_string = simple_message.SerializeToString()
    file.write(bytes_as_string)

with open("simple.bin", "rb") as file:
    print("Read binary values")
    simple_message_data = simple_pb2.SimpleMessage().FromString(file.read())

print(simple_message_data)

print("Is simple: %s" % simple_message_data.is_simple)