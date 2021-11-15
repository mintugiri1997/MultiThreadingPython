# -----------------------------------------------------------
# This file process the data.
#
# email -> mintu.giri1997@gmail.com
# -----------------------------------------------------------

### --- IMPORTS --- ###
from database import delete_data, create_table, insert_data

# -----------------------------------------------------------
# This function returns 10 elements from the list.
# -----------------------------------------------------------
def pop_ten_elements(unprocessed_list):
    ready_list = []
    unprocessed_list.reverse()
    for i in range(10):
        item = unprocessed_list.pop()
        ready_list.append(item)
        delete_data("fake_data","UNPROCESSED",item[0])
    print("Elements Popped!")
    return ready_list

# -----------------------------------------------------------
# This function processes the data.
# -----------------------------------------------------------
def process_data(data):
    db, table = "fake_data", "PROCESSED"
    for d in data:
        print(f"Processing Data : {d}")
        insert_data(db,table,d)
    print(f"Processing Completed!!!")