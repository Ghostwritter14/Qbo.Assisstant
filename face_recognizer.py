import dlib
import face_recognition
import pickle
import os
import numpy as np

encodings_file = 'encodings.pkl'
known_names_file = 'known_names.pkl'


class FaceRecognizer:
    def __init__(self):
        self.encodings = []
        self.names = []
        self.face_detector = dlib.get_frontal_face_detector()
        self.shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        self.face_encoder = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

        if os.path.exists(encodings_file):
            with open(encodings_file, 'rb') as file:
                self.encodings = pickle.load(file)

        if os.path.exists(known_names_file):
            with open(known_names_file, 'rb') as file:
                self.names = pickle.load(file)

        if not self.encodings or not self.names:
            print("Encodings or known names not found! Make sure the training has been done.")

    def dlib_rect_to_tuple(self, rect):
        """ Convert a dlib rectangle into a tuple of (top, right, bottom, left) """
        return (rect.top(),
                rect.right(),
                rect.bottom(),
                rect.left())

    def identify_face(self, frame):
        # Convert the image from BGR color (OpenCV uses this) to RGB color
        rgb_frame = frame[:, :, ::-1]  # Convert BGR to RGB

        # checks
        print("--------------------------------------------------")
        print(f"Type of rgb_frame: {type(rgb_frame)}")
        print(f"Shape of rgb_frame: {rgb_frame.shape}")
        print(f"Data type of rgb_frame elements: {rgb_frame.dtype}")
        print("--------------------------------------------------")

        # Detect faces using dlib get_frontal_face_detector
        face_locations = self.face_detector(rgb_frame)

        # checks
        print(f"Type of face_locations: {type(face_locations)}")
        print(f"Number of detected faces: {len(face_locations)}")
        if face_locations:
            print(f"Type of first face location: {type(face_locations[0])}")
            print(f"Values of first face location: {face_locations[0]}")
            print("--------------------------------------------------")

        # Convert the rectangles into landmarks
        landmarks = [self.shape_predictor(rgb_frame, face_location) for face_location in face_locations]

        # checks
        for idx, landmark in enumerate(landmarks):
            print(f"Type of landmark #{idx + 1}: {type(landmark)}")
            print(f"Number of parts in landmark #{idx + 1}: {landmark.num_parts}")
            print("--------------------------------------------------")

        # Compute the face encodings directly
        face_encodings = [np.array(self.face_encoder.compute_face_descriptor(rgb_frame.astype(np.uint8), landmark,
                                                                             num_jitters=1))
                          for landmark in landmarks]

        # See if the face is a match for the known faces
        if face_encodings:
            matches = face_recognition.compare_faces(self.encodings, face_encodings[0])
            name = "Unknown"

            # If a match was found in known_face_encodings, use the first one
            if True in matches:
                first_match_index = matches.index(True)
                name = self.names[first_match_index]

            return name
        else:
            return "Unknown"




