import argparse
from test_git_utils.verso import verso

if __name__ == 'main':

    parser = argparse.ArgumentParser()
    parser.add_argument("-cnt", "--count")
    args = parser.parse_args()

    for c in int(args.count):
        print(verso())