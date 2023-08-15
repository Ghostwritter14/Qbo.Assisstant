import face_recognition
import os
import pickle

# Paths for the encodings and names files
encodings_file = 'encodings.pkl'     # trained face cardinal location encodings file
known_names_file = 'known_names.pkl'  # trained name labels file
reference_images_path = 'Ref_pics/'  # change name to your own choice name if you would like to


def train():
    all_face_encodings = []
    known_names = []

    # Check if reference images path exists
    if not os.path.exists(reference_images_path):
        print(f"Error: {reference_images_path} does not exist.")
        return

    for root, dirs, files in os.walk(reference_images_path):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                image_path = os.path.join(root, file)
                person_name = os.path.basename(root)  # Get the name of the subfolder
                image = face_recognition.load_image_file(image_path)
                face_encodings = face_recognition.face_encodings(image)

                if face_encodings:
                    all_face_encodings.append(face_encodings[0])
                    known_names.append(person_name)  # Using subfolder name as the person's name

    # Save data to pickle files
    with open(encodings_file, 'wb') as enc_file:
        pickle.dump(all_face_encodings, enc_file)

    with open(known_names_file, 'wb') as names_file:
        pickle.dump(known_names, names_file)

    print(f"Training complete. Encodings saved to {encodings_file} and names saved to {known_names_file}.")


if __name__ == "__main__":
    train()
