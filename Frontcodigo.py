import os
import yt_dlp
import tkinter as tk
from tkinter import filedialog, messagebox

# Função para baixar o áudio
def download_audio():
    video_url = url_entry.get()
    output_path = folder_path.get()

    if not video_url:
        messagebox.showerror("Erro", "Por favor, insira o link do vídeo do YouTube.")
        return

    if not output_path:
        messagebox.showerror("Erro", "Por favor, escolha uma pasta de destino.")
        return

    try:
        # Opções do yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        # Faz o download
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        messagebox.showinfo("Sucesso", "Download concluído!")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Função para selecionar pasta
def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_path.set(folder_selected)

# Interface gráfica
root = tk.Tk()
root.title("Baixa as musica ae parça")

# URL do vídeo
tk.Label(root, text="URL do vídeo:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

# Botão para escolher pasta
folder_path = tk.StringVar()
tk.Label(root, text="Pasta de destino:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=folder_path, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Escolher Pasta", command=select_folder).grid(row=1, column=2, padx=10, pady=10)

# Botão para baixar
tk.Button(root, text="Baixar Áudio", command=download_audio, width=20, bg="green", fg="white").grid(row=2, column=1, pady=20)

# Executa o aplicativo
root.mainloop()
