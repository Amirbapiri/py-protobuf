import enum_pb2

enum_message = enum_pb2.EnumMessage()
enum_message.id = 2345
enum_message.day_of_the_week = enum_pb2.MONDAY

print(enum_message.day_of_the_week)
print(enum_message.day_of_the_week == enum_pb2.THURSDAY)
