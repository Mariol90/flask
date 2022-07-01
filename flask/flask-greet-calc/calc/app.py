# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div


# /add
#     Adds a and b and returns result as the body.
# /sub
#     Same, subtracting b from a.
# /mult
#     Same, multiplying a and b.
# /div
#     Same, dividing a by b. 

app = Flask(__name__)

@app.route("/add")
def do_add():
    """Add a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)

@app.route("/sub")
def do_sub():
    """subtracting b from a"""
    a= int(request.args.get("a"))
    b= int(request.args.get("b"))
    
    result = sub(a,b)
    
    return str(result)

@app.route("/mult")
def do_mult():
    """mmultiplying b from a"""
    a= int(request.args.get("a"))
    b= int(request.args.get("b"))
    
    result = mult(a,b)
    
    return str(result)

@app.route("/div")
def do_div():
    """dividing b from a"""
    a= int(request.args.get("a"))
    b= int(request.args.get("b"))
    
    result = div(a,b)
    
    return str(result)

operators ={
  "add": add,
  "sub": sub,
  "mult": mult,
  "div": div,
}

@app.route("/math/<ope>")
def do_oparators(ope):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[ope](a,b)
    return str(result)
