# author: Rafa Anargyrou

import math
import random

#set seed for random number generator
random.seed(1)

# establish parameters from the Poisson distribution for home and away goals
HOME_PARAM = 1.148698355
AWAY_PARAM = 0.8705505633

class Team:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
        self.pts = 0
        self.wins = 0
        self.draws = 0
        self.losses = 0
        self.gf = 0
        self.ga = 0
        self.gd = 0
    
def simulate_match(home, away):
    '''
    Simulate a match between home and away teams and return the score as a tuple
    parameters: home, away - Team objects
    returns: home_score, away_score - int
    '''
    skill_diff = (home.skill / 3 - away.skill / 3) # divide by 3 to make the difference more realistic
    return random_goals(skill_diff, HOME_PARAM), random_goals(skill_diff, AWAY_PARAM)

def random_goals(skill_diff, parameter):
    '''
    Gets a random number of goals from a Poisson distribution for a team with a given skill difference
    parameters: skill_diff - float, parameter - float
    returns: goals - int
    '''
    if skill_diff == 0:
        raise ValueError("Skill difference cannot be zero")
    goals = 0
    funct = parameter ** skill_diff
    x = random.random()
    while x > 0:
        x -= ((funct ** goals) * math.exp(-1 * funct)) / math.factorial(goals)
        goals += 1
    return goals - 1
     
def simulate_season(teams):
    '''
    Simulate a season of matches between all teams and modify the teams' attributes
    parameters: teams - list of Team objects
    '''
    for home in teams:
        print('-' * 35)
        print(home.name + "'s home games: ")
        print('-' * 35)
        for away in teams:
            if home != away:
                home_score, away_score = simulate_match(home, away)
                print(home.name, home_score, ":", away_score, away.name)
                home.gf += home_score
                away.gf += away_score
                home.ga += away_score
                away.ga += home_score
                home.gd += home_score - away_score
                away.gd += away_score - home_score
                if home_score == away_score:
                    home.draws += 1
                    away.draws += 1
                    home.pts += 1
                    away.pts += 1
                else:
                    winner, loser = (home, away) if (home_score > away_score) else (away, home)
                    winner.wins += 1
                    winner.pts += 3
                    loser.losses += 1
    
if __name__ == '__main__':
    teams = [
        Team('Flamengo', 20),
        Team('Palemiras', 19),
        Team('Atletico Mineiro', 18),
        Team('Sao Paulo', 17),
        Team('Corinthians', 16),
        Team('Bragantino', 15),
        Team('Fluminense', 14),
        Team('Internacional', 13),
        Team('Atletico Paranaense', 12),
        Team('America Mineiro', 11),
        Team('Santos', 10),
        Team('Fortaleza', 9),
        Team('Ceara', 8),
        Team('Cuiaba', 7),
        Team('Juventude', 6),
        Team('Atletico Goianiense', 5),
        Team('Botafogo', 4),
        Team('Coritiba', 3),
        Team('Goias', 2),
        Team('Avai', 1)
    ]

    for team in teams:
        print(team.name, team.skill)
    
    simulate_season(teams)

    print('-' * 115)
    print(f"| {'Team':^20} | {'Points':^10} | {'Wins':^10} | {'Draws':^10} | {'Losses':^10} | {'GF':^10} | {'GA':^10} | {'GD':^10} |")
    print('-' * 115)
    
    for team in sorted(teams, key=lambda team: team.pts, reverse=True):
        print(f'| {team.name:^20} | {team.pts:^10} | {team.wins:^10} | {team.draws:^10} | {team.losses:^10} | {team.gf:^10} | {team.ga:^10} | {team.gd:^10} |')
    print('-' * 115)
    