garbage_weight = [1.99, 1.01, 2.5, 1.5, 1.01]
max_bag = 3.0


def efficient_janitor(weight, bag_size):
    rounds = 0
    curr_bag = 0
    for w in weight:
        if curr_bag + w <= bag_size:
            curr_bag += w
        else:
            rounds += 1
            curr_bag = w
    if curr_bag > 0:
        rounds += 1

    return rounds


print(efficient_janitor(garbage_weight, max_bag))

#
# Balanced bracket problem