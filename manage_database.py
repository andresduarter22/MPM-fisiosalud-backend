import pprint
from main.database_manager.db_manager import DbManager
from main.models.patient import Patient
from main.api.api_endpoints import FisiosaludAPI

if __name__ == "__main__":
    # db_manager = DbManager()
    # db_manager.init_database()
    # patient = Patient()
    doc = {
        "_id": "5973546",
        "patient_name": "Andres Duarte",
        "patient_email": "andresduarter13@gmail.com",
        "patient_nickname": "dinis",
        "patient_birthday": "13/11/1997",
        "patient_phone_number": "72027677",
        "patient_address": "calle G # 108, Achumani",
        "reference_contact_name": "Sergio ",
        "reference_contact_number": "666",
        "reference_doctor": "Maggi",
        "additional_info": "Test",
        "old_id": "1"
    }
    doc1 = {
        "_id": "5973546",
        "patient_name": "Andres Duarte Rios",
        "patient_email": "andresduarter13@gmail.com",
        "patient_nickname": "dinis",
        "patient_birthday": "13/11/1997",
        "patient_phone_number": "72027677",
        "patient_address": "calle G # 108, Achumani",
        "reference_contact_name": "Sergio ",
        "reference_contact_number": "666",
        "reference_doctor": "Maggi",
        "additional_info": "Test",
        "old_id": "1"
    }

    FisiosaludAPI().run()
    # pprint.pprint(patient.selectAll())
