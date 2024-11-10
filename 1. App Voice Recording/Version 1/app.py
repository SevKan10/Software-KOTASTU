# Khai báo thư viện
import tkinter as tk
import threading
import time
import speech_recognition as sr
import keyboard
import pyperclip
import pyautogui
import pygame.mixer

# Hàm thực hiện copy paste
def paste_string_in_any_field(message):
    pyperclip.copy(message)
    pyautogui.hotkey('ctrl', 'v')
    print("Đã dán tin nhắn: ", message)

# Hàm nghe và điền
def listen_and_send():
    status_label.config(text="Vui lòng nhập văn bản...")
    pygame.mixer.music.load("beep.wav")
    pygame.mixer.music.play()
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)

    try:
        status_label.config(text="Đang nhận dạng giọng nói...")
        message = recognizer.recognize_google(audio_data, language="vi")
        status_label.config(text="Văn bản của bạn: " + message)
        paste_string_in_any_field(message)
    except sr.UnknownValueError:
        status_label.config(text="Không thể nhận dạng giọng nói")
    except sr.RequestError as e:
        status_label.config(text="Lỗi kết nối; {0}".format(e))

def start_listening_thread():
    thread = threading.Thread(target=listen_and_send)
    thread.start()

def start_listening(event=None):
    status_label.config(text="Đang khởi động...")
    time.sleep(0.7)
    start_listening_thread()

# Giao diện ứng dụng
root = tk.Tk()
root.geometry("400x200")
root.title("Voice Typing App")

status_label = tk.Label(root, text="Chưa sẵn sàng")
status_label.config(text="Chế độ Soạn Văn Bản")
status_label.pack(pady=10)

recognizer = sr.Recognizer()
mic = sr.Microphone()

pygame.mixer.init()

keyboard.add_hotkey('ctrl+shift+alt+m', start_listening)

root.mainloop()
