payouts = {
    6: 10000,
    7: 36,
    8: 720,
    9: 360,
    10: 80,
    11: 252,
    12: 108,
    13: 72,
    14: 54,
    15: 180,
    16: 72,
    17: 180,
    18: 119,
    19: 36,
    20: 306,
    21: 1080,
    22: 144,
    23: 1800,
    24: 3600
}

ordered_payouts = sorted(payouts.items(), key=lambda item: item[1], reverse=True)

def possible_values(three_number_sequence, possible_numbers):
    known_numbers = [n for n in three_number_sequence if n]
    num_unknown_numbers = len(three_number_sequence) - len(known_numbers)
    combos = [(n,) for n in possible_numbers]
    while num_unknown_numbers > 1:
        combos = [t + (n,) for n in possible_numbers for t in combos if n not in t]
        num_unknown_numbers -= 1
    return set([tuple(sorted(list(tup) + known_numbers)) for tup in combos])

def calculate_max_payout_rank(three_number_sequence, known_numbers):
    possible_numbers = [n for n in range(1, 10) if n not in known_numbers]
    possible_completes = possible_values(three_number_sequence, possible_numbers)
    possible_sums = {sum(c): c for c in possible_completes}
    for i, (target, payout) in enumerate(ordered_payouts):
        if target in possible_sums:
            return i, target, payout, possible_sums[target]

def calculate_sums(grid):
    known_numbers = [n for row in grid for n in row if n]
    results = []
    for row in grid:
        results.append(calculate_max_payout_rank(row, known_numbers))
    for n in range(len(grid[0])):
        col = [row[n] for row in grid]
        results.append(calculate_max_payout_rank(col, known_numbers))
    results.append(calculate_max_payout_rank([grid[0][0], grid[1][1], grid[2][2]], known_numbers))
    results.append(calculate_max_payout_rank([grid[0][2], grid[1][1], grid[2][0]], known_numbers))
    
    best_guess = min(results, key=lambda item: item[0])

    position_lookup = {
        0: 'Row 1',
        1: 'Row 2', 
        2: 'Row 3',
        3: 'Column 1', 
        4: 'Column 2',
        5: 'Column 3',
        6: 'Diagonal top right to bottom left',
        7: 'Diagonal bottom right to top left'
    }

    position = results.index(best_guess)

    for row in grid:
        print(row)
    print('Best guess is {}'.format(position_lookup[position]))
    print('Possible sum of {}, made by {}'.format(best_guess[1], best_guess[3]))
    print('Possible payout of {}'.format(best_guess[2]))


if __name__=="__main__":
    grid = [
        [0, 0, 9],
        [2, 1, 4],
        [0, 0, 0]
    ]
    calculate_sums(grid)



