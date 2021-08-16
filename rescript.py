# Deffered Graph Theory Project
import argparse

#counter for matches
counter = 0

# agsparse inserted for to read in filepath and have -h/--help options
parser = argparse.ArgumentParser(description='Add a Regular expression and a filepath')
parser.add_argument('firstcommand', metavar='path', type=str,
                     help='Add a regular expression, hit space and then ...')
parser.add_argument('filepath', metavar='path', type=str,
                     help='... add filepath and hit enter')
args = parser.parse_args()

#filepath opener using argparse
with open(args.filepath, 'r', encoding='utf-8') as f:
    for l in f:
        if args.firstcommand in l:
            counter+=1
            #List in word file
            list = []

            # # # parse word file into individual words, sort,
            # # # and then populate into word list
            l = l.split() #individual words

            for w in l:
                list.append(w) # populate word list with words

            list.sort() #alphabetical order

            wd = {} #word dictionary for words and counts them

            # #count words in word list and then populate dictionary
            for w in list:
                wd[w] =list.count(w)

            # # # print and format words and counts
            print('\n{:^8}{:^8}'.format('Word', 'Count'))

            # # # data is printed
            for w in wd:
                print('{:^8}{:^8d}'.format(w,wd[w]))

    print(f"\nCounter:  {counter}")