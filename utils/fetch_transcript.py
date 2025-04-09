from youtube_transcript_api import YouTubeTranscriptApi
import re

def clean_youtube_transcript(text: str, remove_list=None) -> str:
    """
    Clean transcript text:
    - Unescapes characters like \\' to '
    - Removes unwanted Unicode junk
    - Normalizes whitespace
    """
    # Step 1: Decode double-escaped sequences like \\' => '
    try:
        text = text.encode('latin1').decode('utf-8')
    except Exception:
        pass  # fallback if decoding fails

    # Step 2: Remove unwanted substrings
    if remove_list:
        pattern = "|".join(re.escape(item) for item in remove_list)
        text = re.sub(pattern, ' ', text)

    # Step 3: Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def get_transcript(video_url: str):
    video_id = video_url.split("v=")[-1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    raw_text = " ".join([entry["text"] for entry in transcript])
    remove_list = ["\xa0\n", "\xa0\xa0"]
    cleaned_text = clean_youtube_transcript(raw_text, remove_list)

    return cleaned_text