#! python3
# template-creator.py - Creates basic template for Jekyll post
import sys
from datetime import date

if (len(sys.argv) < 2):
    print ('Missing title argument. EX: python template-creator.py "Here is my title"')
    exit()

# Parse and format input title name
title = sys.argv[1]
formattedTitle = title.lower()
formattedTitle = formattedTitle.replace(" ", "-")
formattedTitle = formattedTitle.replace("!", "")
formattedTitle = formattedTitle.replace(",", "")
formattedTitle = formattedTitle.replace(":", "")


print ('Creating post template for ' + title + '...')

# Create date portion of title
today = date.today()
titleDate = today.strftime("%Y-%m-%d")

postName = titleDate + '-' + formattedTitle

# Create file
f = open("_posts/" + postName + ".md", "a")
f.write("---\n")
f.write("layout: post\n")
f.write("title: '" + title + "'\n")
f.write("---\n")
f.write("\n-- Content goes here --")
f.close()

print ('Post: ' + postName + " has been created")
