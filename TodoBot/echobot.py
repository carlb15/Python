"""Echo Todo Bot using Telegram."""

import json
import requests
import time

TOKEN = "382586960:AAHBBBxzJ-ET98e9rIPSq3ZSWLDimxgexwI"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    """Retrieves the URL."""
    """
    Assumption: Request doesn't fail due to - internet connection, Telegram is
                is down, or an issue with the Token.
    """
    response = requests.get(url)
    content = response.content.decode("utf-8")
    return content


def get_json_from_url(url):
    """Retrieve JSON string from the URL."""
    content = get_url(url)
    js = json.loads(content)
    return js


def get_last_update_id(updates):
    """Calculates the highest ID of all updates received."""
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def echo_all(updates):
    """Send an echo reply for each message received."""
    for update in updates["result"]:
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        send_message(text, chat)


def get_updates(offset = None):
    """Retrieve messages sent to the Chat Bot."""
    url = URL + 'getUpdates?timeout=100'
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_chat_id_and_text(updates):
    """Get the last chat id and text sent to the bot."""
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates['result'][last_update]['message']['text']
    chat_id = updates['result'][last_update]['message']['chat']['id']
    return (text, chat_id)


def send_message(text, chat_id):
    """Send a message to the chat bot."""
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def main():
    """Retrieve most recent messages from Telegram every 0.5 seconds."""
    last_update_id = None
    while True:
        print("getting updates")
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
