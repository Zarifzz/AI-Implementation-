import json
from openai import OpenAI


def load_json_key(file_path):
    with open(file_path, 'r') as f:
        config = json.load(f)
        api_key = config['openai_key']
    return api_key


client = OpenAI(
    # This is the default and can be omitted
    api_key=load_json_key("Api_Key.json"),
)



def chat_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role" : "user", "content" : prompt}]
    )

    return response.choices[0].message.content.strip(), response.usage.total_tokens


if __name__ == "__main__":

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            break

        response, tokens_used = chat_gpt(user_input)
        print("Chatbot: ", response, "Tokens used: ", tokens_used)



