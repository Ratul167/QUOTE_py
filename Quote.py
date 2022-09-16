import pyttsx3
import requests
import json



def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " by:" + json_data[0]['a']
  return(quote)


engine = pyttsx3.init()
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)  
engine.setProperty('voice', voices[1].id)   
quote=get_quote()
engine.say(quote)
print(quote)
engine.runAndWait()

