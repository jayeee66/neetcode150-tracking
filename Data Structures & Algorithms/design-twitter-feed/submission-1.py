class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list) # list of [timestamp, tweetId]
        self.followees = defaultdict(set) # set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.timestamp, tweetId])
        self.timestamp -= 1
        #print(self.tweets)
    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # order for the result
        heap = [] 
        self.followees[userId].add(userId) # add themselves to show 
        # traverse user's followees' tweets and add to heap
        for followeeId in self.followees[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1 # index of followee's tweet
                timestamp, tweetId = self.tweets[followeeId][index] # find the latest post of followee
                heap.append([timestamp, tweetId, followeeId, index - 1]) # put into heap and index move
        
        heapq.heapify(heap)
        print(heap)
        while heap and len(res) < 10:
            timestamp, tweetId, followeeId, index = heapq.heappop(heap)
            res.append(tweetId)
            if index >= 0:  
                timestamp, tweetId = self.tweets[followeeId][index] # find the next post if exist
                heapq.heappush(heap, [timestamp, tweetId, followeeId, index - 1]) # put in and move index
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followees[followerId]:
            self.followees[followerId].remove(followeeId)