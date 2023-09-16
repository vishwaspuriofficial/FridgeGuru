from taipy.gui import Gui, Markdown, notify

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


from taipy.gui import Gui, Markdown, notify

def __init__(css_file="./styling.css"):
    return

page = Markdown(
    """
<img src="banner.png" alt="NavBar" class="banner"/>

  <div class="special">
    <div>
      <h2 id="description">Do you need help thinking of recipes? 🤔</h2>
      <p id="description" class="text">Have no idea what to make with the contents left in your fridge? FridgeGuru
        provides easy and delicious recipes tailored to your preferences based on only what you have at home! Simply
        take
        one picture of your entire fridge showing all its contents, and get recipe recommendations in an instant. 🙀</p>
    </div>
    <img src="fridge.png" alt="Fridge" class="fridge"/>
  </div>
  <div class="main">
    <div class="section">
      <h2>1. Create A Profile ⭐️</h2>
      <input id="profile" type="text" placeholder="Name" />
      <input id="profile" type="number" placeholder="Number of Portions" />
      <input id="profile" type="test" placeholder="Prefrence Eg. Indian Food" />

    </div>
    <div class="section">
      <button class="submit-button">Submit</button>
    </div>

    <div class="section">
      <h2>2. Upload a picture ⬆️</h2>
      <div class="upload-btn-wrapper">
        <button class="btn">Upload a file</button>
        <input type="file" name="myfile" />
      </div>
    </div>

    <div class="section">
      <h2>3. Recipes! 🥗</h2>

    </div>
  </div>
  <div class="footer">
    <div class="logo">
      <img src="logo.png" alt="Logo"/>
    </div>
    <div class="footer-content">
      <p>fridgeguru@gmail.com</p>
      <p>200 University Avenue West Waterloo, Ontario</p>
    </div>
  </div>
"""
)


# def image_action(state):
#     webbrowser.open("https://taipy.io")


def on_push(state):
    ...


def on_slider(state):
    if state.value == 100:
        notify(state, "success", "Taipy is running!")


def on_change(state, var_name: str, var_value):
    ...


if __name__ == "__main__":
    gui = Gui(page=page)
    gui.run(title="Recipe Maker")