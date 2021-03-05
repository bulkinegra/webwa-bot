import os
import sys
import time
import sh_action

my_name = 'vvv'
my_phone = '89602641406'
my_id = '89602641406@c.us'

while True:
    print("Checking for more messages")
    new_msg = input()
    if sh_action.add_sh_contact(my_id, my_phone):
        msgs = sh_action.get_msg_from_sh_bot()
        print('<--------From bot-------->')
        [print('      ' + msg) for msg in msgs]
        print('<------------------------>')
