import ptbot
import os
from dotenv import load_dotenv
from pytimeparse import parse


load_dotenv()

TG_TOKEN = os.getenv('TOKEN')
TG_CHAT_ID = os.getenv('LOGIN')


def choose(author_id, message):
    secs = parse(message)
    message = "Осталось секунд: {}".format(secs)
    message_id = bot.send_message(author_id, message)
    bot.create_countdown(secs, notify_progress, message_id=message_id, author_id=author_id, total_secs=secs)


def notify_progress(secs_left, message_id, author_id, total_secs):
    progress_bar = render_progressbar(total_secs, total_secs - secs_left)
    message = "Осталось секунд: {}\n{}".format(secs_left, progress_bar)
    bot.update_message(author_id, message_id, message)
    if not secs_left:
        bot.send_message(author_id, 'Время вышло')


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)


def main():
    global bot
    bot = ptbot.Bot(TG_TOKEN)
    bot.reply_on_message(choose)
    bot.run_bot()


if __name__ == '__main__':
    main()
