from google import genai
from dotenv import load_dotenv
import os
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY")
)

def generate_blog(topic, audience,tone,word_count,keywords):
    prompt = f"""You are an expert blog writer.

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
        model="gemini-3.7-flash",
    contents=prompt)
    return response.text
    
def get_user_input():
    print("\n========== AI BLOG GENERATOR ===========\n")
    topic = input("What is the topic?")

    audience = input("Who is the target audience?")
    tone = input("What tone should the blog have? "
        "(Professional / Friendly / Academic / Casual):")

    word_count = input("Approximate word count (e.g. 500, 1000, 1500): ")

    keywords = input("Enter keywords separated by commas:")

    return topic, audience, tone, word_count, keywords


def main():
   while True:

      answer = input("\nDo you want to generate a blog? "
            "Y for yes, anything else to exit: ")

      if answer.upper() != 'Y':
          print("Goodbye!")
          break


      topic, audience, tone, word_count, keywords = get_user_input()

      print("\nGenerating your blog...\n")

      try:
            blog = generate_blog(
                topic,
                audience,
                tone,
                word_count,
                keywords
            )

            print("\n========== GENERATED BLOG ==========\n")
            print(blog)

      except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
