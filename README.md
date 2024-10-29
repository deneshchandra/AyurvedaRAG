# RAG Project: Retrieval-Augmented Generation with LangChain, Chroma, and Ollama

This project is a Retrieval Augmented Generation (RAG) application, using LangChain, Chroma, and Ollama to answer questions based on embedded knowledge from Ayurveda textbook documents. It uses document embeddings stored in a Chroma vector database, enabling efficient and accurate retrieval for various health related queries. 

## Project Structure

- **embedding.py**: Defines and initializes embedding functions.
- **popdatabase.py**: Loads documents, splits them into chunks, embeds them, and stores them in Chroma.
- **query.py**: Provides the main query functionality to retrieve information from the vector database and generate responses.
- **testrag.py**: Runs unit tests to validate response accuracy for specific questions.
- **requirements.txt**: Lists all required packages.
- **data/**: Folder containing the Ayurveda documents (PDFs) for embedding and retrieval.
- **chroma/**: Directory where Chroma stores embeddings and metadata.

## Features

- **Document Embeddings**: Utilizes Bedrock or Ollama embeddings to transform document text into vector space.
- **PDF Loader**: Extracts text from PDFs stored in the `data/` folder.
- **Text Splitting**: Splits documents into manageable chunks for efficient search and retrieval.
- **Vector Database**: Stores document embeddings in Chroma for fast similarity searches.
- **RAG Querying**: Combines retrieved document context with the Ollama model to generate accurate answers.
- **Unit Testing**: Validates model responses against expected answers for specific test cases.

## Setup

### 1. Prerequisites

- Python 3.8+
- An AWS account with a configured profile for Bedrock (optional, if using Bedrock embeddings)
- Access to the `mistral` model from Ollama

### 2. Installation

Clone the repository, create a virtual environment, and install dependencies

###3. Configure AWS (Optional)
- If using AWS Bedrock embeddings, configure your AWS credentials:

```bash
aws configure --profile default
```

# Usage

## Embedding Documents

1. Add PDF files to the `data/` directory.
2. Run `popdatabase.py` with the `--reset` flag to clear and rebuild the database.

## Querying

- Use `query.py` to input questions, retrieve related document context, and generate answers.
- Customize the prompt template in `query.py` as needed for different query contexts.

## Testing

- Customize `testrag.py` to add or modify test cases, especially useful for validating responses on specific queries.

# Advanced Deployment Options

- **Docker**: Optionally containerize the application for deployment on cloud or container orchestration platforms.
- **Serve as API**: Integrate Flask or FastAPI to serve `query_rag()` as an endpoint, enabling HTTP based query submissions.

# License

MIT License

---
