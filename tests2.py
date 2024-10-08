from datetime import date,datetime
import json
note="hi"

now = datetime.now()

dt_string = now.strftime("%H:%M")


dictionary = {
            "Date": str(date.today()),
    "Time":str(dt_string),
            "Content": note,
}

# Serializing json
json_object = json.dumps(dictionary, indent=3)

# Writing to sample.json
with open("usernotes.json", "a") as outfile:
    outfile.write(json_object)