import gradio as gr
from video_utils import *
import os

def process_clip(url:str, 
                 start:str, 
                 end:str, 
                 name:str)->tuple[str, str]:
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

def build_interface():
    try:
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
        return demo
    except Exception as e:
        return f"❌ Erreur durant la création de l'interface : {str(e)}"

if __name__ == "__main__":
    build_interface().launch() 