import subprocess
import os
import requests
import json


### Helper function to format the chat messages and Print out the response
DEFAULT_SYSTEM_PROMPT = """\nYou are VietHealth-GPT an AI medical assistant developed by VietnamAIHub, designed to provide User accurate and comprehensive medical information. Your goal is to assist users by delivering clear and detailed answers, ensuring they receive all necessary information without needing to look elsewhere. In cases where the user's question is unclear or factually incorrect, asking again for clarify or correct the misconceptions rather than providing misleading information."""


def apply_chat_template(example):
    messages = example["messages"]
    formatted_chat = ""

    eos_token = "<|eot_id|>"  
    if messages and messages[0]["role"] == "system":
        # Update the content of the first system message
        previous_content =  messages[0]["content"] #"<|begin_of_text|>system<|start_header_id|>\n"+
        messages[0]["content"] = "<|begin_of_text|>system<|start_header_id|>\n" + previous_content +eos_token
    ## Add an empty system message if there is no initial system message
    elif messages and messages[0]["role"] != "system":
        # Insert a new system message at the beginning if there isn't one
        messages.insert(0, {"role": "system", "content": f"<|begin_of_text|>system<|start_header_id|>{DEFAULT_SYSTEM_PROMPT}<|eot_id|>"})
        
    # Define your end-of-sentence token here
    eos_token_="<|eot_id|><|start_header_id|>assistant<|end_header_id|>"
    # Loop through the messages to apply the template
    for i, message in enumerate(messages):
        role = message['role']
        
        if role =="user":
            content = "<|start_header_id|>user<|end_header_id|>\n\n" + message['content'] +"\n\nYour Vietnamese response:" + eos_token_
            formatted_chat += f'{content}'
        
        elif  role =="assistant":
            content = message['content'] + eos_token +"\n"
            formatted_chat += f'\n{content}' 
        else :
            content = message['content']
            formatted_chat += f'{content}' 

            
    return formatted_chat



## 3. Function to Print Response from API

def print_response(response):
    if response.status_code == 200:
        all_content = []
        # Iterate over the response stream line by line
        for line in response.iter_lines():
            if line:
                try:
                    response_json = json.loads(line.decode('utf-8'))
                    content = response_json.get("response", "")
                    if content:
                        all_content.append(content)
                        print(content, end='', flush=True)  # Print content as it arrives
                except json.JSONDecodeError as e:
                    print("Error parsing JSON:", e)

        print()
    else:
        print("Request failed with status code:", response.status_code)
    all_content=' '.join(all_content)
    return all_content


messages = {
"messages": [
    {"role": "system", "content": f"{DEFAULT_SYSTEM_PROMPT}"}
]
}
## Optional 
# Append the user message
messages["messages"].append({"role": "user", "content": "Cho tôi hỏi, Bạn tôi, 30 tuổi, đã vô tình nuốt phải hai giọt phenol vì nhầm là sữa. Anh ấy đã nôn và uống nhiều nước muối. Xin hãy tư vấn cho bất kỳ tác dụng phụ nào.?"})
# Append the assistant response

input_prompt = apply_chat_template(messages)

url = "http://140.115.53.106:5000/api/generate"
payload = {
    "model": "VietHealthGPT_202407_8B",
    "prompt": input_prompt,
    "stream": True, 
    "options": {
        # "seed": 123,
        "temperature": 0.5 
        # "top_k": 20,
        # "top_p": 0.9,
        # "tfs_z": 0.5,
        # "typical_p": 0.7,
        # "repeat_last_n": 33,
        # "repeat_penalty": 1.2,
        # "presence_penalty": 1.5,
        # "frequency_penalty": 1.0,
    }
}
response = requests.post(url, data=json.dumps(payload), headers={"Content-Type": "application/json"}, stream=True)
respone_output=print_response(response)
