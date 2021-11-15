# -----------------------------------------------------------
# This file generates the fake data into local database
#
# email -> mintu.giri1997@gmail.com
# -----------------------------------------------------------

### --- IMPORTS --- ###
from database import create_table, insert_data

# -----------------------------------------------------------
# main function
# -----------------------------------------------------------
def main():
    db, table = "fake_data","UNPROCESSED"
    create_table(db,table)
    for i in range(1,10001):
        insert_data(db,table,(f'Mac{i}', 'Mohan', 20, 'M', 2000*i))
    print("Fake Data Generated!!!")

if __name__ == "__main__" :
    main()