# Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

# For example: ["3:1", "2:2", "0:1", ...]

# Points are awarded for each match as follows:

# if x > y: 3 points (win)
# if x < y: 0 points (loss)
# if x = y: 1 point (tie)
# We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

# Notes:

# our team always plays 10 matches in the championship
# 0 <= x <= 4
# 0 <= y <= 4


#steps
# define a function that takes in a list
# create some varibles for scores
# loop through list given to make a comparison (we can index or use the .split method)
# check for the conditions listed above
# return our teams score (total)

def solution(scores):
    home_team = 0
    for game in scores:
        x = int(game[0])
        y = int(game[2])
        if x > y:
            home_team += 3
        elif x == y:
            home_team += 1
    return home_team
