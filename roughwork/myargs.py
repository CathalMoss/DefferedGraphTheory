#! /usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                     help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                     const=sum, default=max,
                     help='sum the integers (default: find the max)')
# parser.add_argument('--help|-h', dest='help', action='help',
#                      help='Add integers and then type "--sum"')
                     

args = parser.parse_args()
print(args.accumulate(args.integers))

