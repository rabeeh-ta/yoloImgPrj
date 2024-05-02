from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
to_phone = os.getenv('TO_PHONE')
from_phone = os.getenv('FROM_PHONE')

# function for sending txt message
def sendSmsNotification(message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        to=to_phone,
        from_=from_phone
    )

    print("text message send with id:",message.sid)


if __name__ == '__main__':
    print("send text message code")