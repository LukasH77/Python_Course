#solution to https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def not_right():
#     if front_is_clear():
#         move()
#     else:
#         turn_left()
#
#
# steps = 0
# sum = 0
# while not at_goal():
#     if steps == 4:
#         steps = 0
#         if sum == 4:
#             sum = 0
#             not_right()
#
#     if right_is_clear():
#         turn_right()
#         move()
#         sum += 1
#     else:
#         not_right()
#
#     steps += 1
