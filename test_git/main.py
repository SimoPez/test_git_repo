import argparse
import time
from test_git_utils.verso import verso

if __name__ == '__main__':

    print('Hellooo')

    parser = argparse.ArgumentParser()
    parser.add_argument("-cnt", "--count")
    args = parser.parse_args()

    to_print = ''
    for c in range(2*int(args.count)):
        to_print = to_print + verso() + '\n'
    
    while True:
        print(verso())
        time.sleep(12)
