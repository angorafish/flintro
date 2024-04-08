from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# Mapping of operation names to their functions.
operations = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div,
}

@app.route('/math/<operation>')
def do_math(operation):
    # Try to retrieve the operation function from dictionary.
    operation_func = operations.get(operation)
    # If the operation is invalid, return an error.
    if not operation_func:
        return "Invalid operation", 404
    # Try to extract 'a' and 'b' from the URL query string
    # and convert them to integers. If either 'a' or 'b' 
    # are blank or are not integers, return an error.
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))
    except (TypeError, ValueError):
        return "Invalid input. Please ensure 'a' and 'b' are integers.", 400
    
    # Performs the operation and returns the result as a string.
    result = operation_func(a, b)
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)