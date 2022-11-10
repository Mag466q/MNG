
import csv
import re

publisher_location = []
publisher_name = []
publisher_year = []
no = []
vol = []
article_no = []
pages_in_range = []

separator = "$"
name_csv = "new.csv"

def fill_data(data):
    if data != None:
        return data.group()
    else:
        return "NUll"

def test(tab):
    good = 0
    bad = 0
    for data in tab:
        if data == " ":
            bad = bad + 1
        else:
            good = good + 1

    print(str(good) + "/" + str(len(tab)) + " " + str(bad))



def d_publisher_location(buff):
    publisher_location.append(fill_data(buff))



with open('details.csv', 'r', encoding="utf8") as file:
    reader = csv.reader(file)
    for row in reader:
        buff = re.search("(?P<publisher_location>[a-zA-Z-żźćńółęąśŻŹĆĄŚĘŁÓŃ]+\s)", row[0])
        d_publisher_location(buff)

        buff = re.search("(?P<publisher_name>([a-zA-Z-żźćńółęąśŻŹĆĄŚĘŁÓŃ]+\s)*([(]([A-Z])*[)]|[a-zA-Z-żźćńółęąśŻŹĆĄŚĘŁÓŃ]+)(,|(\s\\\)))",row[0])
        publisher_name.append(fill_data(buff))

        buff = re.search("(?P<publisher_year>\d\d\d\d)", row[0])
        publisher_year.append(fill_data(buff))

        buff = re.search("(?P<no>((nr|Nr)|(No|no)\.)\s\d{1,4})",row[1])
        no.append(fill_data(buff))  # bez iss.

        buff = re.search("(?P<vol>(vol|Vol)\.\s\d{1,3})",row[1])
        vol.append(fill_data(buff))

        buff = re.search("(?P<article_no>[e]+\d\d\d\d\d)",row[1])
        article_no.append(fill_data(buff))

        buff = re.search("(?P<pages_in_range>(S\.|s\.)\s\d{1,9}[-]\d{1,9})", row[1])
        pages_in_range.append(fill_data(buff))


test(publisher_location)
test(publisher_name)
test(publisher_year)
test(no)
test(vol)
test(article_no)
test(pages_in_range)



with open(name_csv,"w",encoding="utf8",newline="\n") as f:
    for val in range(0,700):
        f.write(publisher_location[val]+separator+
                publisher_name[val]+separator+
                publisher_year[val]+separator+
                no[val] +
                "\n")






