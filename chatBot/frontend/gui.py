import tkinter as tk
from tkinter import ttk, scrolledtext
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.chatbot import get_relevant_info  # Now it should work

def ask_chatbot():
    """Get response from chatbot and update the GUI."""
    platform = platform_var.get()
    query = query_entry.get()

    if not platform or not query:
        response_text.set("Please select a platform and enter a question.")
        return

    response = get_relevant_info(platform, query)
    response_text.set(response)

# GUI Setup
root = tk.Tk()
root.title("CDP Support Chatbot")
root.geometry("500x500")
root.configure(bg="lightgray")

# Title Label
title_label = tk.Label(root, text="CDP Support Chatbot", font=("Arial", 16, "bold"), bg="lightgray")
title_label.pack(pady=10)

# Platform Selection
platform_var = tk.StringVar()
platform_label = tk.Label(root, text="Select CDP Platform:", bg="lightgray")
platform_label.pack()
platform_dropdown = ttk.Combobox(root, textvariable=platform_var, values=["Segment", "mParticle", "Lytics", "Zeotap"])
platform_dropdown.pack()

# Query Entry
query_label = tk.Label(root, text="Enter your question:", bg="lightgray")
query_label.pack()
query_entry = tk.Entry(root, width=50)
query_entry.pack(pady=5)

# Submit Button
submit_button = tk.Button(root, text="Ask", command=ask_chatbot, bg="blue", fg="white")
submit_button.pack(pady=10)

# Response Output
response_text = tk.StringVar()
response_box = scrolledtext.ScrolledText(root, width=60, height=10, wrap=tk.WORD)
response_box.pack(pady=10)

def update_response():
    response_box.delete(1.0, tk.END)
    response_box.insert(tk.END, response_text.get())

response_text.trace_add("write", lambda *args: update_response())

# Run the GUI
root.mainloop()
