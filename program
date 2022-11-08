import csv
import re

ublisher_location = []
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
        return "NULL"


def test(tab):
    good = 0
    bad = 0
    for data in tab:
        if data == "NULL":
            bad = bad + 1
        else:
            good = good + 1

    print(str(good) + "/" + str(len(tab)) + " " + str(bad))


with open('details.csv', 'r', encoding="utf8") as file:
    reader = csv.reader(file)
    for row in reader:
        x = re.search("(?P<ublisher_location>[a-zA-Z-żźćńółęąśŻŹĆĄŚĘŁÓŃ]+\s)", row[0])
        y = re.search("(?P<publisher_name>([a-zA-Z-żźćńółęąśŻŹĆĄŚĘŁÓŃ]+\s)*([(]([A-Z])*[)]|[a-zA-Z-żźćńółęąśŻŹĆĄŚĘŁÓŃ]+)(,|(\s\\\)))",row[0])
        z = re.search("(?P<publisher_year>\d\d\d\d)", row[0])
        v = re.search("(?P<no>((nr|Nr)|(No|no)\.)\s\d{1,4})",row[1])
        t = re.search("(?P<vol>(vol|Vol)\.\s\d{1,3})",row[1])
        u = re.search("(?P<article_no>[e]+\d\d\d\d\d)",row[1])
        h = re.search("(?P<pages_in_range>(S\.|s\.)\s\d{1,9}[-]\d{1,9})",row[1])
        ublisher_location.append(fill_data(x))
        publisher_name.append(fill_data(y))
        publisher_year.append(fill_data(z))
        no.append(fill_data(v)) #bez iss.
        vol.append(fill_data(t))
        article_no.append(fill_data(u))
        pages_in_range.append(fill_data(h))



test(ublisher_location)
test(publisher_name)
test(publisher_year)
test(no)
test(vol)
test(article_no)
test(pages_in_range)
print(ublisher_location)

with open(name_csv,"w",encoding="utf8",newline="\n") as f:
    writer =csv.writer(f)
    writer.writerow(ublisher_location)
