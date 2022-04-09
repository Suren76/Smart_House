import face_recognition
import cv2
import time
import os
import sys
import pickle
import datetime

import send_to_telegram
from send_to_telegram import *


def face_unlock():
    users = os.listdir("dataset")
    users_encodings = [f"dataset/{username}/encodings/{sorted(os.listdir(f'dataset/{username}/encodings/'))[-1]}" for username in users]
    print(users_encodings)
    cap = cv2.VideoCapture(0)

    attempts = 30

    while attempts != 0:
        print(attempts)
        attempts -= 1
        success, img = cap.read()
        cv2.waitKey(1)

        face_location = face_recognition.face_locations(img)

        # print(results)

        if len(face_location) == 0:
            time.sleep(1)
            continue

        img_encodings = face_recognition.face_encodings(img)[0]

        for encoding_file in users_encodings:
            data = pickle.loads(open(encoding_file, "rb").read())
            # print(data["encodings"])
            result = face_recognition.compare_faces(data["encodings"], img_encodings)

            if True in set(result):
                return {"name": data["name"], "unlock": True}
            else:
                cv2.imwrite(img, f"unknown_people_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}")
                send_me(f"unknown_people_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}")
                return {"name": "unknown", "unlock": False}

        # for (top, right, bottom, left) in face_location:
        #     cv2.rectangle(img, (left, top), (right, bottom), (56, 178, 86), thickness=3)

        # cv2.imshow(f"web camera", img)
        # print(result)

    return False


def face_model(_name: str, model_data_type, video_path=None):
    if not os.path.exists("dataset"):
        sys.exit()
    if not os.path.exists(f"dataset/{_name}"):
        os.mkdir(f"dataset/{_name}")
    if not os.path.exists(f"dataset/{_name}/encodings"):
        os.mkdir(f"dataset/{_name}/encodings")

    def __model_by_photos(name):
        if not os.path.exists(f"dataset/{name}/img"):
            sys.exit()

        encodings = []
        images = os.listdir(f"dataset/{name}/img")

        print(os.listdir(f"dataset/{name}/img"))

        for image in images:
            print(f"dataset/{str(name)}/img/{str(image)}")

            face_image = face_recognition.load_image_file(f"dataset/{name}/img/{image}")
            if len(face_recognition.face_locations(face_image)) != 0 and len(face_recognition.face_locations(face_image)) == 1:
                face_image_encode = face_recognition.face_encodings(face_image)[0]
            else:
                continue
            # print(face_image_encode)

            if len(encodings) == 0:
                encodings.append(face_image_encode)
            else:
                for item in encodings:
                    result = face_recognition.compare_faces([face_image_encode], item)
                    print("result: ", result)

                    if result[0]:
                        encodings.append(face_image_encode)
                        break

        data = {
            "name": name,
            "encodings": encodings
        }

        with open(f"dataset/{name}/encodings/{name}_encodings_{datetime.datetime.now().strftime('%Y%m%d%H%M')}.pickle", "wb") as file:
            file.write(pickle.dumps(data))

        return "model encodings added"

    def __model_by_video(name, video):
        if not os.path.exists(f"dataset/{_name}/img"):
            os.mkdir(f"dataset/{_name}/img")

        photos_count = 0

        cap = cv2.VideoCapture(video)

        while True:

            success, img = cap.read()
            fps = cap.get(cv2.CAP_PROP_FPS)

            if success:
                frame_id = int(round(cap.get(1)))
                cv2.waitKey(1)

                if frame_id % int(round(fps)) == 0:
                    cv2.imwrite(f"dataset/{name}/img/{name}_screenshot_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.jpg", img)
                    photos_count += 1
                    print("screenshot")
                if photos_count >= 30:
                    print("there are 30 images")
                    break
            else:
                break

        cap.release()
        cv2.destroyAllWindows()

    if model_data_type == "photo":
        return __model_by_photos(name=_name)
    if model_data_type == "video":
        __model_by_video(name=_name, video=video_path)
        __model_by_photos(_name)

print(1)
print(face_unlock())
print( "end")
print(2)
