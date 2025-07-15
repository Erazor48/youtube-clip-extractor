import yt_dlp
from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def download_video(url: str, output_dir: str = "downloads", cookies_file: file) -> str:
    """
    Downloads a video from a given URL and saves it to the specified directory.

    Args:
        url (str): The URL of the video to download.
        output_dir (str): The directory where the downloaded video will be saved. Defaults to 'downloads'.

    Returns:
        str: The path to the downloaded video file.
    """
    print("T10")
    os.makedirs(output_dir, exist_ok=True)
    print("T11")
    ydl_opts = {
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "quiet": True,
        "no_warnings": True
    }
    print("T12")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("T13")
        info_dict = ydl.extract_info(url, download=True)
        print("T14")
        video_path = ydl.prepare_filename(info_dict).replace('.webm', '.mp4')
        print("T15")
    return video_path

def convert_to_seconds(temps: str) -> int:
    """
    Convertit un temps donné au format HH:MM:SS en secondes totales.

    Args:
        temps (str): Le temps sous forme de chaîne au format 'HH:MM:SS'.

    Returns:
        int: Le temps total en secondes.
    """
    heures, minutes, secondes = map(int, temps.split(":"))
    total_secondes = heures * 3600 + minutes * 60 + secondes
    return total_secondes

def extract_video_segment(input_path: str, 
                          output_path: str, 
                          start_time: str, 
                          end_time: str) -> str:
    """
    Extrait un segment de vidéo entre deux temps donnés, en prenant en charge les formats de temps HH:MM:SS.

    Args:
        input_path (str): Le chemin du fichier de la vidéo originale.
        output_path (str): Le chemin du fichier où sera sauvegardé l'extrait.
        start_time (str): Le temps de début de l'extrait au format 'HH:MM:SS'.
        end_time (str): Le temps de fin de l'extrait au format 'HH:MM:SS'.

    Returns:
        str: Le chemin du fichier de l'extrait sauvegardé.
    """
    # Charger la vidéo
    video = VideoFileClip(input_path)

    # Définir les temps de début et de fin de l'extrait (en secondes)
    debut = convert_to_seconds(start_time)
    fin = convert_to_seconds(end_time)

    # Découper l'extrait
    extrait = video.subclipped(debut, fin)

    # Sauvegarder l'extrait dans un nouveau fichier
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    extrait.write_videofile(output_path, codec="libx264", audio_codec="aac")

    # Fermer les fichiers pour libérer les ressources
    video.close()
    extrait.close()
    return output_path