# utils/prompt_engineering.py

from langchain.prompts import ChatPromptTemplate

# Prompt for summarizing technical sections of transcripts
summary_prompt = ChatPromptTemplate.from_template("""
You are an AI assistant skilled in understanding coding-related content.
Given the following YouTube transcript, identify the main coding concepts, problem statements, or techniques discussed.

Transcript:
{transcript}

Respond in bullet points.
""")

# Prompt for extracting coding problem + solution
code_task_prompt = ChatPromptTemplate.from_template("""
Given the following transcript section, extract any coding problems discussed.
If a solution is provided or implied, extract that as well.

Transcript:
{transcript}

Respond in this format:
**Problem:** <summary>
**Approach:** <how it was solved>
**Code (if any):** <pseudo code or real code if mentioned>
""")

# Prompt for suggesting improvements or optimizations
refactor_prompt = ChatPromptTemplate.from_template("""
Act as a senior developer. Analyze the transcript below for code improvement ideas, performance optimizations, or better practices.

Transcript:
{transcript}

Respond with suggestions.
""")
