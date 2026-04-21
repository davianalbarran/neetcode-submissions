class Twitter:
    def __init__(self):
        self.users = {}
        self.all_tweets = defaultdict(list)
        self.timestamp = 0 # discrete timesteps

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = {userId}
        self.all_tweets[userId].append([self.timestamp, tweetId])
        self.timestamp -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        if userId not in self.users:
            self.users[userId] = {userId}
        
        for followeeId in self.users[userId]:
            if followeeId in self.all_tweets and len(self.all_tweets[followeeId]) > 0:
                index = len(self.all_tweets[followeeId]) - 1
                timestamp, tweetId = self.all_tweets[followeeId][index]
                min_heap.append([timestamp, tweetId, followeeId, index - 1])

        heapq.heapify(min_heap)
        while min_heap and len(res) < 10:
            timestamp, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)

            if index >= 0:
                next_timestamp, next_tweetId = self.all_tweets[followeeId][index]
                heapq.heappush(min_heap, [next_timestamp, next_tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId] = {followerId}
        if followeeId not in self.users:
            self.users[followeeId] = {followeeId}
        self.users[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users and followeeId != followerId:
            if followeeId in self.users[followerId]:
                self.users[followerId].remove(followeeId)
