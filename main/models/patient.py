from main.database_manager.db_manager import DbManager

class Patient():
    def insert(dict):
        try:
            DbManager.get_instance().insertOne("patient", dict)
        except:
            print("ay nooooo")
