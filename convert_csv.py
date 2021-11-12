#!/usr/bin/env python

from convert import Convert

convert = Convert()
convert.SAVE_LOCATION = 'foursquare.ics'
convert.CSV_FILE_LOCATION = 'foursquare.csv'

convert.read_ical(convert.SAVE_LOCATION)
convert.make_csv()
convert.save_csv(convert.CSV_FILE_LOCATION)

