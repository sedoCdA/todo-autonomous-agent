
# Autonomous AI Agent with FastAPI & Groq

## Overview

This project implements a simple autonomous AI agent that accepts a natural language request, creates its own execution plan, completes the required tasks, performs a self-check, and generates a professional Microsoft Word (`.docx`) document.

The project was built as part of a Python AI Engineer autonomous agent assignment and demonstrates autonomous planning, reasoning, document generation, and REST API development.

---

## Features

* FastAPI REST API
* Autonomous task planning using an LLM
* Multi-step execution workflow
* Reflection (self-check) before returning results
* Microsoft Word document generation (`.docx`)
* Clean and modular Python architecture
* Uses Groq's free LLM API

---

## Project Structure

```text
autonomous-agent/
│
├── app.py                 # FastAPI application
├── planner.py             # Generates execution plan (TODO list)
├── executor.py            # Executes the generated plan
├── reflection.py          # Reviews generated output
├── document.py            # Creates Word document
├── outputs/
│   └── report.docx
├── requirements.txt
├── .env
└── README.md
```

---

## Architecture

```text
                 User Request
                      │
                      ▼
              POST /agent (FastAPI)
                      │
                      ▼
                 Planner (LLM)
            Creates TODO / Task List
                      │
                      ▼
                Executor (LLM)
        Executes tasks and generates content
                      │
                      ▼
           Reflection / Self-Check
      Validates completeness of the document
                      │
                      ▼
            Word Document Generator
                      │
                      ▼
             outputs/report.docx
```

---

## Technologies Used

* Python
* FastAPI
* Groq API
* python-docx
* Pydantic
* Uvicorn
* python-dotenv

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd autonomous-agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```text
GROQ_API_KEY=your_groq_api_key
```

---

## Running the Application

Start the FastAPI server:

```bash
uvicorn app:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

Swagger UI will be available for testing the API.

---

## API Endpoint

### POST `/agent`

Request

```json
{
    "request": "Create a project proposal for an Employee Leave Management System."
}
```

Example Response

```json
{
    "request": "...",
    "plan": "...",
    "review": "APPROVED",
    "document": "outputs/report.docx"
}
```

---

## Sample Test Cases

### Test Case 1 – Standard Business Request

```json
{
    "request":"Create a project proposal for developing an Employee Leave Management System."
}
```

---

### Test Case 2 – Complex Request

```json
{
    "request":"Create a technical design document for migrating our HR platform to the cloud. Budget is limited, timeline is unclear, and several requirements are missing. Make reasonable assumptions and generate a complete document."
}
```

---

## Autonomous Agent Workflow

1. Receive the user's request.
2. Generate an execution plan (TODO list).
3. Execute each planned task.
4. Review the generated content using a reflection step.
5. Generate a Microsoft Word document.
6. Return the execution plan, review status, and document path.

---

## Engineering Improvement

### Reflection / Self-Check

The project implements a reflection step after document generation.

The reflection agent reviews the generated document and checks:

* Completeness
* Logical structure
* Missing sections
* Reasonable assumptions

If the document satisfies these checks, it returns **APPROVED**; otherwise, it identifies missing or incomplete areas.

This improves the reliability and quality of the generated output.

---

## Future Improvements

* Conversation memory
* Retrieval-Augmented Generation (RAG)
* Tool calling
* Multi-agent architecture
* Automatic regeneration if reflection fails
* PDF export
* Cloud storage integration
* Authentication and authorization

---

## License

This project is intended for educational and demonstration purposes.
