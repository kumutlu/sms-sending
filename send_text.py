from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello World! This is Kemal from Python',
                              from_='+xxxxxxxxx',
                              to='+905052xxxxxxx8'
                          )

print(message.sid)