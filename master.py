from taipy.gui import Gui, notify

name = ""
pref = ""  
image = ""
size = 0
d = ""
h1 = "" 
h2 = "" 
h3 = ""
d1 = ""
d2 = "" 
d3 = ""

items = {}

def getMeals(name, pref, size):
    items = [{'apple':1}]  # 'item: # of items'
    # TODO: Object Classification using YOLO Code goes here
    meals=[f'Hello {name}, here is few {pref} meals you can make for {size} people:','1. Contrary to popular belief:', 'Lorem Ipsum is not simply random text It has roots in a piece of classical Latin literature from 45 BC', '2. Contrary to popular belief:', 'Lorem Ipsum is not simply random text It has roots in a piece of classical Latin literature from 45 BC', '3. Contrary to popular belief:', 'Lorem Ipsum is not simply random text It has roots in a piece of classical Latin literature from 45 BC'] 
    return meals

# class User:
#     def getItems(image):
#         items = {'apple':1}  # 'item: # of items'
#         # TODO: Object Classification using YOLO Code goes here
#         return items
#     def __init__(self, name, size, image):
#         self.name = name
#         self.size = size
#         self.items = getItems(image)

#          # TODO: Research and create prompt for ideal results
#         prompt = open("prompt.txt", "r").read()
#         # TODO: Plug in items available and their quantities
#         # TODO: Send this prompt to BentoML
#         ideas = "Hello" + name
#         # ideas = BentoML(...)
#         return ideas

page = """
Name:  \n
<|{name}|input|>


Portion Size: <|{size}|>   
<|{size}|slider|min=1|max=10|>


Preferences:  
<|{pref}|input|>


Input a image of your fridge:   
<input type="file" accept="image/*" />


<|Submit|button|on_action=submit|>


<|{d}|>


<|{h1}|>

<|{d1}|>


<|{h2}|>

<|{d2}|>


<|{h3}|>

<|{d3}|>
"""

def submit(state):
    state.d, state.h1, state.d1, state.h2, state.d2, state.h3, state.d3 = getMeals(state.name, state.pref, state.size)
    # state.text = "Button Pressed"
    # notify(state, 'info', f'The text is: {state.text}')
    

# def on_change(state, var_name, var_value):
#     if var_name == "text" and var_value == "Reset":
#         state.text = ""
#         return

# def on_push(state):
#     ...


# def on_slider(state):
#     if state.value == 100:
#         notify(state, "success", "Taipy is running!")


# def on_change(state, var_name: str, var_value):
#     ...


if __name__ == "__main__":
    gui = Gui(page=page)
    gui.run(title="Fridge Guru")
