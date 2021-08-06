import complex_pb2

complex_message = complex_pb2.ComplexMessage()

# Create a dummy_message
complex_message.one_dummy.id = 1
complex_message.one_dummy.name = "Dummy Message #1"

# First way of appending
first_multiple_dummy = complex_message.multiple_dummy.add()
first_multiple_dummy.id = 345
first_multiple_dummy.name = "Multiple Dummary Message #1"

# Second way of appending
complex_message.multiple_dummy.add(id=56, name="Second way of adding new multiple message")

dummy_message = complex_pb2.DummyMessage()
dummy_message.id = 2020
dummy_message.name = "I hope this way works."

# A copy of 'DummyMessage' going to be passed to the .extend
complex_message.multiple_dummy.extend([dummy_message])
dummy_message.name = "Hope is not good!"

print(dummy_message)
print(complex_message)