# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = ""
auth_token = ""


client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='+12282204630',
                              to='+8613166382772'
                          )

print(message)
