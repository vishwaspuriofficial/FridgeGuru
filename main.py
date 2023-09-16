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


def __init__(css_file="./styling.css"):
    return


page = Markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inclusive+Sans&family=Lato&display=swap');

body {
    font-family: 'Lato', sans-serif;
    /* Use Kollektif font */
    color: #064F3C;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.navbar {
    background-color: #FA9B76;
    color: white;
    padding: 10px 20px;
    display: flex;
    align-items: center;
}

.navbar img {
    width: 50px;
    margin-right: 10px;
}

.main {
    padding: 20px;
}

.fridge {
    /* width: 50px; */
    margin-left: 10px;

    /* padding-right: 15px; */
}

.section {
    margin-bottom: 30px;
}

.section h2 {
    font-size: 36px;
    margin-bottom: 10px;
}

.section input,
.section select {
    width: 100%;
    padding: 10px;
    font-size: 16px;
    margin-bottom: 10px;
}

.section .upload-btn-wrapper {
    position: relative;
    overflow: hidden;
    display: inline-block;
}

.section .btn {
    border: 2px solid gray;
    color: gray;
    background-color: white;
    padding: 8px 20px;
    border-radius: 8px;
    font-size: 16px;
    font-weight: bold;
}

.section .upload-btn-wrapper input[type=file] {
    font-size: 100px;
    position: absolute;
    left: 0;
    top: 0;
    opacity: 0;
}

.list {
    list-style-type: none;
    padding: 0;
}

.list li {
    font-size: 20px;
    margin-bottom: 10px;
}

.description {
    flex-grow: 1;
}

#profile {
    width: 80%;
}


.h1 {
    font-size: 36px;
    max-width: 100%;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;

}

#description {

    padding-left: 20px;
    max-width: 650px;
    box-sizing: border-box;
}

img.fridge {
    display: block;
    margin: auto;
    /* padding-top: 10px; */

}

.submit-button {
    padding: 10px 20px;
    font-size: 16px;
    background-color: #0B8565;
    color: white;
    border: none;
    cursor: pointer;
}

.submit-button:hover {
    background-color: #064F3C;
}

.special {
    display: grid;
    align-items: center;
    grid-template-columns: 2fr 2fr;
    /* Two equal-width columns */
    gap: 5px;
    /* Adjust as needed for spacing */
}

.text,
.fridge {
    flex: 1;
}

.fridge {
    max-width: 90%;
    border-radius: 10px;
}

.container {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
}

.image img {
    max-width: 100%;
    height: auto;
    border-radius: 5px;
}

.footer {

    border-top: 1px solid #ccc;
    padding: 10px 0;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.logo img {
    max-width: 100%;
    height: 50px;
    ;
    display: inline-block;
    margin-top: 10px
        /* Add some space between logo and footer content */
}

.footer-content {
    text-align: center;
}

.upload-btn-wrapper {
    justify-content: center;
    align-items: center;
    text-align: center;
}

.banner {
    width: 100%;
}
</style>
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
