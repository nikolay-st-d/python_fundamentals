all_users = {}
number_of_commands = int(input())
for _ in range(number_of_commands):
    data_list = input().split()
    if data_list[0] == 'register':
        user_name = data_list[1]
        license_plate = data_list[2]
        if user_name not in all_users.keys():
            all_users[user_name] = license_plate
            print(f"{user_name} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate}")
    elif data_list[0] == 'unregister':
        user_name = data_list[1]
        if user_name not in all_users.keys():
            print(f"ERROR: user {user_name} not found")
        else:
            del all_users[user_name]
            print(f"{user_name} unregistered successfully")

for username, license_plate_number in all_users.items():
    print(f"{username} => {license_plate_number}")