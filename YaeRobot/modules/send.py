

from telegram.ext import run_async

from YaeRobot import dispatcher
from YaeRobot.modules.disable import DisableAbleCommandHandler
from YaeRobot.modules.helper_funcs.alternate import send_message
from YaeRobot.modules.helper_funcs.chat_status import user_admin
from YaeRobot.modules.helper_funcs.chat_status import dev_plus

@run_async
@dev_plus
def send(update, context):
    args = update.effective_message.text.split(None, 1)
    creply = args[1]
    send_message(update.effective_message, creply)


ADD_CCHAT_HANDLER = DisableAbleCommandHandler("snd", send)
dispatcher.add_handler(ADD_CCHAT_HANDLER)
__command_list__ = ["snd"]
__handlers__ = [ADD_CCHAT_HANDLER]
