import torch
import numpy as np
import cv2
from time import time
from ultralytics import yolo

class ObjectDetection:
    def _init_(self, capture_index):
        self.capture_index = capture_index

        self_device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("Using Device: ", self.device)

        self.model = self.load_model()

    def load_model(self):

        model = yolo("FoodModel.pt")
        model.fuse()

        return model
    
    def predict(self,frame):

        results = self.mode(frame)

        return results
    
    def plot_bboxes(self, results, frame):

        xyxys = []
        confidences = []
        class_ids = []

        for result in results:
            boxes = result.boxes.cpu().numpy()
            
            
            xyxy = boxes.xyxy
            print(xyxy)

        return frame





    

