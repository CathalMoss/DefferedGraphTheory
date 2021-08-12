# Deffered Graph Theory Project
import argparse


parser = argparse.ArgumentParser(description='Add a Regular expression and hit enter')
parser.add_argument('filepath', metavar='path', type=str,
                     help='Add filepath and hit enter')
args = parser.parse_args()


with open(args.filepath, 'r') as f:
   # for line in fileSearcher:
            #print(line)

# Words for txt file
#f = "input.txt"
#f = open (f, 'r')

#List in word file
 list = [] 

# # parse word file into individual words, sort, 
# # and then populate into word list
 for l in f:
     l = l.split() #individual words

     for w in l:
         list.append(w) # populate word list with words

 list.sort() #alphabetical order

 wd = {} #word dictionary for words and counts them

# # count words in word list and then populate dictionary
 for w in list:
     wd[w] =list.count(w)

# # print and format words and counts
 print('\n{:^8}{:^8}'.format('Word', 'Count'))

# # data is printed
 for w in wd:
     print('{:^8}{:^8d}'.format(w,wd[w]))
 print("")



# with open('test.txt', 'r') as rf:
#     with open('test_copy.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)

# with open('test.txt', 'r') as f:
    
    # for line in f:
    #     print(, end='')

    # size_to_read = 10

    # f_contents = f.read(size_to_read)
    # print(f_contents, end='')

    # f.seek(0)

    # f_contents = f.read(size_to_read)
    # print(f_contents)

    # while len(f_contents) > 0:
    #     print(f_contents, end='*')
    #     f_contents = f.read(size_to_read)


#name = name of test
# mode = r w a r+

# r = read
# w = write
# a = appending
# r+ = read and write
#f = open('test.txt', 'r')

# f_contents = f.read() = readsfile
#  f_contents = f.readlines() = reads all lines in order


# with open('test2.txt', 'w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('R')