import unittest
import csv
import os
import main
TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'details.csv')
TESTDATA_FILENAME1 = os.path.join(os.path.dirname(__file__), 'new.csv')

class MyTestCase(unittest.TestCase):

    def setUp(self):

        self.size=0
        with open(TESTDATA_FILENAME,"r",encoding='utf8')as self.file:
            reader = csv.reader(self.file)
            for row in reader:
                self.size=self.size+1

        self.tested_row=[]
        with open(TESTDATA_FILENAME1, 'r',encoding='utf8') as self.csv_file:
            reader = csv.reader(self.csv_file,delimiter="$")
            next(reader)
            for row in reader:
                self.tested_row.append(row)

    def tearDown(self):
        self.file.close()
        self.csv_file.close()

    def test_re_no(self):
        for dana in range(0,700):
            self.assertEqual((self.tested_row[dana][0]),main.no[dana])

    def test_re_vol(self):
        for dana in range(0, 700):
            self.assertEqual((self.tested_row[dana][1]), main.vol[dana])

    def test_re_article_no(self):
        for dana in range(0,700):
            self.assertEqual((self.tested_row[dana][2]),main.article_no[dana])

    def test_re_pages_in_range(self):
        for dana in range(0, 700):
            self.assertEqual((self.tested_row[dana][3]), main.pages_in_range[dana])

    def test_re_publisher_name(self):
        for dana in range(0, 700):
            self.assertEqual((self.tested_row[dana][4]), main.publisher_name[dana])

    def test_re_publisher_location(self):
        for dana in range(0, 700):
            self.assertEqual((self.tested_row[dana][5]), main.publisher_location[dana])
    def test_re_publisher_year(self):
        for dana in range(0, 700):
            self.assertEqual((self.tested_row[dana][6]), main.publisher_year[dana])

    def test_size_publisher_location(self):
        self.assertEqual(len(main.publisher_location), self.size)

    def test_size_publisher_name(self):
        self.assertEqual(len(main.publisher_name), self.size)

    def test_size_publisher_year(self):
        self.assertEqual(len(main.publisher_year), self.size)

    def test_size_no(self):
        self.assertEqual(len(main.no), self.size)

    def test_size__article_no(self):
        self.assertEqual(len(main.article_no), self.size)

    def test_size__pages_in_range(self):
        self.assertEqual(len(main.pages_in_range), self.size)

    def test_size__vol(self):
        self.assertEqual(len(main.vol), self.size)



if __name__ == '__main__':
    unittest.main()
