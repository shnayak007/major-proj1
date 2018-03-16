import MySQLdb as mysql

def connect_to_db():
    # Open database connection
    try:
        db = mysql.connect("localhost", "root", "", "fb_module");
        return db
    except (mysql.Error) as e:
        print(e)

def populate(data):
    # Connect to db
    db = connect_to_db()
    cursor=db.cursor()

    # Retrieve data from json object
    page_id=str(data["id"])
    likes=str(data["fan_count"])
    talking_about=str(data["talking_about_count"])
    comp_name =(data["name"])

    query="INSERT INTO page_info VALUES("+likes+","+page_id+",\"active\",\"sh1212\"," \
        +talking_about+",\""+comp_name+"\",CURDATE());"
    try:
        cursor.execute(query);
        db.commit()
    except (mysql.Error) as e:
         print(e)
         db.rollback()




