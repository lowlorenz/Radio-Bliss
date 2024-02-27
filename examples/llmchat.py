#%%
from openai import OpenAI
import dotenv

dotenv.load_dotenv()
key = dotenv.get_key("./.env", "OPENAI")



client = OpenAI(api_key=key,base_url="https://llms.azurewebsites.net")


stream = client.chat.completions.create(
    model="gpt-3.5",
    messages=[{"role": "user", "content": "Hi how are you doing today?"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")




# %%

# %%
