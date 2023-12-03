#! /usr/bin/env python3

from argparse import ArgumentParser
import re

def get_number(line):
    """
    Get a two-digit number from first and last digits present in line
    :param line:
    :return:
    """
    l = []
    # Preprocess digit names
    # overlapping cases first
    line = re.sub('zerone', '01', line)
    line = re.sub('oneight', '18', line)
    line = re.sub('twone', '21', line)
    line = re.sub('threeight', '38', line)
    line = re.sub('fiveight', '58', line)
    line = re.sub('sevenine', '79', line)
    line = re.sub('eightwo', '82', line)
    line = re.sub('eighthree', '83', line)
    line = re.sub('nineight', '98', line)
    print(line)
    names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
             'eight', 'nine']
    for digit, name in enumerate(names):
        line = re.sub(name, str(digit), line)
    for i in line:
        if i in '1234567890':
            l.append(i)
    print(line, l)
    print('---')
    # if len(l) >= 2:
    return 10 * int(l[0]) + int(l[-1])
    # else:
    #     return int(l[0])


parser = ArgumentParser('AOC task 1/1')
parser.add_argument('-f', type=str, help='Input file')
args = parser.parse_args()

print(sum(get_number(x) for x in open(args.f)))
