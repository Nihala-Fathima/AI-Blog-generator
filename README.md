# AI Blog Generator 

A simple Python-based AI Blog Generator that uses the OpenAI API to generate paragraphs based on a topic provided by the user.

## What It Does

The program:

- Asks the user if they want to generate a paragraph.
- Takes a topic as input.
- Sends the topic to the OpenAI API.
- Generates an AI-written paragraph.
- Displays the generated paragraph in the terminal.
- Allows the user to generate multiple paragraphs.

## Technologies Used

- Python 3
- OpenAI Python SDK
- OpenAI API
- Git
- GitHub

## Installation
## 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/AI-Blog-generator.git
```
## 2. Navigate to the project directory
```bash
cd AI-Blog-generator
```
## 3. Install the OpenAI Python SDK
```bash
pip3 install --upgrade openai
```

## OpenAI API Key Setup
The application requires an OpenAI API key.
Set your API key as an environment variable.
## macOS / Linux
export OPENAI_API_KEY="your-api-key-here"
The program uses the key through:
```python
from openai import OpenAI
client = OpenAI()
```
** Important: Never add your API key directly to the Python file or commit it to GitHub.

## How to Run
Run the following command:
```bash
python3 blog_generator.py
```
The program will ask:
```text
Write a paragraph? Y for yes, anything else for no. Y
What should this paragraph talk about? Kerala
```

## Example Output
```text
Write a paragraph? Y for yes, anything else for no. Y
What should this paragraph talk about? Kerala
```

Kerala is a beautiful state in southern India, known for its lush
green landscapes, peaceful backwaters, rich culture, and diverse
traditions. It is often called "God's Own Country" and is a popular
destination for travelers from around the world.

Write a paragraph? Y for yes, anything else for no.
