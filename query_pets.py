#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys


def main():
    """This script queries the Pets database and returns queried information.

    Raises:
        Exception: A generic exception.
    """

    try:
        # Connect to DB
        db = lite.connect('pets.db')
        cursor = db.cursor()

        while True:
            try:
                # Validate input
                user_input = int(raw_input('\nPlease enter an ID #: '))
                if user_input == -1:
                    sys.exit()

                elif isinstance(user_input, int) and user_input is not -1:
                    cursor.execute(
                        '''
                            SELECT person.first_name, person.last_name, person.age, pet.name, pet.breed, pet.age, pet.dead
                            FROM person_pet, person, pet
                            WHERE person_pet.person_id = {0}
                            AND person_pet.person_id = person.id
                            AND person_pet.pet_id = pet.id
                        '''.format(user_input))

                    # Raise exception if there is no match.
                    requested_data = cursor.fetchall()
                    print '''\n{} {} is {} years old.\nPets that belong to this person:
                    '''.format(
                        requested_data[0][0],
                        requested_data[0][1],
                        requested_data[0][2]
                    )

                    for row in requested_data:
                        if row[6] == 1:
                            print '{} was a {} who died at the age of {}.'.format(
                                row[3], row[4], row[5])
                        elif row[6] == 0:
                            print '{}, a {} that is {} years old.'.format(
                                row[3], row[4], row[5])

            except Exception:
                print 'ERROR: Enter a valid ID.'

        db.close()

    except Exception:
        print 'ERROR: The database could not be queried.'


if __name__ == '__main__':
    main()
