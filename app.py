from flask import Flask, request, render_template
import random

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')
    # Below is the previous version of this function
    # 
    # return """
    # <form action="/froyo_results" method="GET">
    #     What is your favorite Fro-Yo flavor? <br/>
    #     <input type="text" name="flavor"><br/>
    #     What are your favorite Fro-Yo toppings? <br/>
    #     <input type="text" name="toppings"><br/>
    #     <input type="submit" value="Submit!">
    # </form>
    # """

@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    context = {
        "users_froyo_flavor": request.args.get('flavor'),
        "users_froyo_toppings": request.args.get('toppings')
    }
    return render_template('froyo_results.html', **context)
    # Below is the previous version of this function
    # 
    # users_froyo_flavor = request.args.get('flavor')
    # users_froyo_toppings = request.args.get('toppings')
    # return f'You ordered {users_froyo_flavor} flavored Fro-Yo with {users_froyo_toppings} toppings!'

@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite color? <br/>
        <input type="text" name="color"><br/>
        What is your favorite animal? <br/>
        <input type="text" name="animal"><br/>
        What is your favorite city? <br/>
        <input type="text" name="city"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    users_fav_color = request.args.get('color')
    users_fav_animal = request.args.get('animal')
    users_fav_city = request.args.get('city')
    return f"Wow, I didn't know {users_fav_color} {users_fav_animal}s lived in {users_fav_city}!"

@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
        Enter your secret message below: <br/>
        <input type="text" name="message"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    # Retrieve the message with `request.form.get()` because POST request used
    input_message = request.form.get('message')
    # Sort the message by calling the helper function defined at the top of the file
    sorted_message = sort_letters(input_message)
    return f"Here's your encrypted secret message: {sorted_message}"

@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')
    # Below is the previous version of this function
    # 
    # return """
    # <form action="/calculator_results" method="GET">
    #     Please enter 2 numbers and select an operator.<br/><br/>
    #     <input type="number" name="operand1">
    #     <select name="operation">
    #         <option value="add">+</option>
    #         <option value="subtract">-</option>
    #         <option value="multiply">*</option>
    #         <option value="divide">/</option>
    #     </select>
    #     <input type="number" name="operand2">
    #     <input type="submit" value="Submit!">
    # </form>
    # """

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    # Retrieve the two operands and cast them as integers and retrieve the operation selected from the drop-down menu
    context = {
        'operand1': int(request.args.get('operand1')),
        'operand2': int(request.args.get('operand2')),
        'operation': request.args.get('operation')
    }
    # Compute the calculation based on the operation selected and add the result to the `context` dictionary
    if context['operation'] == "add":
        context['result'] = context['operand1'] + context['operand2']
    elif context['operation'] == "subtract":
        context['result'] = context['operand1'] - context['operand2']
    elif context['operation'] == "multiply":
        context['result'] = context['operand1'] * context['operand2']
    elif context['operation'] == "divide":
        context['result'] = context['operand1'] / context['operand2']

    return render_template('calculator_results.html', **context)
    # Below is the previous version of this function
    # 
    # # Retrieve the two operands and cast them as integers
    # operand1 = int(request.args.get('operand1'))
    # operand2 = int(request.args.get('operand2'))
    # # Retrieve the operation selected from the drop-down menu
    # operation = request.args.get('operation')
    # # Compute the calculation based on the operation selected
    # if operation == "add":
    #     result = operand1 + operand2
    # elif operation == "subtract":
    #     result = operand1 - operand2
    # elif operation == "multiply":
    #     result = operand1 * operand2
    # elif operation == "divide":
    #     result = operand1 / operand2
    # return f"You chose to {operation} {operand1} and {operand2}. Your result is: {result}."
    


# List of compliments to be used in the `compliments_results` route (feel free 
# to add your own!) 
# https://systemagicmotives.com/positive-adjectives.htm
list_of_compliments = [
    'awesome',
    'beatific',
    'blithesome',
    'conscientious',
    'coruscant',
    'erudite',
    'exquisite',
    'fabulous',
    'fantastic',
    'gorgeous',
    'indubitable',
    'ineffable',
    'magnificent',
    'outstanding',
    'propitioius',
    'remarkable',
    'spectacular',
    'splendiferous',
    'stupendous',
    'super',
    'upbeat',
    'wondrous',
    'zoetic'
]

@app.route('/compliments')
def compliments():
    """Shows the user a form to get compliments."""
    return render_template('compliments_form.html')

@app.route('/compliments_results')
def compliments_results():
    """Show the user some compliments."""
    # Save keys and values from compliments_form.html
    context = {
        'users_name': request.args.get('users_name'),
        'wants_compliments': request.args.get('wants_compliments'),
        'num_compliments': int(request.args.get('num_compliments'))
    }
    # Append the dictionary with a random sample of compliments (dictionary name cannot be called before initialization)
    context['random_compliments'] = random.sample(list_of_compliments, k=context['num_compliments'])

    return render_template('compliments_results.html', **context)


if __name__ == '__main__':
    app.run()
