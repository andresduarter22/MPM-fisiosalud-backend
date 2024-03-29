from enum import IntEnum

collections = [
    "patient",
    "shopArticle",
    "contactList",
    "staff",
    "therapy",
    "treatment",
    "workingArea",
]

class TokenType(IntEnum):
    ID = 0
    ACCESS = 1
    REFRESH = 2

KNOWN_FACES_DIR = 'main/pictures/known_patients'
UNKNOWN_FACES_DIR = 'main/pictures/unknown_patient'
TOLERANCE = 0.4
COLLECTONS_WITHOUT_OBJECT_ID = [ "patient", "staff" ]