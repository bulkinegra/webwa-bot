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
                new_contact = sh_action.addShContact(chat_id = message.sender.id, phone = "хуй там пока что")
                if new_contact:
                    msgs = sh_action.getMsgFromShBot()
                    for msg in msgs:
                        contact.chat.send_message(msg)
                        time.sleep(0.100*len(msg))
