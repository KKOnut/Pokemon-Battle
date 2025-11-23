from snails import Snail

first_snail = Snail("Liza", 0.3, 0)
second_snail = Snail("Azil", 0.4, 0)

iter = 0
while True:
    first_snail.move()
    second_snail.move()

    iter += 1
    print(f"Turn - {iter}")
    print(f'{first_snail.name:<5}: {(first_snail.distance)}')
    print(f'{second_snail.name:<5}: {(second_snail.distance)}')
    print()
    
    if first_snail.distance >= 10:
        print(f"The winner is {first_snail.name}")
        break

    if second_snail.distance >= 10:
        print(f"The winner is {second_snail.name}")
        break