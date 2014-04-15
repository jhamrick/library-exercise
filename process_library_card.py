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
#print "Due dates: " + str(due_dates)
#print "Due dates: ", due_dates

for date in due_dates:
	date_parts = date.split()
	month = date_parts[0]
	day = date_parts[1]
	year = date_parts[2]
	
	print "-" # this is a separator
	print "Month: " + month
	print "Day: " + day
	print "Year: " + year
	
	if year.startswith("'"):
		new_year = "19" + year[1:]
	else:
		new_year = year
		
	print "New year: " + new_year
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	






