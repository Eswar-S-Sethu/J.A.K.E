# the main selling point of my creation.
# Author : Eswar Sivan Sethu
'''when a user says something, that input data after speech recognition comes here. this is where
   things get sorted out. this is connected with all other
   classes. After accurately finding the context of a sentence, it is sent to appropriate function. It
   can be directly sent to GPT if it finds it more suited.
   Example: I ask "what time is it?" and this can have different meanings depending on what we were
   talking about. It could be me simply asking the current time or something related to the previous
   sentences like maybe I was talking about an event I set in the calendar, or I was talking about
   the time when something happens or happened. It also corrects a grammar mistake that I made like
   chatgpt does. This is where the context of a sentence is separated. A custom algorithm will be
   developed to do this. When the analyser gets confused because of contradicting info, it will
   proceed to get a clear data from the user.'''