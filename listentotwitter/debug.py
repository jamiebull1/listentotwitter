from listentotwitter.config import DEBUG


def log(message):
    if DEBUG:
        print message.encode('utf-8')
