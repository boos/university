#!/usr/bin/python

import csv
import geometric_transformation

START_POSITION_FILE = "data/start_position"
CAMERAS_DATA_FILE   = "data/camera_rotations"


def main():

    point = geometric_transformation.geometric_transformation(3,5,7)

    with open(CAMERAS_DATA_FILE, 'rb') as csvfile:
        data = csv.reader(csvfile, skipinitialspace=True)

        for row in data:

			# skip row with comments or empty 
            if len(row) == 0: continue
            if row[0][0] == '#': continue

			# transform text to integers 
            row = map(lambda x: int(x), row)

            point.rotate_X_axis(row[0]) # rotate of value
            point.rotate_X_axis(row[1]) # rotate as the error value 

            point.rotate_Y_axis(row[2]) # rotate on Y as value 
            point.rotate_Y_axis(row[3]) # rotate as the error value  

            point.rotate_Z_axis(row[4]) # rotate on Y as value 
            point.rotate_Z_axis(row[5]) # rotate as the error value 

            point.traslate(row[6], row[7], row[8])











__init__ = main()
