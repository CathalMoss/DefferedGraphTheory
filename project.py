# Deffered Graph Theory Project

with open('test.txt', 'r') as f:
    
    # for line in f:
    #     print(, end='')

    size_to_read = 10

    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    f.seek(0)

    f_contents = f.read(size_to_read)
    print(f_contents)

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
