# the log which will contain the past questions and responses
# Author : Eswar Sivan Sethu
'''to make JAKE understand the user better, a log will be kept with all the past questions and
    responses or actions taken, much like a person remembering what they did. this log will
    have everything the user interacted with, and it will store upto 6 months of data before
    deleting it automatically. This data can be accessed by the user. it uses sqlite to store the
    data. it only stores texts and will be limited to a maximum of 4 lines.'''