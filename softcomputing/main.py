#!/usr/bin/python

import csv
import geometric_transformation

# TODO ( Italian languages ) 
# Leggo i dati dai vari files 
# inizializzo un numero prefissato di formiche 
# ogni formica crea una soluzione ( thread ) e computa le varie variazioni 
# ogni formica contribuisce ad apportare delle correzioni al calcolo dell'oggetto ( thread ) 
# ogni formica calcola la performance della soluzione trovata e aggiorna la trails 
# condizione di uscita NON valida, torna su 
# ritorna la miglior soluzione trovata 


REAL_POSITION_FILE  = "data/real_end_position"

CAMERAS_DATA_FILE   = "data/camera_rotations"

def main():

    with open(REAL_POSITION_FILE, 'rb') as rpositionfile:
        data = csv.reader(rpositionfile, skipinitialspace=True)
        for row in data: real_position = row
        rpositionfile.close()

    print "Real position of the object is: ", real_position

    point = geometric_transformation.geometric_transformation(0,0,0)
    print dir(point)

    # for every camera roto-traslate the object 
    with open(CAMERAS_DATA_FILE, 'rb') as csvfile:

        data = csv.reader(csvfile, skipinitialspace=True)

        for row in data:

            # skip row with comments or empty 
            if len(row) == 0: continue
            if row[0][0] == '#': continue

            # transform text to integers 
            row = map(lambda x: float(x), row)

            print "ROW: ", row

            point.rototraslate_on_all_axis(row[0] + row[1], row[2] + row[3], row[4] + row[5], row[6] + row[7], row[8] + row[9], row[10]+row[11])

            print point.actual_position

            print "-----------------------"










__init__ = main()
