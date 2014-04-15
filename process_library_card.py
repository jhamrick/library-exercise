file_handler = open("library-card.txt", "r")
file_contents = file_handler.read()
file_handler.close()

lines = file_contents.split("\n")

call_number = lines[0]
print "Call number: " + call_number

author = lines[1]
print "Author: " + author

title = lines[2]
print "Title: " + title

# the lines[3:] syntax selects the element
# at index 3 and every index afterwards
due_dates = lines[3:]
print "Due dates: " + str(due_dates)
#print "Due dates: ", due_dates






