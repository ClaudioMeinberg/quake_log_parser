import argparse

from parsers.task1 import parse_game_kills
from parsers.task2 import report
from parsers.utils import jsonify

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Parse log file of quake game matches')
    parser.add_argument('-f', '--logfile',
                        dest='logfile',
                        metavar='logfile',
                        action='store',
                        help='your logfile fullpath',
                        required=True)

    parser.add_argument('-r', dest='report', action='store_true',
                        help='print report on finish')

    parser.add_argument('-v', dest='verbose', action='store_true',
                        help='verbose mode')

    args = parser.parse_args()
    game_matches = parse_game_kills(args.logfile)

    if args.verbose:
        games_json = jsonify(game_matches)
        print(games_json)

    if args.report:
        print(report(game_matches))
