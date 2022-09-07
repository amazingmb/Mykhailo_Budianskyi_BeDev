user =  {"username" : "Mykhailo Budianskyi",
           "user_id" : 1,
           "lvl" : 3}
         

message = {"user" : user,
           "message_text" : "embarrassed"}

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

matched_lvl = []
for sentence in sentences:
        if (lambda sentence: True if user.get("lvl") == sentence.get("lvl") else False) (sentence):
            matched_lvl.append(sentence)

send_message = []
for sentence in matched_lvl:
    if (lambda sentence: True if message.get("message_text") in sentence.get("text") else False) (sentence):
        send_message.append(sentence.get("text"))

print(send_message)
