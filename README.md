# 🤖 Smart Research Assistant

This is a simple yet powerful PDF Question Answering application that allows you to interact with your documents using **local LLMs** like `Phi` or `Mistral` via **Ollama**. It uses `LangChain` for retrieval-augmented generation, `FAISS` for vector indexing, and `HuggingFace` for embeddings — all packed into a clean **Streamlit interface**.

---

## 📌 Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Demo](#demo)
7. [Project Structure](#project-structure)
8. [Credits](#credits)

---

## 📖 Overview

> Upload any PDF, ask questions about its content, and get instant answers — all running **100% locally** on your machine.

This app is designed to be lightweight, fast, and private. It doesn’t rely on OpenAI APIs or cloud services. Perfect for students, researchers, or professionals who want to explore documents using AI without compromising on data privacy.

---

## ✨ Features

- 📄 Upload and process any PDF file
- 💬 Ask natural language questions
- 🧠 Uses **HuggingFace embeddings** + **FAISS** for semantic search
- ⚡ Powered by **local LLMs** (`phi`, `mistral`) via Ollama
- 🔐 Fully offline and private
- 🖥️ Simple and clean **Streamlit** UI

---

## 🧰 Tech Stack

| Tool             | Role                          |
|------------------|-------------------------------|
| LangChain        | Retrieval chain & memory      |
| Ollama + Phi     | Local LLM for generation      |
| FAISS            | Vector similarity search      |
| HuggingFace      | Sentence embeddings           |
| Streamlit        | Web interface                 |
| PyPDFLoader      | Document parsing              |

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/smart-research-assistant.git
cd smart-research-assistant
