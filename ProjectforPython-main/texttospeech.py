import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

names = ['Ravi','Rahul','Aranav','Tate']

for name in names:
    speaker.speak(f"Shoutout to {name}")