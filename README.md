# 🕵️‍♂️ Log Lurker

**An AI-powered security assistant that finds the needle in the haystack of your logs.**

Log Lurker uses AI to learn the "normal" behavior of your system logs. It identifies potential threats by flagging entries that are statistical outliers and then uses a local LLM to explain *why* they are suspicious in plain English.

---

## 🔧 How It Works

1.  **Ingest & Understand** Transforms raw, cryptic log lines into structured, meaningful sentences.
2.  **Detect Anomalies** Converts sentences into numerical vectors ("embeddings") to find statistical outliers that deviate from the normal baseline.
3.  **Explain in Plain English** Uses a local, privacy-focused LLM (like **Gemma** or **Llama**) to generate a human-readable explanation of the threat.

---

## ✨ Features

* 🧠 **Unsupervised Detection**: Learns what's normal for *your* environment without needing pre-labeled attack data.
* 🤖 **Natural Language Explanations**: No more cryptic codes; get clear, concise threat descriptions.
* 🧩 **Adaptable**: Works with any log format that can be structured into a sentence (e.g., Apache, network flows).
* 🔒 **Privacy-Focused**: The entire analysis runs **locally**. Your sensitive log data never leaves your control.

---

## 🛠️ Tech Stack

* **AI/ML**: `PyTorch`, `Hugging Face (transformers, sentence-transformers)`
* **Data**: `pandas`, `numpy`, `scikit-learn`
* **Backend**: `Python`

---

## 🚀 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/log-lurker.git](https://github.com/your-username/log-lurker.git)
    cd log-lurker
    ```

2.  **Install the requirements:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Login to Hugging Face:**
    ```bash
    huggingface-cli login
    ```

4.  **Run the project:**
    ```bash
    python main.py
    ```

---

## 📈 Project Status

* ✅ **Phase 1: Complete** Core engine for parsing, embedding, and finding outliers.
* ⏳ **Phase 2: In Progress** Integrating a local LLM for natural language explanations.
* 💡 **Phase 3: Future Add-ons** Building a simple web UI for real-time analysis.