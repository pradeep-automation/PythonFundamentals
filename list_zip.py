names = ['Peter Parker', 'Clare Kent', 'Wade WIlson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

for name, hero, universe in zip(names, heroes, universes):
    print(f"{name} is actually {hero} from {universe}")

"""Normal method"""
# for index, name in enumerate(names):
#     hero = heroes[index]
#     universe = universes[index]
#     print(f"{name} is actually {hero} from {universe}")

"""Basic method"""
# i = 0
# for name in names:
#
#     hero = heroes[i]
#     universe = universes[i]
#     print(f"{name} is actually {hero} from {universe}")
#     i += 1


"""+++++++++- Separate Code-- Unpacking """

a, _ = (1, 3)
print(_)


