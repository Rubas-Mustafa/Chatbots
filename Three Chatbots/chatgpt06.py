import openai   
import gradio  

openai.api_key = "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" #

messages = [{"role": "system", "content": "You are psychologist"}] 

def CustomChatGPT(user_input): 
    messages.append({"role": "user", "content": user_input}) 
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply 

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Sisters of Syntax | ChatBot")

demo.launch(share=True)
