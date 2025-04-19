from langchain_core.prompts import ChatPromptTemplate
from utils.model_loader import load_llm
from utils.fetch_transcript import get_transcript
from utils.prompt_engineering import summary_prompt

def main():
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    transcript_text = get_transcript(video_url)

    llm = load_llm()

    # 1. Format the prompt manually
    prompt_value = summary_prompt.format(transcript=transcript_text)

    # 2. Extract text from the ChatPromptValue object
    formatted_prompt = prompt_value.to_string()

    # 3. Pass it directly to the model
    response = llm(formatted_prompt)

    print("🧠 Response:\n", response["choices"][0]["text"])

if __name__ == "__main__":
    main()
