import csv
import re

separator = "$"
name_csv = "new.csv"

publisher_location = []
publisher_name = []
publisher_year = []
no = []
vol = []
article_no = []
pages_in_range = []

def fill_data(data:object) -> str:
    if data != None:
        return data.group()
    else:
        return " "

def re_publisher_location(row:str):
    buff = re.search("(?P<publisher_location>[a-zA-Z-żéźćńółęąśŻŹĆĄŚĘŁÓŃ]+\s)", row)
    publisher_location.append(fill_data(buff))


def re_publisher_name(row:str):
    buff = re.search("(?P<publisher_name>([a-zA-Z-żéźćńółęąśŻŹĆĄŚĘŁÓŃ]+\s)*([(]([A-Z])*[)]|[a-zA-Z-éżźćńółęąśŻŹĆĄŚĘŁÓŃ]+)(,|(\s\\\)))",row)
    publisher_name.append(fill_data(buff))

def re_no(row:str):
    buff = re.search("(?P<no>((nr|Nr)|(No|no)\.)\s\d{1,4})", row)
    no.append(fill_data(buff))


def re_publisher_year(row:str):
    buff = re.search("(?P<publisher_year>\d\d\d\d)", row)
    publisher_year.append(fill_data(buff))


def re_vol(row:str):
    buff = re.search("(?P<vol>(vol|Vol)\.\s\d{1,3})", row)
    vol.append(fill_data(buff))


def re_article_no(row:str):
    buff = re.search("(?P<article_no>[e]+\d\d\d\d\d)", row)
    article_no.append(fill_data(buff))


def re_pages_in_range(row:str):
    buff = re.search("(?P<pages_in_range>(S\.|s\.)\s\d{1,9}[-]\d{1,9})", row)
    pages_in_range.append(fill_data(buff))


def clear():

    buffer = publisher_name.copy()
    publisher_name.clear()
    for buff in buffer :
        publisher_name.append((buff[:-1]))
    buffer.clear()

    buffer = no.copy()
    no.clear()
    for buff in buffer:
        data_filter = re.search("\d{1,4}",buff)
        no.append(fill_data(data_filter))
    buffer.clear()

    buffer = vol.copy()
    vol.clear()
    for buff in buffer:
        data_filter = re.search("\d{1,3}",buff)
        vol.append(fill_data(data_filter))
    buffer.clear()

    buffer = pages_in_range.copy()
    pages_in_range.clear()
    for buff in buffer:
        data_filter = re.search("\d{1,9}[-]\d{1,9}", buff)
        pages_in_range.append(fill_data(data_filter))
    buffer.clear()


with open('details.csv', 'r', encoding="utf8") as file:
    reader = csv.reader(file)
    for row in reader:
        re_publisher_location(row[0])
        re_publisher_name(row[0])
        re_publisher_year(row[0])
        re_no(row[1])
        re_vol(row[1])
        re_article_no(row[1])
        re_pages_in_range(row[1])
    file.close()
clear()

with open(name_csv,"w",encoding="utf8",newline="\n") as file:
    file.write("no" + separator + "vol" + separator + "article_no" + separator + "pages_in_range" + separator + "publisher_name" + separator + "publisher_location" + separator + "publisher_year" + "\n")
    for val in range(0,700):
        file.write(
                   no[val] + separator +
                   vol[val] + separator +
                   article_no[val] + separator +
                   pages_in_range[val] + separator +
                   publisher_name[val] + separator +
                   publisher_location[val] + separator +
                   publisher_year[val]+
                "\n")





