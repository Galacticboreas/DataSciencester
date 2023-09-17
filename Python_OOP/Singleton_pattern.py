class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"Connecting to the database: {self.user}, {self.psw}, {self.port}")
    
    def close(self):
        print("Closing the database connection")
    
    def read(self):
        return "Data from the database"

    def write(self, data):
        print(f"Database entry {data}")

# And then we assume that only one instance of this class 
# should exist in the program at each moment of its operation. 
# That is, there should not be two objects of the DataBase 
# class at the same time. To ensure and guarantee this, the 
# Singleton pattern is used. We implement it for the DataBase class.

# Let's write a special attribute in it (at the class level):
# __instance = None
# which will store a reference to an instance of this class. 
# If there is no instance, the attribute will take the value 
# None. And then, to guarantee the creation of strictly one 
# instance, we add the magic method __new to the class__:

db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)
print(id(db), id(db2))

db.connect()
db2.connect()
