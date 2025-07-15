import yt_dlp
from moviepy.video.io.VideoFileClip import VideoFileClip
import os
from typing import Optional, Union

def download_video(url: str, output_dir: Optional[str] = "downloads", cookies_file: Optional[Union[str, bytes]] = None) -> str:
    """
    Downloads a video from a given URL and saves it to the specified directory.
    
    Args:
        url (str): The URL of the video to download.
        output_dir (str): The directory where the downloaded video will be saved. Defaults to 'downloads'.
        cookies_file (Optional[Union[str, bytes]]): Path to cookies file or cookies file content. 
                                                   Can be a file path (str) or file content (bytes from Gradio file upload).
                                                   If None, downloads without cookies (limited to non-restricted videos).
    
    Returns:
        str: The path to the downloaded video file.
    
    Raises:
        Exception: If download fails (e.g., restricted video without proper cookies).
    """
    os.makedirs(output_dir, exist_ok=True)
    
    ydl_opts = {
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        #"format": "bestvideo+bestaudio/best",
        #"merge_output_format": "mp4",
        """extractor_args": {
            "youtube": {
                "player_client": ["web"],
                "skip": ["dash", "hls"]
            }
        },"""
        "verbose": True,
        "quiet": False,
        "no_warnings": False
    }
    
    try:
        # Gestion des cookies
        if cookies_file is not None:
            os.makedirs("tmp", exist_ok=True)
            cookies_path = os.path.join("tmp", "cookies.txt")
            
            # Lire le contenu du fichier uploadé via Gradio
            with open(cookies_file, 'r', encoding='utf-8') as f:
                cookies_content = f.read()
            
            # Écrire le contenu dans le fichier temporaire
            with open(cookies_path, 'w', encoding='utf-8') as f:
                f.write(cookies_content)
            
            # Ajouter les cookies aux options yt-dlp
            ydl_opts["cookiefile"] = cookies_path
        
        print("ydl_opts:", ydl_opts)

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("A1")
            info_dict = ydl.extract_info(url, download=True)
            print("A2")
            video_path = ydl.prepare_filename(info_dict).replace('.webm', '.mp4')
        print("A3:", video_path)
        return video_path
        
    except Exception as e:
        error_msg = str(e)
        if "Sign in to confirm you're not a bot" in error_msg or "Private video" in error_msg:
            raise Exception(f"❌ Vidéo restreinte ou privée. Veuillez fournir un fichier cookies.txt valide. Erreur: {error_msg}")
        else:
            raise Exception(f"❌ Erreur lors du téléchargement: {error_msg}")
        
        
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