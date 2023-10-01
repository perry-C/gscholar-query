import openai

import config


def get_chat_summary(paper_name):
    # Utilisation of chat_gpt api to give a short summarization of the papers found

    openai.api_key = config.chat_api_key

    question = f'Please give me a summary of the findings made in paper "{paper_name}", \
               in less than 200 words'

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': question},

            # TODO: Further querying to narrow done answers
            # {'role': 'assistant', 'content': 'The Los Angeles Dodgers won the World Series in 2020.'},
            # {'role': 'user', 'content': 'Where was it played?'}
        ]
    )

    response_content = response['choices'][0]['message']['content']
    return response_content
