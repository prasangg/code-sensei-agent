from langchain.prompts import ChatPromptTemplate

def build_prompt(prompt_type="summary"):
    if prompt_type == "summary":
        return ChatPromptTemplate.from_template("""
        You are an AI assistant skilled in understanding coding-related content.
        Given the following YouTube transcript, identify the main coding concepts, problem statements, or techniques discussed.

        Transcript:
        {transcript}

        Respond in bullet points.
        """)
    elif prompt_type == "task":
        return ChatPromptTemplate.from_template("""
        Given the following transcript section, extract any coding problems discussed.
        If a solution is provided or implied, extract that as well.

        Transcript:
        {transcript}

        Respond in this format:
        **Problem:** <summary>
        **Approach:** <how it was solved>
        **Code (if any):** <pseudo code or real code if mentioned>
        """)
    elif prompt_type == "refactor":
        return ChatPromptTemplate.from_template("""
        Act as a senior developer. Analyze the transcript below for code improvement ideas, performance optimizations, or better practices.

        Transcript:
        {transcript}

        Respond with suggestions.
        """)
    else:
        raise ValueError("Invalid prompt_type passed. Use 'summary', 'task', or 'refactor'.")

# 