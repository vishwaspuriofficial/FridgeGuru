class User:
    def __init__(self, name, size, items):
        self.name = name
        self.size = size
        self.items = items

    def updateItems(self, items):
        self.items = items

def getItems(image):
    items = {} #'item: # of items'
    #TODO: Object Classification using YOLO Code goes here
    return items

def getMeals(items):
    #TODO: Research and create prompt for ideal results
    prompt = open("prompt.txt", "r").read()
    #TODO: Plug in items available and their quantities
    #TODO: Send this prompt to BentoML
    #ideas = BentoML(...)
    return ideas