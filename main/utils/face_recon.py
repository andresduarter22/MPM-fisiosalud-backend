import face_recognition
import os
import base64
from main.utils.constants import KNOWN_FACES_DIR, UNKNOWN_FACES_DIR, TOLERANCE
from main.utils.string_utils import format_string


def recognize_face():
    known_faces = []
    known_names = []
    for name in os.listdir(KNOWN_FACES_DIR):
        for filename in os.listdir(f'{KNOWN_FACES_DIR}/{name}'):
            knownFace = face_recognition.load_image_file(
                f'{KNOWN_FACES_DIR}/{name}/{filename}')
            encoding = face_recognition.face_encodings(knownFace)[0]
            known_faces.append(encoding)
            known_names.append(name)
    print("patient codes", known_names)

    image = face_recognition.load_image_file(
        f'{UNKNOWN_FACES_DIR}/unknown_patient.jpg')
    encodings = face_recognition.face_encodings(image)
    if len(encodings) > 0:
        for face_encoding in encodings:
            results = face_recognition.compare_faces(
                known_faces, face_encoding, TOLERANCE)
            match = None
            print("results", results)
            if True in results:
                match = known_names[results.index(True)]
                print(f' - id: {match} from {results}')
                return {
                    "id": match,
                    "result": True
                }
            else:
                return {
                    "message": "Patient face not found, pelase try again",
                    "result": False
                }
    else:
        return {
            "message": "Patient face not found, pelase try again",
            "result": False
        }


def check_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def save_image(image_base64, image_name, image_dir):
    check_directory(image_dir)
    formated_name = format_string(image_name)
    img_name = f"{image_dir}/{formated_name}.jpg"
    image_data = image_base64.split(",")[1]
    image = base64.b64decode(image_data)
    image_result = open(img_name, 'wb')
    image_result.write(image)

def save_patient_image(image_base64, patient_name, patient_id, image_dir=KNOWN_FACES_DIR):
    save_image(image_base64, patient_name, f"{image_dir}/{patient_id}")

def delete_image(image_dir):
    print("deleting image")
    os.remove(image_dir)
    print("image deleted")