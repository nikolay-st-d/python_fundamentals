number_of_rooms = int(input())
total_free_chairs = 0
chairs_needed_in_room = False
for room in range(1, number_of_rooms + 1):
    room_list = input().split()
    chairs = len(room_list[0])
    people = int(room_list[1])
    if people > chairs:
        print(f"{people - chairs} more chairs needed in room {room}")
        chairs_needed_in_room = True
    else:
        total_free_chairs += chairs - people
if not chairs_needed_in_room:
    print(f"Game On, {total_free_chairs} free chairs left")