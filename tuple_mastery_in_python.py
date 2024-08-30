# Task 1

flight_info = [
    ("Harry", "New York", "California"),
    ("Jerry", "California", "Seattle"),
    ("Hailey", "Seattle", "Florida")
]

def flight_format(flight_info):
    flight_counter = 1
    for i in flight_info:
        print(f"Itinerary {flight_counter} - {i[0]} From {i[1]} to {i[2]}")
        flight_counter += 1


flight_format(flight_info)