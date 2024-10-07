import yt_dlp

def download_audio_with_ytdlp(video_url, output_path='downloads'):
    try:
        # Cria o diretório de saída se não existir
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        print(f"Download completo! O arquivo foi salvo na pasta: {output_path}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
url = input("Insira o link do vídeo do YouTube: ")
download_audio_with_ytdlp(url)
