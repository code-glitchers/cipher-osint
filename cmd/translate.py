import tkinter as tk
from googletrans import Translator
from langdetect import detect
from gtts import gTTS
import playsound
import os

def detect_language():
    text = entry.get()
    detected_lang = detect(text)
    source_lang.set(detected_lang)

def translate_text():
    text = entry.get()
    translator = Translator()
    result = translator.translate(text, src=source_lang.get(), dest=target_lang.get())
    translated_text.set(result.text)

def copy_text():
    root.clipboard_clear()
    root.clipboard_append(translated_text.get())

def read_audio():
    text = translated_text.get()
    tts = gTTS(text=text, lang=target_lang.get(), slow=False)
    tts.save("translation.mp3")
    playsound.playsound("translation.mp3")
    os.remove("translation.mp3")

root = tk.Tk()
root.title("Translator")

source_lang = tk.StringVar()
source_lang.set("")
target_lang = tk.StringVar()
target_lang.set("es")
translated_text = tk.StringVar()

source_label = tk.Label(root, text="Source Language:")
source_label.grid(row=0, column=0, padx=5, pady=5)
source_entry = tk.Entry(root, textvariable=source_lang, state="readonly", width=30)
source_entry.grid(row=0, column=1, padx=5, pady=5)

detect_button = tk.Button(root, text="Detect Language", command=detect_language)
detect_button.grid(row=0, column=2, padx=5, pady=5)

target_label = tk.Label(root, text="Target Language:")
target_label.grid(row=1, column=0, padx=5, pady=5)
target_entry = tk.Entry(root, textvariable=target_lang, width=30)
target_entry.grid(row=1, column=1, padx=5, pady=5)

entry = tk.Entry(root, width=30)
entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

copy_button = tk.Button(root, text="Copy", command=copy_text)
copy_button.grid(row=4, column=0, padx=5, pady=5)

audio_button = tk.Button(root, text="Audio", command=read_audio)
audio_button.grid(row=4, column=1, padx=5, pady=5)

output_label = tk.Label(root, text="Translated Text:")
output_label.grid(row=5, column=0, padx=5, pady=5)
output_text = tk.Label(root, textvariable=translated_text, wraplength=300, justify="left")
output_text.grid(row=5, column=1, padx=5, pady=5)

root.mainloop()
