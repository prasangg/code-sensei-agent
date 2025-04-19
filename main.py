from langchain_core.prompts import ChatPromptTemplate
from utils.model_loader import load_llm
from utils.fetch_transcript import get_transcript
from utils.prompt_engineering import build_prompt

def main():
    video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    transcript_text = get_transcript(video_url)

    llm = load_llm()

    # Choose your type of analysis here
    prompt = build_prompt("summary")  # or "task", or "refactor"
    chain = prompt | llm

    # 3. Pass it directly to the model
    response = chain.invoke({"transcript": transcript_text})  # ✅ this is correct
    print(response)

    print("🧠 Response:\n", response["choices"][0]["text"])

if __name__ == "__main__":
    main()
