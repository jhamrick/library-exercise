# "Library Card" Exercise

At the Software Carpentry bootcamp for librarians at PyCon 2014, I
found
[an image of an old library catalogue card](http://2.bp.blogspot.com/-6VxNTXpOnoc/URh4RVpm6wI/AAAAAAAAPEQ/c6mhrcTgEiw/s1600/duedate.jpg)
which has nearly illegible dates, partially out of order, and in
varying formats. I transcribed this by hand into
[library-card.txt](library-card.txt), and also created a more
difficult version of the same data in
[library-card-hard.txt](library-card.txt). I then walked the class
through the exercise of writing a script to load the data into Python,
parse it, and convert it to a more consistent and useful format. We
interspersed writing the script with learning about git, and making
periodic git commits to save our progress.

This exercise proved to be really successful for several reasons: it
tied together all the building block concepts we had gone over the day
before; it provided a realistic setting for learning version control;
and it resulted in a legitimately useful program that the students had
written.

## Steps

We went through the following steps. In general, I tried to take the
approach of telling the class what we should do next at a conceptual
level (I occasionally asked them this as well), and then asking them
how I should actually write the code to do it.

After each of the steps below, we would make a git commit.

1. Load the data into Python using `open` and `read`. I opted to write
   the script without a function and without `if __name__ ==
   "__main__"` because, while technically good style, I think it would
   have mostly just caused people to have issues with
   indentation/whitespace and thus distract from the actual writing of
   code.

   Split the file contents into lines with `split`. Read out the first
   three lines and save them into variables `call_number`, `author`,
   and `title`, respectively, and print them out.

   Isolate the lines with dates on them using list slicing. We hadn't
   really talked about slicing lists at this point, so this was a bit
   confusing for some people.

2. Write a for loop to process each date in the list of dates. We
   started the for loop just printing out each date (not actually
   doing any processing). Then, we used `split` again to split each
   date into `month`, `day`, and `year`, and print out the values.

3. Handle years that were in a format like '59. Ask the class to
   brainstorm how to do this, get multiple responses, and then talk
   about how there are multiple ways you could do this and provide
   tips on how to decide which way to use (e.g., if you can think of a
   way that seems to use fewer edge cases, use that).

4. Handle years that were in a format like 59. Assume everything else
   is formatted correctly, and add an assert statement to verify that
   the correclty formatted year is of length 4. Talk about why we
   would want to use assert statements (e.g., maybe there was a year
   format that we didn't realize).

5. Convert three-letter month names to integers. This required
   introducting the `index` method of lists.

6. Combine the processed month, day, and year into a date format like
   1959-07-13, and append the new date to a list called
   `clean_data`. Write the original `call_number`, `author`, and
   `title` to the first three lines of a new file. Create another for
   loop, and write all the dates in `clean_data` to the file as well.

## Thoughts

Here are some of my thoughts about what worked and what we could have
done differently.

* Some students with older versions of OS X had trouble with git. We
  should have probably tried to make sure everyone had git installed
  earlier on.

* If I were to redo this lesson, I would probably process years like
  59 before years like '59.

* I forgot to append the processed dates to a list at first, but I
  think this was actually a good mistake to make, because it
  demonstrated that even experience programmers aren't perfect, and
  that coding can be somewhat nonlinear.

* While we were working on writing the cleaned data out to file, a few
  of the students accidentally opened a file handler for the
  *original* data file and overwrote it, meaning that the next time
  they ran their script, they got an error. This was a great teaching
  moment for the value of git: we actually had the whole class
  overwrite their data files, and then had everybody use `git
  checkout` to revert the changes. However, we didn't undo the change
  to the script (so it wouldn't overwrite the file anymore) soon
  enough, and some people overwrote their data file a second time, so
  it would be good to remember to do this in the future.

* If there were more time, I would have had them write the script to
  take a command line argument of the name of the file to process. We
  covered command line arguments the day before, so I don't think this
  would have been difficult (we just ran out of time).
