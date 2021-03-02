import json
import os
import sys
import time
import sh_action

from webwhatsapi import WhatsAPIDriver
from webwhatsapi.objects.message import Message

print("Environment", os.environ)
try:
    os.environ["SELENIUM"]
except KeyError:
    print("Please set the environment variable SELENIUM to Selenium URL")
    sys.exit(1)

profiledir = os.path.join(".", "firefox_cache")
if not os.path.exists(profiledir):
    os.makedirs(profiledir)

driver = WhatsAPIDriver(
    profile=profiledir, client="remote", command_executor=os.environ["SELENIUM"]
)
print("Waiting for QR")
driver.wait_for_login()
print("Saving session")
driver.save_firefox_profile(remove_old=False)
print("Bot started")

while True:
    time.sleep(3)
    print("Checking for more messages, status", driver.get_status())
    for contact in driver.get_unread():
        for message in contact.messages:
            if isinstance(message, Message):  # Currently works for text messages only.
                contact.chat.send_message(message.content)
                print("class", message.__class__.__name__)
                print("message", message)
                print("id", message.id)
                print("type", message.type)
                print("timestamp", message.timestamp)
                print("chat_id", message.chat_id)
                print("sender", message.sender)
                print("sender.id", message.sender.id)
                print("sender.safe_name", message.sender.get_safe_name())
                if message.type == "chat":
                    print("-- Chat")
                    print("safe_content", message.safe_content)
                    print("content", message.content)
                sh_action.addShContact(id = message.sender.id, phone = "хуй там пока что")
