#!/usr/local/bin/python3

def simulate(x_vel, y_vel):
    global best_max_y

    x = 0
    y = 0
    max_y = 0

    while True:
        x += x_vel
        y += y_vel
        if x_vel > 0: x_vel -= 1
        if x_vel < 0: x_vel += 1
        y_vel -= 1

        max_y = max(y, max_y)

        if y_vel < 0 and y < target_y_min:
            return False
        if x >= target_x_min and x <= target_x_max and y >= target_y_min and y <= target_y_max:
            best_max_y = max(max_y, best_max_y)
            return True

# target_x_min = 20
# target_x_max = 30
# target_y_min = -10
# target_y_max = -5
target_x_min = 192
target_x_max = 251
target_y_min = -89
target_y_max = -59

best_max_y = 0
successful_shots = 0

for x_vel in range(0, 300):
    for y_vel in range(-300, 300):
        success = simulate(x_vel, y_vel)
        if success:
            successful_shots += 1

print("best_max_y", best_max_y)
print("successful_shots", successful_shots)
