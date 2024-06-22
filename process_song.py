import csv
import os
import unittest


def get_dict_list(filename):

    # create the list of dictionaries
    d_list = []

    # open the file as a csv file
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, filename)
    with open(filename,'r') as f:
        csv_reader = csv.reader(f)

        # read the headers
        headers = next(csv_reader)

        # loop through the rows
        for row in csv_reader:
            d = {}
            for i in range(5):
                d[headers[i]] = row[i]
            d_list.append(d)

        return d_list


def top_five_year(d_list):
    """return a list of tuples for the top five years
    based on the number of songs from
    that year
    """
    d_out = {}
    for d in d_list:
        year = d.get("year", 0)
        d_out[year] = d_out.get(year, 0) + 1
    top = sorted(d_out.items(), key=lambda t: t[1],reverse=True)
    return top[:5]


def top_five_artist(d_list):
    """return a list of tuples for the top five artists
    based on the number of songs in the list
    """
    d_out={}
    for dic in d_list:
        d_out[dic['artist']]=d_out.get(dic['artist'],0)+1
    return sorted(d_out.items(),key= lambda dic:dic[1],reverse=True)[:5]    


def top_five_decade(d_list):
    """return a list of tuples for the top five decades
    (40, 50, 60, etc) based on the number of songs from
    that decade
    """

    d_out={}
    for dic in d_list:
        d_out[dic['year'][-2]+"0"]=d_out.get(dic['year'][-2]+"0",0)+1
    return sorted(d_out.items(),key= lambda dic:dic[1],reverse=True)[:5]    



def top_five_album(d_list):
    """return a list of tuples for the top file albums
    based on the number of songs from that album
    """
    d_out={}
    for dic in d_list:
        if dic['album']!='':
            d_out[dic['album']]=d_out.get(dic['album'],0)+1        
    return sorted(d_out.items(),key= lambda dic:dic[1],reverse=True)[:5]


class TestAllMethods(unittest.TestCase):


    def setUp(self):
        self.d = get_dict_list("Top500Songs.csv")

    def test_top_five_year(self):
        t = top_five_year(self.d)
        self.assertEqual(
            t,
            [("1965", 38), ("1966", 28), ("1967", 26), ("1968", 23), ("1969", 23)],
            "test of top_five_year",
        )

    def test_top_five_artist(self):
        t = top_five_artist(self.d)
        self.assertEqual(
            t,
            [
                ("The Beatles", 23),
                ("The Rolling Stones", 14),
                ("Bob Dylan", 13),
                ("Elvis Presley", 11),
                ("U2", 8),
            ],
            "test of top_five_artist",
        )

    def test_top_five_decade(self):
        t = top_five_decade(self.d)
        self.assertEqual(
            t,
            [("60", 196), ("70", 131), ("50", 67), ("80", 56), ("00", 27)],
            "test of top_five_decade",
        )

    def test_top_five_album(self):
        t = top_five_album(self.d)
        self.assertEqual(
            t,
            [('The Great Twenty-Eight', 6), ('Star Time', 6), ('Elvis Presley', 5), ('Greatest Hits', 5), ('Portrait of a Legend 1951-1964', 4)],
            "test of top_five_album",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
