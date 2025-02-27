# ChatbotCDP-
Building a Support Agent Chatbot for CDP "How-to" Questions

Project Overview
The CDP Support Chatbot helps users answer 'how-to' questions related to Customer Data Platforms (CDPs) including Segment, Technologies Used
- Python
- Tkinter (for GUI)
- Requests & BeautifulSoup (for web scraping)
- OpenAI API (optional, for NLP)
Project Structure
chatBot/
nnn backend/
n nnn __init__.py
n nnn chatbot.py (Handles logic)
nnn frontend/
n nnn gui.py (Tkinter GUI)
nnn requirements.txt
Backend (Chatbot Logic)
The backend fetches documentation content and extracts relevant answers. It includes:
- Fetching documentation using requests & BeautifulSoup
- Matching user queries to relevant documentation sections
- Providing predefined responses for common 'how-to' questions
Frontend (GUI using Tkinter)
The GUI provides an interactive interface for users to ask questions. Features include:
- Dropdown menu to select a CDP platform
- Text entry box for questions
- Scrollable text area for chatbot responses
How to Run the Project
1. Install dependencies:
pip install -r requirements.txt
2. Run the chatbot GUI:
python frontend/gui.py
3. Ask your 'how-to' questions related to CDPs!
