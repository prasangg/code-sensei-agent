from utils.model_loader import load_llm
from utils.fetch_transcript import get_transcript
from utils.prompt_engineering import build_prompt

def main():
    video_url = "https://www.youtube.com/watch?v=XYZ"
    transcript_text = get_transcript(video_url)

    llm = load_llm()
    prompt_template = build_prompt("summary")  # or "task", "refactor"

    # ✅ Convert prompt to string
    prompt_value = prompt_template.invoke({"transcript": transcript_text})
    prompt_str = prompt_value.to_string()

    # ✅ Pass string to Llama
    response = llm(prompt_str)
    print(response["choices"][0]["text"])  # or just print(response) for raw output

if __name__ == "__main__":
    main()