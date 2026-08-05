import argparse
from test_git_utils.verso import verso

if __name__ == 'main':

    parser = argparse.ArgumentParser()
    parser.add_argument("-cnt", "--count")
    args = parser.parse_args()

    to_print = ''
    for c in int(args.count):
        to_print = to_print + verso() + '\n'
    
    with open('../versi.txt', 'w') as f:
        f.write(to_print)
