# VoiceChatAI
AI voice chat using chat gpt

Totally based on [this tutorial](https://levelup.gitconnected.com/i-created-a-voice-chatbot-powered-by-chatgpt-api-here-is-how-6302d555b949)

## Executing

1. Install requirements with:
```sh
    pip install -r requirements.txt
```

2. Create a file `./data/config.json`
```json
{
    "token": "<YOUR VALID OPENAI TOKEN>"
}
```
> **Warning**  
> TOKEN MUST BE GIVEN FOR IT TO WORK

3. Run by using:
```sh
    python -m streamlit run main.py
```
> **Note**  
> Currently it works in Spanish, change every instance of `es` as a language in the code to `en` for English

3. Start recording with the `speak` button. A green circle will appear when you can start talking.