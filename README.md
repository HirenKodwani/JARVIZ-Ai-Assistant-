# JARVIZ-Chat--Bot-
 About Jarvis AI Chatbot Jarvis is a voice-activated artificial intelligence assistant built using Python. Inspired by the iconic assistant from Iron Man, this project integrates multiple libraries to create an interactive system that understands spoken commands, performs specific tasks, and responds through voice output.

🚀 Features
🎙️ Wake Word Activation – Listens for “Jarvis” to activate command mode

🔊 Speech Synthesis – Speaks responses using pyttsx3

🧠 Conversational AI – Uses LLaMA 3 via groq API for smart replies

🌐 Web Automation – Opens websites like Google, YouTube, LinkedIn, etc.

📰 Live News – Fetches and speaks top Indian news headlines using NewsAPI

📷 Camera Test – Opens webcam test site for camera access

🧔 Personalized Responses – Replies to custom queries like “Who made you?”

📦 Tech Stack
Component	Purpose
speech_recognition	Convert spoken input to text
pyttsx3	Text-to-speech voice responses
webbrowser	Launches web pages
requests	Fetches API data (e.g., news)
groq (LLaMA 3 API)	AI-powered responses (chat completion)

🔧 Setup Instructions
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/jarvis-ai-chatbot.git
cd jarvis-ai-chatbot
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Example requirements.txt:

nginx
Copy
Edit
speechrecognition
pyttsx3
requests
openai
Replace API Keys:

Groq API Key (api_key in OpenAI(...))

NewsAPI Key (in the news API URL)

Run the Assistant:

bash
Copy
Edit
python jarvis.py
🖼️ GUI Version with Streamlit (Optional)
To run the Streamlit-based voice assistant UI:

bash
Copy
Edit
streamlit run gui_jarvis.py
This launches a browser UI where you can interact with the assistant via buttons and text, while the backend still handles voice and AI interaction.

🧪 Sample Commands
Command	Action
"Jarvis"	Wake word
"Open Google"	Opens Google in browser
"What's in the news today?"	Reads latest headlines
"Open music"	Plays a predefined Spotify track
"Who made you?"	Responds with a custom message
"Tell me about..."	Uses AI to answer intelligently

📜 License
This project is open-source and free to use under the MIT License.

🙋‍♂️ Credits
Built by Hiren Kodwani
Using OpenAI-compatible Groq APIs, Python, and voice-based libraries.
