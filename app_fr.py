import gradio as gr
from video_utils import *
import os

def process_clip(url:str, 
                 start:str, 
                 end:str, 
                 name:str)->tuple[str, str]:
    """
    Traite une vidéo YouTube pour extraire un clip entre les heures de début et de fin spécifiées.

    Args:
        url (str): L'URL de la vidéo YouTube à télécharger.
        start (str): L'heure de début du clip au format 'HH:MM:SS'.
        end (str): L'heure de fin du clip au format 'HH:MM:SS'.
        name (str): Le nom optionnel du fichier extrait.

    Returns:
        tuple[str, str]: Un tuple où le premier élément est le chemin vers le fichier
        vidéo extrait, et le second élément est un message de statut indiquant le succès
        ou les erreurs rencontrées.

    Raises:
        Exception: S'il y a une erreur pendant le téléchargement ou l'extraction.
    """

    status = ""
    
    if not (url and start and end):
        return "", "❌ Merci de remplir tous les champs (URL, début, fin)."

    try:
        video_path = download_video(url)
        status += f"✅ Vidéo téléchargée : {os.path.basename(video_path)}\n"
    except Exception as e:
        return "", f"❌ Erreur pendant le téléchargement : {str(e)}"

    try:
        clip_name = name.strip() or f"clip_{start.replace(':', '-')}_{end.replace(':', '-')}"
        clip_name += ".mp4"
        output_path = os.path.join("outputs", clip_name)

        extract_video_segment(video_path, output_path, start, end)
        status += f"✅ Extrait créé : {clip_name}\n"
        status += f"📁 Fichier prêt dans : outputs/\n"
        return output_path, status

    except Exception as e:
        return "", f"❌ Erreur pendant l'extraction : {str(e)}"


with gr.Blocks(title="🎞️ Extracteur de Clip YouTube") as demo:
    gr.Markdown("""
    # 🎬 Extracteur de Clip YouTube
    Entrez l'URL d'une vidéo YouTube, l'heure de **début** et **fin**, puis récupérez un extrait avec la même qualité que la vidéo originale.
    """)

    with gr.Row():
        url = gr.Textbox(label="URL de la vidéo YouTube", placeholder="https://www.youtube.com/watch?v=...")
        name = gr.Textbox(label="Nom du fichier extrait (optionnel)", placeholder="Clip_Rick_Astley")

    with gr.Row():
        start = gr.Textbox(label="Heure de début (HH:MM:SS)", placeholder="00:01:30")
        end = gr.Textbox(label="Heure de fin (HH:MM:SS)", placeholder="00:03:45")

    btn = gr.Button("🎥 Générer l'extrait")
    video = gr.Video(label="📺 Résultat de l'extrait", format="mp4")
    status = gr.Textbox(label="ℹ️ Statut", lines=4)

    btn.click(fn=process_clip, inputs=[url, start, end, name], outputs=[video, status])


if __name__ == "__main__":
  demo.launch() 