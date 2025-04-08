# 🧠 CodeSensei Agent

> ⚡ A domain-aware AI agent that transforms YouTube coding content into actionable coding insights — powered by open-source LLMs and LangChain.

![Python](https://img.shields.io/badge/Built_with-Python-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-💬-green.svg)
![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Model](https://img.shields.io/badge/Model-Nous--Hermes--2--Mixtral-red.svg)

---

## 🚀 What is CodeSensei?

**CodeSensei** is an agentic AI system that:
- 🎥 Extracts technical insights from YouTube coding tutorials
- 🧠 Uses LLM agents to debug, summarize, and explain programming content
- 🧪 Provides explanations and code snippets for better understanding
- 🤖 Fully customizable for any coding domain

This project is built using:
- 🦙 `llama-cpp-python` (GPU-compatible)
- 🧩 `LangChain`
- 📄 YouTube transcript parsing
- 🔍 Agent-based modular reasoning

---

## ✨ Features

| Feature             | Description |
|---------------------|-------------|
| 📜 Transcript Parsing | Automatically pulls and cleans YT transcripts |
| 🧠 Code Summarizer   | Creates short and detailed summaries |
| 🐞 Bug Hunter Agent  | Identifies bugs and suggests code fixes |
| 📘 Concept Tutor     | Explains complex programming topics |
| 🧩 Modular Agent Flow| Easily plug new tools and chains |

---

## 🧰 Tech Stack

- 🐍 Python 3.10+
- ⚛️ LangChain
- 🦙 llama-cpp-python (GGUF)
- 🧠 TheBloke/Nous-Hermes-2-Mixtral-8x7B-SFT-GGUF
- 🚀 Google Colab (GPU runtime)
- 📄 YouTubeTranscriptAPI

---

## ⚡ Quickstart (Colab)

```bash
git clone https://github.com/your-username/code-sensei-agent.git
cd code-sensei-agent
pip install -r requirements.txt
# or use the Colab notebook (recommended)
