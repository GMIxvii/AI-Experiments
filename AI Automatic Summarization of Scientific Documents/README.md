Here is a short, structured, and clear README for your project:

---

# AI Scientific Document Summarizer

An automated system designed to handle large scientific PDFs and generate concise summaries using the **Document Chain Refine Method**. The system is built with **LangChain**, **LangGraph**, and **Hugging Face** transformers.

---

## 🚀 Key Features

* **Refine Method Strategy**: Sequential document processing that constructs a running summary state, allowing you to bypass strict LLM context window limits.
* **Translation Support**: Automated English-to-French translation node built directly into the graph.
* **State-Graph Pipeline**: Orchestrated workflow managed by `LangGraph` for reliable, step-by-step logic execution and state tracking.
* **Hugging Face Integration**: Employs `facebook/bart-large-cnn` for extraction/summarization and `Helsinki-NLP/opus-mt-en-fr` for translation.

---

## 🛠️ Installation

Install the required Python dependencies:

```bash
pip install langchain-huggingface transformers huggingface_hub langgraph langchain_community langchain-text-splitters pymupdf

```

---

## 🗺️ How it Works (The Graph)

```
[START] ──> [Generate Initial Summary] ──> [Should Refine?] 
                                                  │
                   ┌──────────────────────────────┴──────────────┐
                   ▼                                             ▼
            [Refine Summary]                              [Translate Summary] ──> [END]

```

1. **Document Management**: Reads your target PDF and splits it into precise chunks (using `max_tokens` constraints to prevent truncation).
2. **Initial Summary**: Generates a summary of the first text chunk.
3. **Sequential Refinement**: Recursively feeds the current summary + the next text chunk back to the model until all chunks are processed.
4. **Translation**: Translates the final refined English summary into French.

---

## 💻 Quick Start

```python
# 1. Load your PDF document
from langchain_community.document_loaders import PyMuPDFLoader
loader = PyMuPDFLoader("/path/to/your/document.pdf")
content = loader.load()
text = ''.join(page.page_content for page in content)

# 2. Split your text to fit the model's token limits
from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(chunk_size=944, chunk_overlap=100)
texts_chunks = text_splitter.create_documents([text])

# 3. Run the compiled LangGraph App (assuming Graph setup is complete)
inputs = {
    "contents": [chunk.page_content for chunk in texts_chunks],
    "index": 0,
    "summary": ""
}
result = await summarizer_app.ainvoke(inputs)

print("English Summary:", result["summary"])
print("French Translation:", result["translation"])

```

---

## ⚠️ Limitations

* **Processing Speed**: Can be slower than batch parallel processing for small texts due to its sequential nature.

---

*For more information on the underlying strategy, consult the [LangChain Refine Docs Chain guide](https://python.langchain.com/docs/versions/migrating_chains/refine_docs_chain/).*