class User:

    def __init__(self, user_id, user_name):
        self.id = user_id
        self.username = user_name
        self.follower = 0
        self.following = 0

        print("User created")

    def follow(self,user):
        user.follower += 1
        self.following += 1


user_1 = User("001", "Luke")



