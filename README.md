# POC: Datatable Analysis

This project demonstrates how to leverage **Large Language Models (LLMs)** for analyzing data tables.

## Available LLM Options

You can choose between a **free** model (Llama3.2 via Ollama) or a **purchased** model (ChatGPT via OpenAI API).

---

## Option 1: Using a Free LLM Model (Llama3.2)

Ollama provides access to various LLMs. You can explore the available models in the [Ollama Library](https://ollama.com/library).

For this setup, we will use **Llama3.2**, a lightweight and efficient model.

### 1. Install Ollama

Download and install Ollama from the official website:

[Download Ollama](https://ollama.com/download)

### 2. Pull the Llama3.2 Model

Once Ollama is installed, pull the **Llama3.2** model using the following command:

```bash
ollama pull llama3.2
```

## Option 2: Using a Purchased LLM Model (ChatGPT)
If you prefer to use ChatGPT via OpenAI’s API, follow these steps:

### Configure API Access
Copy the .env.example file and rename it to .env.
Update the .env file with your OpenAI API key and other relevant values.
