# brasileirao22-sim
Basic simulation of the Brazilian Soccer League for 2022 using Python

# Introduction
This simple Python project simulates the 2022 season of the Brasileirao using predctions made by [FiveThirtyEught](https://projects.fivethirtyeight.com/previsoes-de-futebol/brasileirao) in March 2022 prior to the start of the league. As a soccer entushiast, I made this project to visualize how FiveThirtyEught's inital predictions would serve as an estimator for the final league standings now that the season is over (by the time I made the initial code). Making this project allowed me to gain practical experience with some Python data structures and concepts. During this process, I familiarized myself with Virtual Studio Code and git. Drawing influence from other projects, I expanded my knowledge in programming with Python. I hope you enjoy it!

# Technologies Used:
- Python 3
- Visual Studio Code

# Setup:
This program was crafted using VSCode and can be run in any Python interpreter (although I recommend sticking to VScode). The inital simulator uses the Poisson distribution to randomly assign multipliers for home and away times when generating their scores for a match. After generating all combinations of matches for all 20 clubs, the program prints all expected match results and the final standings for the season. 

# Status:
In the near future I hope to implement a support mechanism to this program where the use can input their team of support and the program would output information specific to that team such as a specific match result or their position on th efinal table. Additionaly, I would like to expand this project to accept data files for alternative leagues (containing some source of skill variable) and predict their output accordingly.