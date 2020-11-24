import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", type=int,
                    help="display a square of a given numbers")
parser.add_argument("-v", "--verbose", type=int, choices = [0, 1, 2],
                    help="Increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose == 2:
    print("verbosity turned on")
    print("the square of {} equals {}".format(args.square, answer))
elif args.verbose == 1:
    print('{}^2 == {}'.format(args.square, answer))
else:
    print("there is no place for verbosity")
    print(answer)
