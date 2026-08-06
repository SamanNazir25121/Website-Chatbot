# Website Knowledge Base RAG Chatbot

An end-to-end Retrieval Augmented Generation (RAG) chatbot project that collects information from a website, processes the extracted content, builds a clean knowledge base, and prepares the data for semantic search and LLM-based question answering.

This project demonstrates a complete RAG pipeline starting from web data collection, document preprocessing, and preparation for embedding generation, vector database storage, and AI chatbot development.

---

# Project Objective

The goal of this project is to build an AI chatbot that can answer domain-specific questions using information retrieved from a custom knowledge base.

Instead of depending only on an LLM's pre-trained knowledge, the system retrieves relevant information from processed documents and provides context to the language model for generating accurate responses.

Example questions:

- What are the main technical areas?
- Explain a specific project.
- What programs or services are available?
- Provide details about a specific topic.
- Summarize available resources.

---

# RAG Pipeline Architecture

```
                 Website Source

                      |
                      v

                URL Discovery

                      |
                      v

                Web Scraping

                      |
                      v

              Text Cleaning Pipeline

                      |
                      v

             Clean Knowledge Base

                      |
                      v

              Document Chunking

                      |
                      v

             Embedding Generation

                      |
                      v

              Vector Database

                      |
                      v

                 LLM Chatbot
```

---

# Project Workflow

## Phase 1: Data Collection

The system collects information from a website by discovering internal pages and extracting useful content.

The crawler identifies different categories of information:

- About information
- Organization details
- Research topics
- Technical domains
- Project information
- Publications
- Reports
- Training information
- Events and resources

---

# Project Structure

```
Website RAG Chatbot/

│
├── main.py
│
├── README.md
│
├── scraper/
│   │
│   ├── __init__.py
│   ├── crawler.py
│   ├── website_scraper.py
│   ├── cleaner.py
│   └── storage.py
│
└── data/
    │
    ├── about_information.txt
    ├── organization_details.txt
    ├── research_topics.txt
    ├── technical_domains.txt
    ├── project_information.txt
    ├── publications_data.txt
    ├── reports_information.txt
    ├── training_information.txt
    └── cleaned documents
```

---

# Implemented Components

## 1. URL Crawler

File:

```
scraper/crawler.py
```

### Purpose

Discovers website pages that need to be processed.

### Responsibilities

- Collect internal website links
- Remove invalid URLs
- Identify available pages
- Prepare URLs for extraction

Flow:

```
Website URL

      |

      v

Discovered Pages
```

---

# 2. Website Scraper

File:

```
scraper/website_scraper.py
```

### Purpose

Extracts readable information from webpage content.

### Implemented Features

- Send HTTP requests
- Download HTML content
- Parse HTML using BeautifulSoup
- Extract useful text

### Removed Elements

- JavaScript
- CSS
- Navigation menus
- Footer content

Flow:

```
URL

 |

 v

HTML Content

 |

 v

Extracted Text
```

---

# 3. Text Cleaning Pipeline

File:

```
scraper/cleaner.py
```

### Purpose

Transforms raw scraped text into clean documents suitable for RAG processing.

### Cleaning Operations

- Remove unnecessary whitespace
- Remove empty lines
- Remove navigation text
- Remove UI elements
- Remove duplicate content


Example:

Before:

```
Home


Read More


Contact Us


Project Information
```


After:

```
Project Information

Detailed project description and relevant information.
```

---

# 4. Document Storage

File:

```
scraper/storage.py
```

### Purpose

Stores processed documents locally.

Generated knowledge base:

```
data/

about_information.txt

research_topics.txt

project_information.txt

training_information.txt
```

---

# Current Data Pipeline

```
main.py

   |
   |
   v

discover_links()

   |
   |
   v

scrape_page()

   |
   |
   v

clean_text()

   |
   |
   v

save_document()

   |
   |
   v

Clean Knowledge Documents
```

---

# Current Output Example

Example processed document:

```
Technical Domain

Project Title

Project description explaining objectives,
methods, technologies, and outcomes.

Additional information related to the topic.
```

---

# Technologies Used

## Programming Language

- Python


## Web Scraping

- Requests
- BeautifulSoup


## Data Processing

- Regular Expressions
- Text Cleaning


## Future RAG Components

Planned:

- Document metadata extraction
- Document chunking
- Sentence Transformer embeddings
- Vector database (Qdrant)
- Similarity search
- LLM integration
- FastAPI backend
- Chat interface

---

# Current Development Status

## Completed

✅ Website crawling  
✅ URL discovery  
✅ HTML extraction  
✅ Text preprocessing  
✅ Noise removal  
✅ Duplicate removal  
✅ Document storage  


## Upcoming

⬜ Metadata generation  
⬜ Document chunking strategy  
⬜ Embedding creation  
⬜ Vector database implementation  
⬜ Retrieval pipeline  
⬜ LLM response generation  
⬜ Chatbot API  
⬜ Evaluation framework  

---

# Future RAG Architecture

```
                User Query

                    |
                    v

            Query Embedding Model

                    |
                    v

             Vector Database

                    |
                    v

          Relevant Document Chunks

                    |
                    v

                  LLM

                    |
                    v

             Final Answer
```

---

# Learning Goals

This project demonstrates practical implementation of:

- Web data ingestion pipelines
- Document preprocessing
- RAG architecture
- Semantic search
- Vector databases
- Embeddings
- LLM applications
- AI chatbot development

---

# Project Goal

Build a production-style RAG chatbot capable of answering domain-specific questions using dynamically collected, processed, and retrieved website information.