import openai


class ChatGPT:
    """
    Сервис для работы с ChatGPT
    """

    def __init__(self, openai_key, openai_org, model='gpt-3.5-turbo'):
        """

        :param openai_key:  API ключ сервиса ChatGPT
        :param openai_org: Ключ организации сервиса ChatGPT
        :param model: Модель к которой обращаемся
        """
        self.openai_key = openai_key
        self.openai_org = openai_org
        self.model = model

    async def chat_completions(self, content: str) -> str:
        """
        Функция отправки запроса в ChatGPT

        :param content: Текстовый запрос к сервису ChatGPT
        :return: Текстовый ответ от сервиса
        """

        openai.organization = self.openai_org
        openai.api_key = self.openai_key
        try:
            completion = openai.ChatCompletion.create(
                model=self.model, messages=[{"role": "user", "content": content}]
            )
            return completion.choices[0].message.content
        except openai.error.APIConnectionError as err:
            return f'Ошибка соединения с сервисом OpenAI: {err}'

    async def create_image(self, prompt: str, n: int = 1, size: str = "1024x1024") -> str:
        """
        Функция отправки запроса в ChatGPT для генерации изображения

        :param prompt: Текстовый запрос к сервису ChatGPT
        :param n: Количество изображений
        :param size: Размер изображения
        :return: Текстовый ответ с url
        """

        openai.organization = self.openai_org
        openai.api_key = self.openai_key
        try:
            image_response = openai.Image.create(
              prompt=prompt,
              n=n,
              size=size
            )
            return image_response
        except openai.error.APIConnectionError as err:
            return f'Ошибка соединения с сервисом OpenAI: {err}'
