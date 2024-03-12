

def badge_maker(name):
    return "Hello, my name is {}.".format(name)

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(speakers):
    return ["Hello, {}! You'll be assigned to room {}!".format(speaker, index + 1) for index, speaker in enumerate(speakers)]

def printer(names):
    badges = batch_badge_creator(names)
    room_assignments = assign_rooms(names)
    
    for badge in badges:
        print(badge)
    for assignment in room_assignments:
        print(assignment)
