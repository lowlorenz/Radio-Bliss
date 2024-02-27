from pathlib import Path
import openai
from typing import Optional
from wiki import WikiParser
import random
from functools import lru_cache


class ChatGPT:
    def __init__(self, api_key: Optional[str] = None):
        if api_key is None:
            env_path = Path('.env')
            if env_path.exists():
                env = {line.split('=')[0]: line.split('=')[1] for line in env_path.read_text().split('\n') if line if '=' in line and not line.startswith('#')}
                api_key = env['OPENAI']
            else:
                raise ValueError('api_key must be provided or set in .env file')
        self.client = openai.OpenAI(
            api_key=api_key,
            base_url='https://llms.azurewebsites.net'
        )

    @lru_cache(maxsize=1000)
    def get_funfacts(self, background_info: str, num_sentences: int = 3) -> str:
        response = self.client.chat.completions.create(
            model="gpt-3.5",
            messages=[
                {
                    "role": "system",
                    "content": f"You find good-to-know/fun-fact information about the area around you. Only use the provided information and discard anything that might be boring. Output {num_sentences} sentences containing fun-facts and interesting information about the most interesting nearby place. Limit the output to the most interesting place and {num_sentences} sentences."
                },
                {
                    "role": "user",
                    "content": background_info,
                }
            ]
        )
        return response.choices[0].message.content


if __name__ == "__main__":
    chatgpt = ChatGPT()
    long = 50 + random.random()
    lat = 14 + random.random()
    summaries = WikiParser.get_summaries(long, lat)
    print(chatgpt.get_funfacts(''.join(summaries), 3))
