import dlib
import cv2

# Load the pre-trained face recognition model from dlib
shape_predictor_path = r"C:\Users\qotiba\Desktop\Code\python\shape_predictor_68_face_landmarks.dat"
face_recognition_model_path = r"C:\Users\qotiba\Desktop\Code\python\dlib_face_recognition_resnet_model_v1.dat"

# Load the image
image = cv2.imread(r"C:\Users\qotiba\Desktop\photo.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find all face rectangles in the image
face_detector = dlib.get_frontal_face_detector()
faces = face_detector(gray_image)

# Load a pre-trained model for face recognition
shape_predictor = dlib.shape_predictor(shape_predictor_path)
face_recognizer = dlib.face_recognition_model_v1(face_recognition_model_path)

# Loop through each face in the image
for face in faces:
    # Get facial landmarks
    landmarks = shape_predictor(gray_image, face)
    
    # Get face descriptor
    face_descriptor = face_recognizer.compute_face_descriptor(image, landmarks, num_jitters=1)

    # Perform face recognition tasks, e.g., compare with known faces

    # Draw a rectangle around the face
    cv2.rectangle(image, (face.left(), face.top()), (face.right(), face.bottom()), (0, 255, 0), 2)

# Display the image with rectangles around the detected faces
cv2.imshow("Face Recognition", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
