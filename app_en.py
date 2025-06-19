import gradio as gr
from video_utils import *
import os

def process_clip(url:str, 
                 start:str, 
                 end:str, 
                 name:str)->tuple[str, str]:
    """
    Processes a YouTube video to extract a clip between specified start and end times.

    Args:
        url (str): The URL of the YouTube video to download.
        start (str): The start time for the clip in 'HH:MM:SS' format.
        end (str): The end time for the clip in 'HH:MM:SS' format.
        name (str): The optional name for the extracted clip file.

    Returns:
        tuple[str, str]: A tuple where the first element is the path to the extracted
        video clip file, and the second element is a status message indicating success
        or any errors encountered.

    Raises:
        Exception: If there is an error during video download or clip extraction.
    """

    status = ""
    
    if not (url and start and end):
        return "", "❌ Please fill all fields (URL, start, end)."

    try:
        video_path = download_video(url)
        status += f"✅ Video downloaded: {os.path.basename(video_path)}\n"
    except Exception as e:
        return "", f"❌ Error during download: {str(e)}"

    try:
        clip_name = name.strip() or f"clip_{start.replace(':', '-')}_{end.replace(':', '-')}"
        clip_name += ".mp4"
        output_path = os.path.join("outputs", clip_name)

        extract_video_segment(video_path, output_path, start, end)
        status += f"✅ Extract created: {clip_name}\n"
        status += f"📁 File ready in: outputs/\n"
        return output_path, status

    except Exception as e:
        return "", f"❌ Error during extraction: {str(e)}"


with gr.Blocks(title="🎞️ YouTube Clip Extractor") as demo:
    gr.Markdown("""
    # 🎬 YouTube Clip Extractor
    Enter a YouTube video URL, **start** and **end** times, then get a clip with the same quality as the original video.
    """)

    with gr.Row():
        url = gr.Textbox(label="YouTube Video URL", placeholder="https://www.youtube.com/watch?v=...")
        name = gr.Textbox(label="Extract file name (optional)", placeholder="Clip_Rick_Astley")

    with gr.Row():
        start = gr.Textbox(label="Start time (HH:MM:SS)", placeholder="00:01:30")
        end = gr.Textbox(label="End time (HH:MM:SS)", placeholder="00:03:45")

    btn = gr.Button("🎥 Generate Extract")
    video = gr.Video(label="📺 Extract Result", format="mp4")
    status = gr.Textbox(label="ℹ️ Status", lines=4)

    btn.click(fn=process_clip, inputs=[url, start, end, name], outputs=[video, status])


if __name__ == "__main__":
  demo.launch() 