# A fastAPI application to tell fortunes

from fastapi import FastAPI
from fastapi.params import Form
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    """
    Shows a form which takes in the user's name, and a submit button.
    When the submit button is clicked, the user's fortune is displayed.

    Args:
        None

    Returns:
        HTMLResponse: A form to take in the user's name and display the fortune.
    """
    return HTMLResponse("""
    <html>
        <head>
            <title>Fortune Teller</title>
        </head>
        <body>
            <h1>Fortune Teller</h1>
            <form action="/fortune" method="post">
                <label for="name">Enter your name:</label>
                <input type="text" id="name" name="name" required>
                <button type="submit">Get my fortune</button>
            </form>
        </body>
    </html>
    """)

@app.post("/fortune", response_class=HTMLResponse)
async def fortune(name: str = Form(...)):
    """
    Displays a fortune for the user based on their name.

    Args:
        name (str): The name of the user.

    Returns:
        HTMLResponse: A message displaying the user's fortune.
    """
    fortunes = [
        "You will have a great day!",
        "Something wonderful is about to happen.",
        "Be cautious of new opportunities.",
        "Happiness is around the corner.",
        "A surprise is waiting for you."
    ]
    fortune = random.choice(fortunes)
    return HTMLResponse(f"""
    <html>
        <head>
            <title>Your Fortune</title>
        </head>
        <body>
            <h1>Hello, {name}!</h1>
            <p>Your fortune is: {fortune}</p>
            <a href="/">Go back</a>
        </body>
    </html>
    """)
