from flask import Flask, jsonify, request

app = Flask(__name__)

recipes = {
    'apple': {'ingredients': ['Apple', 'Sugar', 'Cinnamon'], 'steps': ['Cut apple', 'Add sugar and cinnamon', 'Bake']},
    'banana': {'ingredients': ['Banana', 'Honey'], 'steps': ['Peel banana', 'Drizzle with honey']}
}

@app.route('/get-recipe', methods=['GET'])
def get_recipe():
    ingredient = request.args.get('ingredient')
    recipe = recipes.get(ingredient.lower())
    if recipe:
        return jsonify(recipe)
    else:
        return jsonify({'error': 'Recipe not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
