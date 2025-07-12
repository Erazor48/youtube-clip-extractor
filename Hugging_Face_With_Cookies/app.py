import gradio as gr
from video_utils_1 import *
import os
from typing import Optional, Union

def process_clip(url:str, 
                 start:str, 
                 end:str, 
                 name:str,
                 cookies_file: Optional[Union[str, bytes]] = None)->tuple[str, str]:
    status = ""
    if not (url and start and end):
        return "", "❌ Please fill all fields (URL, start, end)."
    try:
        print("Test_1") # Test
        output_dir = os.path.join("tmp", "downloads")
        video_path = download_video(url, output_dir, cookies_file)
        status += f"✅ Video downloaded: {os.path.basename(video_path)}\n"
        print("Test_2", f"❌ Error during download: {str(e)}") # Test
    except Exception as e:
        return "", f"❌ Error during download: {str(e)}"
    try:
        print("Test_3") # Test
        clip_name = name.strip() or f"clip_{start.replace(':', '-')}_{end.replace(':', '-')}"
        clip_name += ".mp4"
        print("Test_4") # Test
        output_path = os.path.join("/tmp/outputs", clip_name)
        extract_video_segment(video_path, output_path, start, end)
        print("Test_5") # Test
        status += f"✅ Extract created: {clip_name}\n"
        status += f"📁 File ready in: outputs/\n"
        print("Test_6", "output_path :", output_path, "status :", status)
        return output_path, status
    except Exception as e:
        return "", f"❌ Error during extraction: {str(e)}"

def build_interface():
    try:
        print("Test_1_1")
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
            with gr.Row():
                cookies_file = gr.File(label="Cookies file (optional)", file_types=["text"])
            btn = gr.Button("🎥 Generate Extract")
            video = gr.Video(label="📺 Extract Result", format="mp4")
            status = gr.Textbox(label="ℹ️ Status", lines=4)
            btn.click(fn=process_clip, inputs=[url, start, end, name, cookies_file], outputs=[video, status])
        return demo
    except Exception as e:
        print(f"❌ Error during interface creation: {str(e)}")
        return f"❌ Error during interface creation: {str(e)}"

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    build_interface().launch() 