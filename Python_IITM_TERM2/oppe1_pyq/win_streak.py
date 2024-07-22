# function for win streak. Return lax len of win streak
# runs = [150, 10, 20, 120, 100, 88, 120, 100, 115]


def win_streak(runs: list):
    max_streak = 0
    current_streak = 0

    for run in runs:
        if run >= 100:
            current_streak += 1
        else:
            if current_streak > max_streak:
                max_streak = current_streak
            current_streak = 0

    # in case the last match is also in a win streak
    if current_streak > max_streak:
        max_streak = current_streak

    return max_streak


print(win_streak([150, 10, 20, 120, 100, 88, 120, 101, 115, 120]))
