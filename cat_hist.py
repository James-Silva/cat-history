import praw
import random

class Post:
    def __init__(self, permalink='https://reddit.com', 
                       url='https://reddit.com',
                       post_id=00000):
        self.permalink = permalink # Link to the post
        self.url = url # URL the post links to
        self.post_id = post_id 

def txt_to_list(filename):
    with open(filename, 'r') as f:
        lst = f.read().splitlines()
    return lst

def top_score(reddit, sub_name):
    post = Post() # Dummy post to keep the program working
    try:
        subreddit = reddit.subreddit(sub_name)
        submission = next(subreddit.top('week', limit=1))
        permalink = 'https://www.reddit.com' + submission.permalink
        post = Post(permalink, submission.url, submission.id)
    except Exception as e: 
        print('Failed to get submission for subreddit', sub_name) 
    return post

def main():
    # Get reddit instance using praw.ini
    reddit = praw.Reddit('Cat History App') 
    
    # Get a list of cat subreddits from a txt file
    sub_names = txt_to_list('cat_subreddits.txt')
   
    # Find a random subreddit that has a post that is at the top of the week
    post = Post()
    goodPost = False
    while (not goodPost): # iterate until a good link is found
        sub_name = random.choice(sub_names)
        post = top_score(reddit, sub_name)
        if (post.permalink != 'https://reddit.com'):
            goodPost = True
    print(post.permalink)

if __name__ == "__main__":
    main()
