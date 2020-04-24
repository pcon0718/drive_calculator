# Retreive input from users
drive_size = input("Drive size (in TB): ")
drive_quantity = input("Drive quantity: ")
drive_cost = input("Drive cost (in USD): ")

# Convert strings into integers and float
drive_size = float(drive_size)
drive_cost = float(drive_cost)
drive_quantity = int(drive_quantity)

# Do some calculations
cost_tb = drive_cost / drive_quantity
cost_tb = round(cost_tb, 2)
usable_space = drive_quantity * drive_size

# Print out the results
print(f"You will have {usable_space} TB of usable space at ${cost_tb} per TB.")