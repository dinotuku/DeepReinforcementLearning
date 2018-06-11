from game import Game
from funcs import playMatchesBetweenVersions
import loggers as lg

env = Game()
playMatchesBetweenVersions(
    env,
    '',  # the run version number where the computer player is located
    -1,  # the version number of the first player (-1 for human)
    5,  # the version number of the second player (-1 for human)
    10,  # how many games to play
    lg.logger_main,  # where to log the game to
    0,
    1  # which player to go first - 0 for random
)
