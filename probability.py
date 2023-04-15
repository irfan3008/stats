import math
#The probability that a student is accepted to a prestigeous college is 0.3. If 5 students from the same school apply, what is the probability that at most 2 are accepted?

# Probability of acceptance
p = 0.3

# Number of trials (students applying)
n = 5

# Probability of at most 2 being accepted
prob = 0
for i in range(3):
    # Calculate probability of i students being accepted
    comb = math.comb(n, i)
    prob_i = comb * (p ** i) * ((1 - p) ** (n - i))
    prob += prob_i

print("Probability of at most 2 students being accepted:", prob)


# What is the probability that the world series will last 4 games? 5 games? 6 games? 7 games? Assume that the teams are evenly matched.

import math

# Probability of winning a single game
p = 0.5

# Number of games in the series
n = 7

# Probability of World Series lasting i games
for i in range(4, n+1):
    # Calculate probability of i games being played
    comb = math.comb(n, i)
    prob_i = comb * (p ** i) * ((1 - p) ** (n - i))
    print("Probability of World Series lasting", i, "games:", prob_i)




# Bob is a high school basketball player. He is a 70% free throw shooter. That means his probability of making a free throw is 0.70. During the season, what is the probability that Bob makes his third free throw on his fifth shot?
import math
# Probability of making a free throw
p = 0.7
# Number of free throws attempted
n = 5
# Probability of making the third free throw on the fifth shot
comb = math.comb(n-1, 2) # number of combinations where the third free throw is made on the fifth shot
prob = comb * (p ** 3) * ((1 - p) ** 2)
print("Probability of making the third free throw on the fifth shot:", prob)

# Suppose we select 5 cards from an ordinary deck of playing cards. What is the probability of obtaining 2 or fewer hearts?

#using the hypergeometric distribution
import math
# Total number of cards in the deck
N = 52
# Number of hearts in the deck
n_hearts = 13
# Number of cards drawn
n_drawn = 5
# Number of ways to draw 2 or fewer hearts
n_ways = 0
for k in range(3):
    n_ways += math.comb(n_hearts, k) * math.comb(N - n_hearts, n_drawn - k)
# Total number of ways to draw 5 cards
n_total_ways = math.comb(N, n_drawn)

# Probability of obtaining 2 or fewer hearts
prob = n_ways / n_total_ways
print("Probability of obtaining 2 or fewer hearts:", prob)

# Multinomial Problems Example Probability
# Total number of cards in the deck
N = 52

# Number of cards to draw from each suit
n_spades = 1
n_hearts = 1
n_diamonds = 1
n_clubs = 2

# Total number of cards to draw
n_drawn = n_spades + n_hearts + n_diamonds + n_clubs

# Probability of drawing a spade
p_spade = 1 / 4

# Probability of drawing a heart
p_heart = 1 / 4

# Probability of drawing a diamond
p_diamond = 1 / 4

# Probability of drawing a club
p_club = 1 / 4

# Probability of drawing 1 spade, 1 heart, 1 diamond, and 2 clubs
prob = (p_spade ** n_spades) * (p_heart ** n_hearts) * (p_diamond ** n_diamonds) * (p_club ** n_clubs)

print("Probability of drawing 1 spade, 1 heart, 1 diamond, and 2 clubs:", prob)


# Poisson distribution
# The average number of homes sold by the Acme Realty company is 2 homes per day. What is the probability that exactly 3 homes will be sold tomorrow?
import math

# Average number of homes sold per day
lam = 2

# Number of homes sold tomorrow
k = 3

# Probability of selling k homes tomorrow
prob = (lam ** k) * math.exp(-lam) / math.factorial(k)

print("Probability of selling exactly 3 homes tomorrow:", prob)