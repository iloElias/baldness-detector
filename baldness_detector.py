import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import cv2

model = load_model('baldness-detection-model.h5')

def prepare_image(img):
    img = img.convert("RGB")
    img = img.resize((224, 224))
    img = img_to_array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img

def interpret_predictions(preds):
    class_label = preds[0][0]
    class_name = "Careca." if class_label >= 0.5 else "Não é careca."
    return class_name

def predict(image_path):
    img = Image.open(image_path)
    img = prepare_image(img)
    preds = model.predict(img)
    class_name = interpret_predictions(preds)
    return class_name

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Detecção de careca")
        self.state('zoomed') if self.tk.call('tk', 'windowingsystem') == 'win32' else self.attributes('-fullscreen', True)

        main_frame = tk.Frame(self)
        main_frame.pack(expand=True, fill='both')

        self.label = tk.Label(main_frame, text="Detecção de careca", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.image_frame = tk.Frame(main_frame, width=800, height=600)
        self.image_frame.pack(expand=True)
        self.image_frame.pack_propagate(False)

        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack(expand=True)

        self.result_label = tk.Label(main_frame, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=20)

        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=20)

        self.predict_button = tk.Button(button_frame, text="Selecionar imagem", command=self.load_image)
        self.predict_button.pack(side='left', padx=10)

        self.capture_button = tk.Button(button_frame, text="Tirar foto", command=self.capture_image)
        self.capture_button.pack(side='left', padx=10)

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            class_name = predict(file_path)
            img = Image.open(file_path)
            self.display_image(img)
            self.result_label.config(text=f"Predição: {class_name}")

    def display_image(self, img):
        img.thumbnail((800, 600))
        img = ImageTk.PhotoImage(img)
        self.image_label.config(image=img)
        self.image_label.image = img

    def capture_image(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite("captured_image.jpg", frame)
            cap.release()
            class_name = predict("captured_image.jpg")
            img = Image.open("captured_image.jpg")
            self.display_image(img)
            self.result_label.config(text=f"Predição: {class_name}")
        else:
            cap.release()
            self.result_label.config(text="Não foi possivel tirar uma foto")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
