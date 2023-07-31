# managing files data - write append(create a new data and file) - read(read excisting data
# files data in two modes - text mode and binary mode
# three main commands - 'w' to write - 'a' to append data to existing file - 'r' - to read data
# synatx : f = open('path', 'mode')
# f is the name of variable storing operation data
# open is the command to work on data in file
# path is the path of file on which we work
# mode - r,w,a for text data and rb,wb,ab or image data all in single quotes
# when w is used it first checks for existing path if yes open that file and performs operation on it
# if not exist - points to start position of the file
# and each mode has some methods those can be used with variable used for storing operation content
# \n for new line

f = open('first_file','w')
f.write('learning python from telusko yt channel')
f.write('\ncomplete all the videos')
f.write('\nthis is the lesson on file handling')
f.write("\nTextIOWrapper.write() takes no keyword arguments,")
f.write("\nthis methods belong to TextIOWrapper class")
# print(f)
# for e in f:
#     print(e)

f = open('first_file','r')
for e in f:
    print(e)
f = open('first_file','a')
f.write("\n for printing in cose we have to open the file in read mode.. write mode cannot print data in console")
f1 = open('second_file','a')
f1.write("this is the second line but I am trying to write this file with append directly will check if it works")
f1.write("\nyes it worked and it created new file with the path I gave")
f1.write("\n we have to open the file in read mode to do read cannot write in w and a modes")
f1.write('\n but can write using a and w modes')
# copying file
f3 = open("third_file",'w')
f3.write("\nthis file is created to copy contents of firat and second files")
f3.write('\nto copy first we have to open file we cant to copy in read mode and read all of it and then write to another file')

f1 = open('second_file','r')
for e in f1 : # copying content from from f1
    print(e)

f3 = open("third_file",'w')
f3.write("\n to copy of one file to other we have to open one file in read mode other file in write mode")
for e in f1:
    f3.write(e)
    print(e)

