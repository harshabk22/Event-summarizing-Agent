# Event-summarizing-Agent

## Overview

The AI Intelligence Agent is a command-line application designed to generate structured, fact-based intelligence reports on geopolitical topics and current events. It leverages a large language model with integrated web search capabilities to retrieve up-to-date information and present it in a clear, organized format.

The system enforces strict output constraints to ensure that responses remain objective, structured, and grounded in verifiable events.

---

## Features

* Topic-based intelligence report generation
* Integration with real-time web search for up-to-date information
* Structured output with clearly defined sections
* Deterministic responses through low-temperature configuration
* Command-line interface for interactive usage
* Input validation and graceful error handling

---

## System Behavior

The agent operates with a predefined system instruction that enforces:

* Separation of output into:

  * Historical Context
  * Current Events
* Inclusion of specific events and dates
* Avoidance of opinions, commentary, or speculation
* Focus on factual and verifiable information

---

## Technology Stack

* Language: Python
* AI Model: Google Gemini (gemini-2.5-flash)
* SDK: google-genai
* External Tooling: Google Search integration via model tools

---

## Project Structure

agent.py – Main script containing agent logic and execution loop

---

## Setup and Installation

1. Install required dependencies:
   pip install google-generativeai

2. Set your API key as an environment variable:
   export GEMINI_API_KEY="your_api_key_here"

3. Run the application:
   python agent.py

---

## Usage

1. Launch the program
2. Enter a topic or event when prompted
3. The agent will generate a structured intelligence report
4. Type `exit` to terminate the session

---

## Example Use Cases

* Understanding geopolitical conflicts
* Tracking ongoing global events
* Generating structured timelines for research
* Rapid briefing preparation

---

## Author

Harsha

