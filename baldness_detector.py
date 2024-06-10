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
    probability = preds[0][0] * 100
    if probability < 20:
        class_name = "Sem Calvície"
    elif 20 <= probability < 40:
        class_name = "Baixa Calvície"
    elif 40 <= probability < 70:
        class_name = "Calvície Moderada"
    elif 70 <= probability < 95:
        class_name = "Calvície Alta"
    else:
        class_name = "Aeroporto de mosquito"

    return f"{class_name} ({probability:.2f}%)"

def predict(image_path):
    img = Image.open(image_path)
    img = prepare_image(img)
    preds = model.predict(img)
    class_name = interpret_predictions(preds)
    return class_name

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import cv2

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Detecção de Calvície")

        if self.tk.call('tk', 'windowingsystem') == 'win32':
            self.state('zoomed')
        else:
            self.attributes('-fullscreen', True)

        main_frame = tk.Frame(self)
        main_frame.pack(expand=True, fill='both')

        self.label = tk.Label(main_frame, text="Detecção de Calvície", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.image_frame = tk.Frame(main_frame, width=1600, height=600)
        self.image_frame.pack(expand=True)
        self.image_frame.pack_propagate(False)

        self.captured_image_label = tk.Label(self.image_frame, width=800, height=600, bg="gray")
        self.captured_image_label.pack(side='left', padx=10)

        self.camera_feed_label = tk.Label(self.image_frame, width=800, height=600)
        self.camera_feed_label.pack(side='left', padx=10)

        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=20)

        self.predict_button = tk.Button(button_frame, text="Selecionar Imagem e Detectar", command=self.load_image)
        self.predict_button.pack(side='left', padx=10)

        self.capture_button = tk.Button(button_frame, text="Capturar Imagem", command=self.capture_image)
        self.capture_button.pack(side='left', padx=10)

        self.result_label = tk.Label(main_frame, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=20)

        self.cap = cv2.VideoCapture(0)
        self.show_camera_feed()

    def show_camera_feed(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (800, 600))
            frame = Image.fromarray(frame)
            frame = ImageTk.PhotoImage(frame)
            self.camera_feed_label.config(image=frame)
            self.camera_feed_label.image = frame

        self.camera_feed_label.after(10, self.show_camera_feed)

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            result = predict(file_path)
            img = Image.open(file_path)
            self.display_image(img)
            self.result_label.config(text=result)

    def display_image(self, img):
        img.thumbnail((800, 600))
        img = ImageTk.PhotoImage(img)
        self.captured_image_label.config(image=img)
        self.captured_image_label.image = img

    def capture_image(self):
        ret, frame = self.cap.read()
        if ret:
            cv2.imwrite("captured_image.jpg", frame)
            result = predict("captured_image.jpg")
            img = Image.open("captured_image.jpg")
            self.display_image(img)
            self.result_label.config(text=result)
        else:
            self.result_label.config(text="Falha ao capturar a imagem")

    def on_closing(self):
        self.cap.release()
        self.destroy()

if __name__ == "__main__":
    app = Application()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
