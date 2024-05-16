class Twitter:

    def __init__(self):
        self.userToFollowees = defaultdict(set) 
        self.userToTweets = defaultdict(list) 
        self.time = 0      

    def postTweet(self, userId: int, tweetId: int) -> None:
        '''
        Track time tweet was posted. Increment every time.
        '''
        self.time += 1
        self.userToTweets[userId].append((self.time, userId, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        '''
        Add user to list of user's followees
        Loop list of user's followees
            Loop list of tweets made by the followee 
            Get the frontier of each list [last tweet added / most recent tweet posted]
            Add to a max heap. Invert time. Add index of value inside tweet list (so that when you pop the tweet from heap, you can find the tweet after it and push it to the heap).
        Heapify 
        Pop from list until empty.    
            Add to res
            Break if 10 items added
            Find previous tweet if present. Index - 1 of same tweet list
        '''

        self.userToFollowees[userId].add(userId)

        maxHeap = []
        for userFolloweeId in self.userToFollowees[userId]:
            followeeTweets = self.userToTweets[userFolloweeId]
            if followeeTweets:
                frontierIdx = len(followeeTweets)-1
                frontierTime, frontierUserId, frontierTweetId = followeeTweets[-1]
                maxHeap.append((frontierTime * -1, frontierUserId, frontierTweetId, frontierIdx))
        heapify(maxHeap)

        res = []
        while maxHeap:
            tweetTime, tweetUserId, tweetId, tweetIdx = heappop(maxHeap)
            res.append(tweetId)
            if len(res) == 10: break
            if tweetIdx > 0:
                nextTweetTime, nextTweetUserId, nextTweetId = self.userToTweets[tweetUserId][tweetIdx-1]
                heappush(maxHeap, (nextTweetTime * -1, nextTweetUserId, nextTweetId, tweetIdx-1))
        return res       


    def follow(self, followerId: int, followeeId: int) -> None:
        self.userToFollowees[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userToFollowees[followerId]:
            self.userToFollowees[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
