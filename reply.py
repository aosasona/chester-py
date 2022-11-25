from chat_map import message_map, reply_map
import re


def reply_message(message):
    if "urgent" in message:
        return "Sorry, I'm not available right now. Please leave a message and I'll get back to you as soon as I can."
    for key, value in message_map.items():
        message = strip_all(message)
        value = [strip_all(x) for x in value]
        if message in value:
            return reply_map[key]
        for i in value:
            if i in message and len(message) > 5 and len(i) > 5:
                return reply_map[key]
    return "I don't understand :("


def strip_all(message):
    return re.sub(r'\W+', '', message).lower().strip()

