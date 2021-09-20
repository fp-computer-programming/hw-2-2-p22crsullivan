# Author: CRS 9/20/21
freeThrow = 1
basketInside = 2
basketBeyond = 3
freeThrowScored = 4
basketInsideScored = 4
basketBeyondScored = 4
totalScore = (freeThrow * freeThrowScored) + (basketBeyond * basketBeyondScored) + (basketInside * basketInsideScored)
print("The player scored " + str(totalScore) + " points.")
