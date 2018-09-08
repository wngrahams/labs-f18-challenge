from flask import Flask, render_template
from string import Template
import requests  # import requests module to allow for pokeAPI use

app = Flask(__name__)

HTML_FORMAT_TEMPLATE = Template('''<html>
  <head>
    <title>Pokemon Lookup: ${title_placeholder}</title>
  </head>
  <body>
    <h1>${output_placeholder}</h1>
  </body>
</html>''')


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@app.route('/pokemon/<int:pokemon_id>', methods=['GET'])  # restrict dynamic route to GET to comply with pokeAPI
def get_pokemon_name(pokemon_id):

    request_url = "https://pokeapi.co/api/v2/pokemon/" + str(pokemon_id)
    poke_request = requests.get(request_url)  # make a new request from pokeAPI
    api_output = poke_request.json()  # requests.json() returns json data from the api as a dict

    title = "ID=" + str(pokemon_id)

    if 'name' in api_output:  # check if given id corresponds with an existing pokemon
        output = "The pokemon with id " + str(pokemon_id) + " is " + (api_output['name']).capitalize()
        return HTML_FORMAT_TEMPLATE.substitute(title_placeholder=title, output_placeholder=output)
    else:
        output = "There is no pokemon with id " + str(pokemon_id)
        return HTML_FORMAT_TEMPLATE.substitute(title_placeholder=title, output_placeholder=output)


@app.route('/pokemon/<string:pokemon_name>', methods=['GET'])  # restrict dynamic route to GET to comply with pokeAPI
def get_pokemon_id(pokemon_name):

    request_url = "https://pokeapi.co/api/v2/pokemon/" + str(pokemon_name)
    poke_request = requests.get(request_url)  # make a new request from pokeAPI
    api_output = poke_request.json()  # requests.json() returns json data from the api as a dict

    title = "Name=" + str(pokemon_name)

    if 'id' in api_output:  # check if there is a pokemon with the given name
        output = str(pokemon_name).capitalize() + " has id " + str(api_output['id'])
        return HTML_FORMAT_TEMPLATE.substitute(title_placeholder=title, output_placeholder=output)
    else:
        output = "There is no pokemon named " + str(pokemon_name).capitalize()
        return HTML_FORMAT_TEMPLATE.substitute(title_placeholder=title, output_placeholder=output)


if __name__ == '__main__':
    app.run()
