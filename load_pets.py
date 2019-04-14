#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sqlite3 as lite
import sys

person = (
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23),
)

pet = (
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
)

person_pet = (
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
)

try:
    con = lite.connect('pets.db')
    cursor = con.cursor()

    cursor.executemany("INSERT INTO person(id, first_name, last_name, age) "
                       "VALUES(?, ?, ?, ?)", person)
    cursor.executemany("INSERT INTO pet(id, name, breed, age, dead) "
                       "VALUES(?, ?, ?, ?, ?)", pet)
    cursor.executemany("INSERT INTO person_pet(person_id, pet_id) "
                       "VALUES(?, ?)", person_pet)
    con.commit()

except lite.Error, e:
    if con:
        con.rollback()
    print "ERROR: {}".format(e.args[0])
    sys.exit(1)

finally:
    if con:
        con.close()

# Delete this
