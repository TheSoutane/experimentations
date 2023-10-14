import tkinter as tk
from tkinter import scrolledtext, END
import openai
import os

# Function to interact with the OpenAI language model and get the chatbot response
def get_chatbot_response(input_text):
    openai.api_key = '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'
    # openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.ChatCompletion.create(
        engine="gpt-3.5-turbo",
        prompt=input_text,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Function to display the chatbot response in the GUI
def show_chatbot_response():
    user_input = user_input_box.get("1.0", END).strip()
    user_input_box.delete("1.0", END)

    if user_input.lower() in ["exit", "quit", "bye"]:
        chat_log.insert(tk.END, "Chatbot: Goodbye!\n")
        return

    chat_log.insert(tk.END, "You: " + user_input + "\n")
    chatbot_response = get_chatbot_response(user_input)
    chat_log.insert(tk.END, "Chatbot: " + chatbot_response + "\n")

# Main GUI window
root = tk.Tk()
root.title("Chatbot with OpenAI")

# Chat log
chat_log = scrolledtext.ScrolledText(root, width=60, height=20, wrap=tk.WORD)
chat_log.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# User input box
user_input_box = scrolledtext.ScrolledText(root, width=40, height=4, wrap=tk.WORD)
user_input_box.grid(row=1, column=0, padx=10, pady=10)

# Send button
send_button = tk.Button(root, text="Send", command=show_chatbot_response)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()