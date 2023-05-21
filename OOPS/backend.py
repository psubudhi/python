import openai
from openai.error import RateLimitError


class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_input,
                max_token=1000,
                temperature=0.5
            ).choices[0].text

        except RateLimitError:
            response="RateLimitError You exceeded your current quota, please check your plan and billing details."

        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about bird")
    print(response)
