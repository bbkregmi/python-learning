from getuserinputs import askForText

parts_of_speech_needed = [
        "PLURAL NOUN",
        "ADVERB",
        "VERB",
        "ARTICLE OF CLOTHING",
        "BODY PART",
        "ADJECTIVE",
        "NOUN",
        "PLURAL NOUN",
        "ANOTHER BODY PART",
        "PLURAL NOUN",
        "ANOTHER BODY PART",
        "NOUN",
        "NOUN",
        "VERB ENDING IN 'ING",
        "ADJECTIVE",
        "ADJECTIVE",
        "VERB"
        ]

user_response = askForText(parts_of_speech_needed)

template = ("It's simple. Turn the %s. Make him/her want %s to date you. "
            "Make sure you're always dress to %s. Each and every day wear " 
            "a %s that you know shows off your %s to %s advantage and make your " 
            "%s look like a million %s. Even if the two of you make a meaningful " 
            "%s contact, don't admit it. No hugs or %s. Just shake his/her %s " 
            "firmly. And remember, when he/she asks you out, even though a chill may " 
            "run down your %s and you can't stop your %s from %s, just play it %s. " 
            "Take a long pause before answering in a very %s voice. \"I'll have to %s "
            "it over\".")
print(template % tuple(user_response))
