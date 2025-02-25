import cv2
import numpy as np
import torch

def get_face_image(image, faces):
    images = []
    for face in faces:
        x1,y1,x2,y2 = face['box']
        eyes = face['eyes']

        image = align_face(image, eyes[0], eyes[1])

        images.append(image[y1:y2, x1:x2])

    return images

def align_face(image, left_eye, right_eye):
    # Calculate the center point between the two eyes
    eye_center = ((left_eye[0] + right_eye[0]) * 0.5,
                  (left_eye[1] + right_eye[1]) * 0.5)
    
    # Determine the angle between the eyes
    dy = right_eye[1] - left_eye[1]
    dx = right_eye[0] - left_eye[0]
    angle = np.degrees(np.arctan2(dy, dx))
    
    # Get the rotation matrix to rotate around the eye center
    M = cv2.getRotationMatrix2D(eye_center, angle, scale=1)
    # Apply the affine transformation (rotate the image)
    aligned_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return aligned_image

def resize_face(face, size):
    interpolation = cv2.INTER_AREA
    if (size[0] * size[1]) < (face.shape[0] * face.shape[1]):
        interpolation = cv2.INTER_CUBIC
    face = cv2.resize(face, size, interpolation=interpolation)
    return face
        
def transform(face):
    face = face.transpose((2, 0, 1))
    face = face.astype('float32') / 255.0
    return  torch.tensor(face)

def preprocess(face, size): # size is tuple (w, h)
    face = resize_face(face, size)
    face = transform(face)
    return face