from twilio.rest import Client
import os
from dotenv import load_dotenv
import os
import cv2
from ultralytics import YOLO

load_dotenv()

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
to_phone = os.getenv('TO_PHONE')
from_phone = os.getenv('FROM_PHONE')

# function for sending txt message
def sendSmsNotification():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='yoooooo sorry bro wrong message, everything in your field is fine',
        to=to_phone,
        from_=from_phone
    )

    print("text message send with id:",message.sid)



# Load YOLO model
model_path = os.path.join('.', 'runs', 'detect', 'train5', 'weights', 'best.pt')
model = YOLO(model_path)

result = model.predict(source="0", show=True)

def main():
    print("this is from main")

if __name__ == '__main__':
    main()