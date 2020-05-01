import sqlite3
from sqlite3 import Error
database="./pets.db"

#establish connection
try:
    pets_db=sqlite3.connect(database)
except Error as e:
    print(e)


def query_person(id):
    """Function to query the person"""
    pets=[] #to store pets owned by person #id
    db_cursor=pets_db.cursor()
    person_sql="SELECT * FROM Person WHERE id ={}".format(id)
    db_cursor.execute(person_sql)
    result=db_cursor.fetchone()
    if result == None:
        print("No user with that Id") # no user found with that id
    else:
        #print the user's information
        print("{} {}, {} years old".format(result[1], result[2],result[3]))
        person_pets="SELECT * FROM Person_Pet WHERE person_id={}".format(id)
        db_cursor.execute(person_pets)
        person_pet_result=db_cursor.fetchall()

        for x in person_pet_result:
            pet_query="SELECT * FROM Pet WHERE id={}".format(x[1])
            db_cursor.execute(pet_query)
            pet_result=db_cursor.fetchall()
            pets+=pet_result
    #iterate the pets and print result
    for x in pets:
        if x[4]==1: #check if dog is alive or dead
            print ("{} {} owned {} a {}, that was {} years old".format(result[1], result[2],x[1],x[2],x[3]))
        else: #if not dead
            print ("{} {} owns {} a {}, that is {} years old".format(result[1], result[2],x[1],x[2],x[3]))



def main():
    isExit=True

    while isExit:
        person_id=input("Enter a persons ID: ")
        #exit if users enters -1
        if int(person_id) == -1:
            isExit=False
        else:
            query_person(person_id)


if __name__ == "__main__":
    main()

