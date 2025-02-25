# Nhận diện khuôn mặt
import yaml
from facenet_pytorch import InceptionResnetV1

from src.utils.face_utils import preprocess
from scipy.spatial.distance import cosine

from src.recognition.database import Database

class FaceRecognizer:
    def __init__(self):
        with open("configs/model_config.yaml", "r", encoding='utf8') as f:
            config = yaml.safe_load(f)['face_recognition']

        self.model_name = config['model_name']
        self.difference_threshold = config['difference_threshold']
        self.image_size = (config['image_size']['w'], config['image_size']['h'])

        self.database = Database(self)

        self.model = InceptionResnetV1(pretrained=config['weights_path'], classify=False).eval()

    def recognize_faces(self, faces):
        # input: ảnh khuôn mặt
        # output: tên của người đăng ký
        embeddings = [self._get_face_embeddings(preprocess(face, self.image_size)) for face in faces]
        names = [self._recognize_face(embedding) for embedding in embeddings]
        return names
    
    def _get_face_embeddings(self, face):
        embedding = self.model(face.unsqueeze(0))
        return embedding.detach().numpy()[0]
    
    def _recognize_face(self, embedding):
        min_difference = (None, float('inf'))
        for name in self.database.names:
            embs = self.database.get_embeddings(name)
            for emb in embs:
                difference = cosine(embedding, emb) # cosine distance [-1:1]
                if (difference < self.difference_threshold) and (difference < min_difference[1]):
                    min_difference = (name, difference)
        return min_difference
    
    def __str__(self):
        return f"FaceRecognizer(model_name={self.model_name}, difference_threshold={self.difference_threshold})"