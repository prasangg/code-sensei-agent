from utils.fetch_transcript import get_transcript
from utils.model_loader import load_llm
from utils.prompt_engineering import build_prompt
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda

def main():
    # Step 1: Get YouTube transcript
    video_url = "https://www.youtube.com/watch?v=TjthKf7Mc_8"  # Replace with your video
    transcript_text = get_transcript(video_url)

    # Optional: truncate to avoid context overflow
    max_chars = 3000  # tune this if needed
    transcript_text = transcript_text[:max_chars]

    # Step 2: Load model
    llm = load_llm()

    prompt = build_prompt("summary")
    chain = prompt | llm

    # Step 5: Run the model
    response = chain.invoke({"transcript": transcript_text})

    # Step 6: Display output
    print("\n📌 Final Output:")
    print(response)

if __name__ == "__main__":
    main()
