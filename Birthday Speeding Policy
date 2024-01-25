def BirthdaySpeedingPolicy(speed, is_birthday):
    if is_birthday:
        speed -= 5

    if speed <= 60:
        return "No Ticket"
    elif speed <= 80:
        return "Small Ticket"
    else:
        return "Big Ticket"

# Test cases
print(BirthdaySpeedingPolicy(60, False))
print(BirthdaySpeedingPolicy(75, False))
print(BirthdaySpeedingPolicy(85, False))
print(BirthdaySpeedingPolicy(65, True))
print(BirthdaySpeedingPolicy(85, True))
