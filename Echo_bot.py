import requests

TOKEN = "5176285531:AAH2FTZ5jaTVb8iiERZSNcVB2Z5BBdsLPZg"
ROOT_URL = "https://api.telegram.org/bot"
last_updated_id = 0

sentences = [{"text" : "We can make a revolution!",
             "lvl" : 2},
             {"text" : "Dogs is a friends",
             "lvl" : 1},
             {"text" : "Don’t be embarrassed to admit you didn’t understand something.",
             "lvl" : 3},
             {"text" : "You might be surprised at how patient peoples are when they knows you`re still learning Eanglish",
             "lvl" : 4},
             {"text" : "Work is a perfect place to improve your English.",
             "lvl" : 3},
             {"text" : "Sometimes when people are not sure of what they’re saying, they mumble or speak quietly.",
             "lvl" : 4},
             {"text" : "If you are leaving in the evening or late afternoon, you can say “good night”",
             "lvl" : 3}]

def get_updates(root_url,token):
    url = f"{root_url}{token}/getUpdates"
    res = requests.get(url)
    return res.json()

def send_message(root_url, token,  chat_id, message,):
    url = f"{root_url}{token}/sendMessage"
    data = {'chat_id' : chat_id, 'text' : message}
    res = requests.post(url=url, data=data)
    print(res)



while True:
    updates = get_updates(ROOT_URL, TOKEN)
    messages = updates["result"]
    for message in messages:
        if message["update_id"] > last_updated_id:
            send_message(ROOT_URL, TOKEN, message['message']['chat']['id'], message['message']['text'])
            last_updated_id = message["update_id"]
             
