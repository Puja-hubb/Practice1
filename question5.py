seats = [
    "Available",
    "Booked",
    "Available",
    "Available",
    "Booked",
    "Available",
    "Booked",
    "Available"
]

for i in range(len(seats)):
    print("Seat", i + 1, ":", seats[i])

seat_number = int(input())

index = seat_number - 1

if seats[index] == "Available":
    seats[index] = "Booked"
    print("Seat booked successfully.")
else:
    print("Seat is already booked.")

total_seats = len(seats)
booked_seats = seats.count("Booked")
available_seats = seats.count("Available")

print("Total Seats:", total_seats)
print("Booked Seats:", booked_seats)
print("Available Seats:", available_seats)