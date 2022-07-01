"""Demo Flask application."""
"""$env:FLASK_ENV = "development(to get development on)"""
from urllib import request
from flask import Flask

from random import choice, randint

app = Flask(__name__)

@app.route("/")  
def home_page():
  """Show homepage"""
  
  html = """
  <html>
    <body>
      <h1> hi !!</h1>
      <p>This is the home page</p>
      <a href="/hello">go to hello page</a>
    </body>
  </html>
  """
  return html

@app.route('/hello')
def say_hello():
  """Return simple "Hello" Greeting."""
  
  html = """
  <html>
    <body>
      <h1> Hello!!</h1>
      <p>This is the hello page</p>
    </body>
  </html>
  """
  return html

@app.route("/goodbye")
def say_goodbye():
  return "bye bye"

@app.route('/search')
def search():
  """Handle GET requests like /search?term=fun"""
  
  term = request.args['term']
  sort = request.args['sort']
  return f'<h1> Search Results for: {term} and sort by :{sort}</h1>'

# @app.route("/post", methods=['POST'])
# def post_demo():
#   return "You made a post request"

# @app.route("/post", methods=['GET'])
# def get_demo():
#   return "You made a get request"

@app.route("/add-comment")
def add_comment_form():
  """Show form for adding a comment."""
  
  return """
<h1> add comment </h1>
<form method = "POST">
  <input type = "text" placeholder = "comment" name="comment"/>
  <input type = "text" placeholder = "user name" name="username"/>
  <button>Submit</button>
</form>
"""

@app.route("/add-comment", methods=["POST"])
def save_comment():
  """Handle adding comment."""
  
  comment = request.form["comment"]
  username = request.form["username"]
  return f"""
    <h1>save the comment of :{comment} and User Name of :{username}</h1>
"""

@app.route('/r/<subreddit>')
def ahow_subreddit(subreddit):
  return f"<h1>rwouhf {subreddit}</h1>"

@app.route("/r/<subreddit>/comments/<int:post_id>")
def show_comment(subreddit, post_id):
  
  return f"<h1>viewing comment for post with id: {post_id} form the {subreddit} subreddit</h1>"
POSTS ={
  1: "HI",
  2: "HOLA",
  3: "HOLA3",
  4: "HOLA4",
}

@app.route('/posts/<int:id>')
def find_post(id):
  post = POSTS.get(id, "post not found")
  return f"<p>{post}</p>"

USERS = {
  "whiskey": "Whiskey The Dog",
  "spike": "Spike The Porcupine",
}  

@app.route('/user/<username>')
def show_user_profile(username):
    """Show user profile for user."""

    name = USERS[username]
    return f"<h1>Profile for {name}</h1>"
  
@app.route("/shop/<toy>")
def toy_detail(toy):
    """Show detail about a toy."""

    # Get color from req.args, falling back to None
    color = request.args.get("color")

    return f"<h1>{toy}</h1>Color: {color}"
 
