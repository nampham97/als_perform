import oracledb
import os
from dotenv import load_dotenv

def getConfig():
    load_dotenv()
    hostnameDB = os.getenv("DATABASE_HOST")
    portDB = os.getenv("DATABASE_PORT")
    service_nameDB = os.getenv("DATABASE_SERVICE_NAME")

    return {
        "userDb": os.getenv("DATABASE_USERNAME"),
        "passDB": os.getenv("DATABASE_PASSWORD"),
        "dsnDb": f"{hostnameDB}:{portDB}/{service_nameDB}"
    }

def create_instanceDB(userDb, passDB, dsnDb):
    print("Waiting connect to Oracle Database...")
    return oracledb.connect(
        user=userDb,
        password=passDB,
        dsn=dsnDb)

def get_db_connection():
    userDb, passDB, dsnDb = getConfig().values()
    print('userDb:', userDb)
    print('passDB:', passDB)
    return create_instanceDB(userDb, passDB, dsnDb)

if "__main__" == __name__:
    pass