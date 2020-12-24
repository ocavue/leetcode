"""
submits:
- date: 2020-12-24
  minutes: 24
  cheating: false
labels:
- heap
"""
#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#
# https://leetcode.com/problems/design-twitter/description/
#
# algorithms
# Medium (30.61%)
# Likes:    1122
# Dislikes: 218
# Total Accepted:    58.8K
# Total Submissions: 190K
# Testcase Example:  '["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]\n' +
#   '[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]'
#
# Design a simplified version of Twitter where users can post tweets,
# follow/unfollow another user and is able to see the 10 most recent tweets in
# the user's news feed. Your design should support the following methods:
#
#
#
# postTweet(user_id, tweet_id): Compose a new tweet.
# getNewsFeed(user_id): Retrieve the 10 most recent tweet ids in the user's news
# feed. Each item in the news feed must be posted by users who the user
# followed or by the user herself. Tweets must be ordered from most recent to
# least recent.
# follow(follower_id, followee_id): Follower follows a followee.
# unfollow(follower_id, followee_id): Follower unfollows a followee.
#
#
#
# Example:
#
# Twitter twitter = new Twitter();
#
# // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5);
#
# // User 1's news feed should return a list with 1 tweet id -> [5].
# twitter.getNewsFeed(1);
#
# // User 1 follows user 2.
# twitter.follow(1, 2);
#
# // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6);
#
# // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# // Tweet id 6 should precede tweet id 5 because it is posted after tweet id
# 5.
# twitter.getNewsFeed(1);
#
# // User 1 unfollows user 2.
# twitter.unfollow(1, 2);
#
# // User 1's news feed should return a list with 1 tweet id -> [5],
# // since user 1 is no longer following user 2.
# twitter.getNewsFeed(1);
#
#
#

# @lc code=start

from collections import defaultdict
from typing import Dict, List, Tuple
import heapq


class User:
    def __init__(self):
        self.tweets = []
        self.followed: Dict[int, User] = {}

    def getNewsFeed(self):
        feed_heap: List[Tuple[int, int]] = []
        feed: List[int] = []

        for user_id, user in self.followed.items():
            if user.tweets:
                tweet_index = len(user.tweets) - 1
                time, tweet_id = user.tweets[tweet_index]

                heapq.heappush(feed_heap, (time, tweet_id, tweet_index, user_id))

        while len(feed) < 10 and feed_heap:
            _, tweet_id, tweet_index, user_id = heapq.heappop(feed_heap)

            feed.append(tweet_id)

            user = self.followed[user_id]
            tweet_index -= 1
            if tweet_index >= 0:
                time, tweet_id = user.tweets[tweet_index]
                heapq.heappush(feed_heap, (time, tweet_id, tweet_index, user_id))

        return feed


class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.users: Dict[int, User] = defaultdict(User)

        self.time = -1

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        """
        Compose a new tweet.
        """

        user = self.users[user_id]
        user.followed[user_id] = user

        self.users[user_id].tweets.append((self.time, tweet_id))

        self.time -= 1

    def getNewsFeed(self, user_id: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        user = self.users[user_id]
        return user.getNewsFeed()

    def follow(self, follower_id: int, followee_id: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """

        follower = self.users[follower_id]
        followee = self.users[followee_id]

        follower.followed[followee_id] = followee

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if follower_id == followee_id:
            return

        follower = self.users[follower_id]
        if followee_id in follower.followed:
            del follower.followed[followee_id]


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(user_id,tweet_id)
# param_2 = obj.getNewsFeed(user_id)
# obj.follow(follower_id,followee_id)
# obj.unfollow(follower_id,followee_id)
# @lc code=end

if __name__ == "__main__":
    from tool import t

    if True:
        twitter = Twitter()
        twitter.postTweet(1, 5)
        t(twitter.getNewsFeed(1), [5])

        twitter.follow(1, 2)

        twitter.postTweet(2, 6)

        t(twitter.getNewsFeed(1), [6, 5])

        twitter.unfollow(1, 2)
        t(twitter.getNewsFeed(1), [5])

    if True:
        twitter = Twitter()
        twitter.postTweet(1, 5)
        twitter.postTweet(1, 3)
        t(twitter.getNewsFeed(1), [3, 5])

