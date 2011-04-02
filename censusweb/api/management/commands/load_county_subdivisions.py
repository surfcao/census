"""
"""
from django.core.management.base import BaseCommand, CommandError, handle_default_options
from optparse import make_option

import csv
from urllib import urlopen
from django.db import connection
from django.db import connection, transaction
    
class Command(BaseCommand):
    args=''
    help=''
    option_list= BaseCommand.option_list + ()

    def get_version(self):
        return "0.1"

    def handle(self, *args, **options):
        """
        Create a lookup table based on data.
        explanation: http://www.census.gov/geo/www/gazetteer/gazetteer2010_layout.html#cousub
        """
        cur = connection.cursor()
        cur.execute("drop table if exists county_subdivision_lookup")
        cur.execute("""
            create table county_subdivision_lookup (
                state_code char(2),
                geo_id char(10),
                ansi_code char(8),
                county_subdivision_name varchar(255),
                state_fips char(2),
                county_fips char(3)
            )
        """)
        
        reader = fancyreader(urlopen("http://www.census.gov/geo/www/gazetteer/files/Gaz_cousubs_national.txt"), delimiter='\t', encoding="ISO-8859-1")
        headers = reader.next() # junk
        INSERT = "insert into county_subdivision_lookup (state_code, geo_id, ansi_code, county_subdivision_name, state_fips, county_fips) values (%s,%s,%s,%s,%s,%s)"
        for row in reader:
            #state is first two, county is next three
            insert_me = row[:4]
            state_fips = row[1][0:2]
            county_fips = row[1][2:5]
            insert_me.append(state_fips)
            insert_me.append(county_fips)
            cur.execute(INSERT,insert_me)

        transaction.commit_unless_managed()
    
import csv, codecs, cStringIO

class UTF8Recoder:
    """
    Iterator that reads an encoded stream and reencodes the input to UTF-8
    """
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)

    def __iter__(self):
        return self

    def next(self):
        return self.reader.next().encode("utf-8")

class fancyreader:
    """
    A CSV reader which will iterate over lines in the CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)

    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]

    def __iter__(self):
        return self