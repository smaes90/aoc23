# Read input file
with open("data/day2.txt", "r") as file:
    lines = file.readlines()

constants = {
    'red': 12,
    'green': 13,
    'blue': 14
}

games_played = {}
game_sets = {}
solution_part1 = []
solution_part2 = []

def parse_value(value):
    parts = value.split()
    count = int(parts[0])
    color = parts[1]
    return count, color

def is_valid_cube_counts(counts, max_counts):
    for color, count in counts.items():
        if count > max_counts[color]:
            return False
    return True

for line in lines:
    game = line.split(':')
    game_number = game[0].replace('Game ', '')
    game_results = game[1].split(';')
    result_list = []

    for result in game_results:
        result_list.append(result.strip('\n'))

    games_played[game_number] = result_list

for key, game_results in games_played.items():
    red_check = True
    green_check = True
    blue_check = True
    set_constructor = {'red': [], 'green': [], 'blue': []}

    for item in game_results:
        item_values = item.split(',')

        for value in item_values:
            count, color = parse_value(value.strip())
            set_constructor[color].append(count)

    game_sets[key] = set_constructor

    cube_counts = {'red': max(set_constructor['red']),
                   'green': max(set_constructor['green']),
                   'blue': max(set_constructor['blue'])}

    if not is_valid_cube_counts(cube_counts, constants):
        red_check = green_check = blue_check = False

    if red_check and green_check and blue_check:
        solution_part1.append(int(key))

print("Part 1 solution:", sum(solution_part1))

for key, item in game_sets.items():
    cube_power = max(item['red']) * max(item['green']) * max(item['blue'])
    solution_part2.append(cube_power)

print("Part 2 solution:", sum(solution_part2))
