import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import json
import os
import webbrowser
from google import genai
from google.genai import types

import settings

try:
    client = genai.Client(api_key=settings.API_KEY)
except Exception as e:
    messagebox.showerror("Error", f"Invalid API Key: {e}")
    exit()


def generate_vr_scene():
    user_prompt = input_text.get("1.0", tk.END).strip()
    if not user_prompt:
        messagebox.showwarning("Warning", "Describe your scene first!")
        return

    btn_generate.config(
        state=tk.DISABLED, text="VR World Generation in Progress..", bg="#ddd"
    )
    feedback_label.config(text="Request Analysis in Progress...")

    threading.Thread(target=run_api_logic, args=(user_prompt,), daemon=True).start()


def run_api_logic(prompt):
    system_instruction = """
    Sei un esperto di WebXR e A-Frame. Il tuo compito è ricevere una descrizione di una scena, analizzarla e generare il codice.
    Devi restituire ESCLUSIVAMENTE un oggetto JSON con queste due chiavi:
    1. "feedback": Una stringa, in lingua inglese che valuta la chiarezza e la correttezza grammaticale e sintattica del prompt dell'utente e suggerisce miglioramenti grammaticali o tecnici. Ricorda che il prompt dell'utente deve essere tassativamente scritto in lingua inglese, nessun'altra lingua è ammessa! Pertanto la correttezza grammaticale e sintattica del prompt si rifanno alle regole della lingua inglese.
    2. "html_code": Una stringa contenente un file HTML completo (<!DOCTYPE html>...) che usa A-Frame (v1.6.0) per ricreare la scena.
       - Usa primitive colorate (a-box, a-sphere, a-plane, a-sky).
       - Aggiungi luci appropriate.
       - Aggiungi commenti nel codice per spiegare cosa sono gli oggetti.
       - Assicurati che la camera sia posizionata correttamente (0 1.6 0).
    """

    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction,
                response_mime_type="application/json",  # FORZA L'OUTPUT JSON
            ),
        )

        data = json.loads(response.text)
        root.after(0, update_ui_success, data)

    except Exception as e:
        root.after(0, update_ui_error, str(e))


def update_ui_success(data):
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"{data['feedback']}")

    file_path = os.path.abspath("scena_vr.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(data["html_code"])

    feedback_label.config(text="Scene generated correctly!", fg="green")
    btn_generate.config(state=tk.NORMAL, text="Generate VR Scene", bg="#4CAF50")

    webbrowser.open(f"file://{file_path}")


def update_ui_error(error_msg):
    feedback_label.config(text="Scene generation error", fg="red")
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"ERRORE: {error_msg}")
    btn_generate.config(state=tk.NORMAL, text="Generate VR Scene", bg="#4CAF50")


root = tk.Tk()
root.title("Nightmare Machine")

try:
    root.state("zoomed")
except tk.TclError:
    # Fallback, qualora non funzioni "zoomed"
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(f"{w}x{h}+0+0")

tk.Label(
    root,
    text="Describe the scene (i.e.: 'A red cube on a blue floor with a yellow sun')",
    font=("Arial", 20, "italic"),
).pack(anchor="w", padx=20)
input_text = tk.Text(root, height=4, font=("Arial", 15))
input_text.pack(fill=tk.X, padx=20, pady=5)

btn_generate = tk.Button(
    root,
    text="Generate Scene",
    command=generate_vr_scene,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 20, "bold"),
    height=2,
)
btn_generate.pack(pady=10, fill=tk.X, padx=100)

feedback_label = tk.Label(root, text="", font=("Arial", 20, "italic"))
feedback_label.pack()

tk.Label(root, text="Teacher Feedback (AI):", font=("Arial", 20, "bold")).pack(
    anchor="w", padx=20, pady=(20, 0)
)
output_text = scrolledtext.ScrolledText(
    root, height=10, font=("Courier", 20), bg="#f0f0f0"
)
output_text.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

root.mainloop()
