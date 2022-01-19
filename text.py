for i in range(10):
    print(i, end="\n")

teams = ["Packers", "49ers", "Ravens", "Patriots"]
for index, team in enumerate(teams):
    print(index, team)

numbers = [1, 2, 3, 4, 5, 6]
even = [number for number in numbers if number%2 == 0]
print(even)
