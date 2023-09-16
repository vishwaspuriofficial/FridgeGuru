from taipy.gui import Gui, Markdown, notify


class User:
    def __init__(self, name, size, items):
        self.name = name
        self.size = size
        self.items = items

    def updateItems(self, items):
        self.items = items


def getItems(image):
    items = {}  # 'item: # of items'
    # TODO: Object Classification using YOLO Code goes here
    return items


def getMeals(items):
    # TODO: Research and create prompt for ideal results
    prompt = open("prompt.txt", "r").read()
    # TODO: Plug in items available and their quantities
    # TODO: Send this prompt to BentoML
    # ideas = BentoML(...)
    return ideas


page = Markdown(
    """
<div style="font-family: 'Lato', sans-serif; background-color:#FCFCFC; color: #064F3C; margin: 0; padding: 0; box-sizing: border-box;">

    <img src="banner.png" alt="NavBar" class="banner" style="width: 100%;" />

    <div class="special" style="display: grid; align-items: center; grid-template-columns: 2fr 2fr; gap: 5px;">
        <div>
            <h2 id="description" style="padding-left: 20px; max-width: 650px; box-sizing: border-box;">Do you need help thinking of recipes? 🤔</h2>
            <p id="description" class="text" style="flex-grow: 1; padding-left:20px;">Have no idea what to make with the contents left in your fridge? FridgeGuru provides easy and delicious recipes tailored to your preferences based on only what you have at home! Simply take one picture of your entire fridge showing all its contents, and get recipe recommendations in an instant. 🙀</p>
        </div>
        <img src="fridge.png" alt="Fridge" class="fridge" style="max-width: 90%; border-radius: 10px;" />
    </div>
<div class="main" style="padding: 20px;">
<div class="section" style="margin-bottom: 30px;">
<h2 style="font-size: 36px; margin-bottom: 10px;">1. Create A Profile ⭐️</h2>
<input id="profile" type="text" placeholder="Name" style="width: 80%;" />
 <input id="profile" type="number" placeholder="Number of Portions" style="width: 80%;" />
<input id="profile" type="test" placeholder="Preference Eg. Indian Food" style="width: 80%;" />
</div>
<div class="section" style="margin-bottom: 30px;">
<button class="submit-button" style="padding: 10px 20px; font-size: 16px; background-color: #0B8565; color: white; border: none; cursor: pointer;">Submit</button>
</div>
<div class="section" style="margin-bottom: 30px;">
<h2 style="font-size: 36px; margin-bottom: 10px;">2. Upload a picture ⬆️</h2>
 <div class="upload-btn-wrapper" style="position: relative; overflow: hidden; display: inline-block;">
                <button class="btn" style="border: 2px solid gray; color: gray; background-color: white; padding: 8px 20px; border-radius: 8px; font-size: 16px; font-weight: bold;">Upload a file</button>
                <input type="file" name="myfile" style="font-size: 100px; position: absolute; left: 0; top: 0; opacity: 0;" />
            </div>
        </div>

        <div class="section" style="margin-bottom: 30px;">
            <h2 style="font-size: 36px; margin-bottom: 10px;">3. Recipes! 🥗</h2>
        </div>

    </div>

    <div class="footer" style="border-top: 1px solid #ccc; padding: 10px 0; display: flex; justify-content: center; align-items: center; flex-direction: column;">
        <div class="logo" style="text-align: center;">
            <img src="logo.png" alt="Logo" style="max-width: 100%; height: 50px; display: inline-block; margin-top: 10px;" />
        </div>
        <div class="footer-content" style="text-align: center;">
            <p>fridgeguru@gmail.com</p>
            <p>200 University Avenue West Waterloo, Ontario</p>
        </div>
    </div>
  <div class="grid-item" style="border: 1px solid #ccc; padding: 20px;">
            <div class="header" style="font-size: 24px; margin-bottom: 10px; color: #064F3C;">Box 1 Header</div>
            <div class="description" style="font-size: 16px;">This is the description for Box 1.</div>
        </div>

        <div class="grid-item" style="border: 1px solid #ccc; padding: 20px;">
            <div class="header" style="font-size: 24px; margin-bottom: 10px; color: #0B8565;">Box 2 Header</div>
            <div class="description" style="font-size: 16px;">This is the description for Box 2.</div>
        </div>

        <div class="grid-item" style="border: 1px solid #ccc; padding: 20px;">
            <div class="header" style="font-size: 24px; margin-bottom: 10px; color: #FA9B76;">Box 3 Header</div>
            <div class="description" style="font-size: 16px;">This is the description for Box 3.</div>
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
