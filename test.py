class token:
    def __init__(self, tag, func, val):
        self.tag = tag
        self.func = func
        self.val = val
    
    def __str__(self):
        return f"{self.tag}, {self.func}, {self.val}"


test = token("test", "func", "val")
print(test)
