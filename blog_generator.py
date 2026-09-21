from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_blog(topic, audience, tone, word_count, keywords):

    prompt = f"""
You are an expert blog writer.

Create a high quality blog article using the following requirements:

Topic: {topic}
Target audience: {audience}
Tone: {tone}
Approximate word count: {word_count}
Keywords: {keywords}

Structure the response as:

1. An engaging title
2. Introduction
3. A clear blog outline
4. Full blog article with appropriate headings
5. Conclusion

Requirements:
- Make the content informative and original.
- Use clear and readable language.
- Naturally incorporate the provided keywords.
- Keep the article close to the requested word count.
- Use Markdown headings.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    return response.text


print("\nAvailable Gemini models:\n")

for model in client.models.list():
    print(model.name)