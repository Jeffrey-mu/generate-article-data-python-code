import requests
import json
from config import OPENAI_API_KEY

def openai_stream(title) -> str:
    payload = dict()
    payload['model'] = 'gpt-3.5-turbo'
    payload['max_tokens'] = 2000
    payload['messages'] = [
        {
            "role": "system",
            "content": "我要你把我写的句子翻译成表情符号。我会写句子，你会用表情符号表达它。我只是想让你用表情符号来表达它。除了表情符号，我不希望你回复任何内容。当我需要用英语告诉你一些事情时，我会用 {like this} 这样的大括号括起来。我的第一句话是“你好，请问你的职业是什么？”"
        },
        {"role": "user", "content": title},
    ]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }
    print(json.dumps(payload))
    base_path = 'https://api.openai.com'
    response = requests.post(base_path + "/v1/chat/completions", headers=headers, data=json.dumps(payload))
    stream = response.json()
    print(stream)
    try:
        return stream["choices"][0]['message']['content']
    except (KeyError, IndexError):
        return ""
