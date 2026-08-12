# 🎬 Class 09-10 — Structured Output & Tools Deep Dive: Building CineBot
**📅 25-26 July 2026** · Agentic AI 3.0 Specialization · Mentor: Mayank Aggarwal

📖 **[Class 09 summary →](<../classes_summary/09 - 25 Jul - Structured Output Mastery.md>)** · **[Class 10 summary →](<../classes_summary/10 - 26 Jul - Tools Deep Dive.md>)**

```mermaid
flowchart LR
    A["😩 Free text —<br/>unpredictable shape"] --> B["📐 with_structured_output()<br/>+ Pydantic"] --> C["🛠️ @tool + ToolRuntime"] --> D["🎬 CineBot"]
    style D fill:#22c55e,color:#fff
```

Two weekends taught through one running project — **CineBot**, a movie-ticket booking agent — covering structured output (`with_structured_output`, `Union` schemas, automatic error recovery) and a full deep-dive into tools (`@tool`, `args_schema`, reserved `config`/`runtime` names, `ToolRuntime`, and memory-backed tools).

## 📂 What's Here

| Path | Class | Covers |
|---|---|---|
| [`Langchain_Structured_OUTPUT_COLAB.ipynb`](<Langchain_Structured_OUTPUT_COLAB.ipynb>) | 09 | CineBot structured output, `Union` intents, error recovery |
| [`Langchain-Tools.ipynb`](<Langchain-Tools.ipynb>) | 10 | `@tool`, `args_schema`, `ToolRuntime`, memory-backed tools |
| [`Langchain_Till_Agents.ipynb`](<Langchain_Till_Agents.ipynb>) | 09-10 | Consolidated: everything through tools |
| [`Assignment & Questions/`](<Assignment & Questions/>) | 10 | Practical assignment + real interview questions |

🔗 Live Colab used in class: [CineBot — Movie Ticket Booking Assistant](https://colab.research.google.com/drive/1BfYVnjabM0BYL0Wr6zqabdFCn6-Waz-T?usp=sharing)

---
⬅️ [Class 07-08](<../07-08 - 18-19 Jul - LangChain Family & the Model Layer/README.md>) · [Course index](<../README.md>) · ➡️ [Class 11-12](<../11-12 - 1-8 Aug - Agents, Memory & Middleware/README.md>)
