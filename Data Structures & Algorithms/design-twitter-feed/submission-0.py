class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list)
        self.followings = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        followers = list(self.followings[userId])
        followers.append(userId)

        for follower in followers:
            # Makes sure follwers have tweets
            if follower in self.tweets and self.tweets[follower]:
                f_tweets = self.tweets[follower]
                last_index = len(f_tweets) - 1
                timestamp, tweetId = f_tweets[last_index]
                heapq.heappush(heap, (-timestamp, follower, last_index))
        print(heap)

        while heap and len(res) < 10:
            time, uId, currIndex = heapq.heappop(heap)
            timestamp, tweetId = self.tweets[uId][currIndex]
            res.append(tweetId)

            if currIndex > 0:
                nextIndex = currIndex - 1
                nextTimestamp, nextTweetId = self.tweets[uId][nextIndex]   
                heapq.heappush(heap, (-nextTimestamp, uId, nextIndex))          

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # Ignore follow themselves
        if followerId == followeeId:
            return
        self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followings[followerId].discard(followeeId)