import openai


class ChatGPT:
    def __init__(self, openai_key, openai_org, model='gpt-3.5-turbo'):
        self.openai_key = openai_key
        self.openai_org = openai_org
        self.model = model

    def chat_completions(self, content: str) -> str:
        openai.organization = self.openai_org
        openai.api_key = self.openai_key
        completion = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "user", "content": content}]
        )
        return completion.choices[0].message.content
