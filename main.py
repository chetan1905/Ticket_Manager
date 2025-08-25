# This class serves as the entry/execution point for this project
from db_queries import init_table

class main(): # organize the entire functionality inside this function
    
    def __init__(self):
        print("In main")
        init_table()



if __name__ == "__main__": # Entry Point
    
    main()
    