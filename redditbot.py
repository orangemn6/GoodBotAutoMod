import praw
import prawcore
#import goodbotconfig
import time
import os

automod = 'AutoModerator'

def bot_login():
    print("Logging In...")
    r = praw.Reddit(username = "GoodBotAutoMod",
            password = "",
            client_id = "",
            client_secret = "",
            user_agent = "Wi_Tarrd's Good Bot v0.2")
    print("Logged In!")

    return r

def run_bot(r, comments_replied_to):
    print("Obtaining Comments...")
    for comment in r.subreddit('memes+dankmemes+teenagers').comments(limit=25):

        if "I" in comment.body and comment.id not in comments_replied_to and comment.author == automod:
            try:
                print("Found AutoMod " + comment.id)

                comment.reply("Good Bot. \n\n*I am a bot, and this action was performed automatically. Please contact u\/Wi_Tarrd with issues. (I apologize if the bot comments twice. It happens when I encounter locked comments.)*")
                print("Replied to AutoMod " + comment.id)

                comments_replied_to.append(comment.id)

                with open ("/comments_replied_to.txt", "a") as f:
                    f.write(comment.id + "\n")
            except:
                print("Error")

    for comment in r.subreddit('memes+dankmemes+teenagers').comments(limit=25):

        if "freekarma4u" in comment.body and comment.id not in comments_replied_to and comment.author == automod:
            print("Found freekarma4u " + comment.id)
            comment.reply("Please be aware that posting in subreddits meant for getting free karma can and will get you banned from participating in other subreddits that you may want to use in the future. \n\n*I am a bot, and this action was performed automatically. Please contact u\/Wi_Tarrd with issues.*")
            print("Replied to freekarma4u " + comment.id)

            comments_replied_to.append(comment.id)

            with open ("/comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")

    for comment in r.subreddit('memes+dankmemes+teenagers').comments(limit=250):

        if "!goodbot" in comment.body and comment.id not in comments_replied_to and comment.author == automod:
            print("Found !goodbot " + comment.id)
            comment.reply("Hello! \n\n*I am a bot, and this action was performed automatically. Please contact u\/Wi_Tarrd with issues.*")
            print("Replied to !goodbot " + comment.id)

            comments_replied_to.append(comment.id)

            with open ("/comments_replied_to.txt", "a") as f:
                f.write(comment.id + "\n")

    print(comments_replied_to)

    print("Sleeping for 10 Seconds")
    #Sleep for 10 Seconds
    time.sleep(10)

def get_saved_comments():
    if not os.path.isfile("/comments_replied_to.txt"):
        comments_replied_to = []
    else:
        with open("/comments_replied_to.txt", "r") as f:
            comments_replied_to = f.read()
            comments_replied_to = comments_replied_to.split("\n")
            comments_replied_to = filter(None, comments_replied_to)

        return comments_replied_to



r = bot_login()
comments_replied_to = []

while True:
    run_bot(r, comments_replied_to)
