from openai import OpenAI
client = OpenAI()

def generate_blog(paragraph_topic):
    
    response = client.responses.create(
        model = 'gpt-5.2',
        input = 'write a paragraph about the following topic.' + paragraph_topic,
        max_output_tokens = 400,
        temperature = 1.3
    )
    retrieve_blog = response.output_text
    return retrieve_blog

keep_writing = True
while keep_writing:
  answer = input('Write a paragraph? Y for yes, anything else for no. ')
  if (answer == 'Y'):
    paragraph_topic = input('What should this paragraph talk about? ')
    print(generate_blog(paragraph_topic))
  else:
    keep_writing = False