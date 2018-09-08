from flask import Flask, render_template
import requests  # import requests module to allow for pokeAPI use

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


@app.route('/pokemon/<int:pokemon_id>', methods=['GET'])  # restrict dynamic route to GET to comply with pokeAPI
def get_pokemon_name(pokemon_id):

    request_url = "https://pokeapi.co/api/v2/pokemon/" + str(pokemon_id)
    poke_request = requests.get(request_url)  # make a new request from pokeAPI
    api_output = poke_request.json()  # requests.json() returns json data from the api as a dict

    if 'name' in api_output:  # check if given id corresponds with an existing pokemon
        return "The pokemon with id " + str(pokemon_id) + " is " + api_output['name']
    else:
        return "There is no pokemon with id " + str(pokemon_id)


if __name__ == '__main__':
    app.run()
