import tempfile
from typing import Optional, Union
import os
import yt_dlp

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
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "quiet": True,
        "no_warnings": True
    }
    
    # Gestion des cookies
    cookies_path = None
    temp_cookies_file = None
    
    try:
        if cookies_file is not None:
            if isinstance(cookies_file, bytes):
                # Cas Gradio : fichier uploadé (contenu en bytes)
                temp_cookies_file = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False)
                temp_cookies_file.write(cookies_file.decode('utf-8'))
                temp_cookies_file.close()
                cookies_path = temp_cookies_file.name
            elif isinstance(cookies_file, str):
                # Cas fichier local : chemin vers le fichier
                cookies_path = cookies_file
            
            # Ajouter les cookies aux options yt-dlp
            ydl_opts["cookiefile"] = cookies_path
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_path = ydl.prepare_filename(info_dict).replace('.webm', '.mp4')
            
        return video_path
        
    except Exception as e:
        error_msg = str(e)
        if "Sign in to confirm you're not a bot" in error_msg or "Private video" in error_msg:
            raise Exception(f"❌ Vidéo restreinte ou privée. Veuillez fournir un fichier cookies.txt valide. Erreur: {error_msg}")
        else:
            raise Exception(f"❌ Erreur lors du téléchargement: {error_msg}")
            
    finally:
        # Nettoyer le fichier temporaire de cookies
        if temp_cookies_file and os.path.exists(temp_cookies_file.name):
            os.unlink(temp_cookies_file.name)