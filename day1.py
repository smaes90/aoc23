import re

with open("data/day1.txt") as file:
    data = file.read().strip()


def calibration(data):
    lines = data.split("\n")
    numbers = [re.findall("\d", line) for line in lines]
    return sum(int(number[0] + number[-1]) for number in numbers)


# Part 1
print("deel 1: " + str(calibration(data)))

# Part 2
data = (
    data.replace("one", "one1one")
    .replace("two", "two2two")
    .replace("three", "three3three")
    .replace("four", "four4four")
    .replace("five", "five5five")
    .replace("six", "six6six")
    .replace("seven", "seven7seven")
    .replace("eight", "eight8eight")
    .replace("nine", "nine9nine")
)

print("deel 2:" + str(calibration(data)))