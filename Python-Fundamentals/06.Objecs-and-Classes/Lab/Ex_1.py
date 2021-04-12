class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes

    def printing(self):
        return f"{self.username}\n{self.content}\n{self.likes}"


comment = Comment("user1", "I like this book")
print(comment.printing())
