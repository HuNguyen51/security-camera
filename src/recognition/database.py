# Quản lý database đối tượng
import os
import yaml
import cv2

from src.utils.face_utils import transform

class Database:
    def __init__(self, model):
        with open("configs/config.yaml", "r", encoding='utf8') as f:
            config = yaml.safe_load(f)

        self.database_path = config['output_paths']['database']
        self.names = os.listdir(self.database_path)
        self.model = model

    def get_embeddings(self, name):
        embeddings = []
        filenames = os.listdir(f'{self.database_path}/{name}')

        for filename in filenames:
            im_path = f'{self.database_path}/{name}/{filename}'
            img = cv2.imread(im_path)
            img = transform(img)
            embedding = self.model._get_face_embeddings(img)
            embeddings.append(embedding)
        return embeddings

    def __str__(self):
        return f"Database(database_path={self.database_path}, names={self.names}"
    
if __name__ == "__main__":
    db = Database(None)
    print(db.db_embeddings.items())