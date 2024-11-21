# Langchain Icebreaker

Langchain Icebreaker is an AI-powered application that generates personalized icebreaker information from LinkedIn profiles. Utilizing Langchain and OpenAI's GPT models, it automates the creation of bios, interesting facts, and more.

## 📊 Project Overview

- **Langchain Integration**  
  ██████████████████████████████ (100%)

- **LinkedIn Profile Scraping**  
  ██████████████████████████░░░░ (90%)

- **AI-Generated Summaries**  
  ██████████████████████████████ (100%)

- **Fullstack Web Application**  
  ██████████████████████░░░░░░░░ (80%)

## 🚀 Getting Started

### Installation

1. **Clone the Repository**
    ```bash
    git clone https://github.com/yourusername/langchain-icebreaker.git
    cd langchain-icebreaker
    ```

2. **Set Up Environment**
    - Create a `.env` file and add your API keys:
      ```env
      OPENAI_API_KEY=your_openai_api_key
      PROXYCURL_API_KEY=your_proxycurl_api_key
      LANGCHAIN_API_KEY=your_langchain_api_key
      LANGCHAIN_TRACING_V2=true
      LANGCHAIN_PROJECT=ice_breaker
      ```

3. **Install Dependencies**
    ```bash
    conda activate
    conda install langchain -c conda-forge
    pip install langchain-openai black python-dotenv
    ```

4. **Run the Application**
    ```bash
    black .
    python app.py
    ```

## 🛠 Features

- **LinkedIn Profile Scraping**  
  Retrieves detailed LinkedIn profile information using Proxycurl API.

- **AI-Powered Summaries**  
  Generates bios, interesting facts, MBTI types, and more with Langchain and GPT-3.5-turbo.

- **Interactive Web Interface**  
  User-friendly frontend built with Flask displaying profile pictures and summaries.

- **ReAct Agents**  
  Implements reasoning and acting for enhanced data retrieval and tool utilization.

## 📈 Usage Statistics

- **API Calls Tracked by Langsmith**  
  █████████████████████████████ (100%)

- **User Interactions Processed**  
  █████████████████████████████ (100%)

- **Response Accuracy**  
  █████████████████████████████ (100% I hope 🤞)

## 📸 Screenshots

![App Screenshot](https://github.com/stevenzhang070302/icebreaker/blob/main/1.png)
![App Screenshot](https://github.com/stevenzhang070302/icebreaker/blob/main/2.png)
![Agent Reasoning Screenshot](https://github.com/stevenzhang070302/icebreaker/blob/main/3.png)

## 🔧 Technologies Used

- **Backend:** Python, Flask, Langchain, OpenAI GPT
- **Frontend:** HTML, CSS, JavaScript
- **APIs:** Proxycurl, Langsmith, Tavily

## 📈 Langsmith Integration

Tracks LLM calls, tool usage, latency, token count, and cost for efficient monitoring.


