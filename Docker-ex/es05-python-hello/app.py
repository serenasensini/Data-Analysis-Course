import os

message = os.getenv("APP_MESSAGE", "Ciao dal container Python!")
print(message)

