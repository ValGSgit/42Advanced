cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10,
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60,
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15,
    }
}


def print_recipe_names():
    """Print all recipe's"""
    for recipe in cookbook.keys():
        print(recipe)

def print_recipe(recipe_name):
    """Print details of a specific recipe."""
    recipe_name = recipe_name.lower()
    for key in cookbook.keys():
        if key.lower() == recipe_name:
            recipe = cookbook[key]
            print(f"Recipe for {key}:")
            print(f"Ingredients list: {recipe['ingredients']}")
            print(f"To be eaten for {recipe['meal']}.")
            print(f"Takes {recipe['prep_time']} minutes of cooking.")
            return
    print(f"Recipe '{recipe_name}' not found.")


def delete_recipe(recipe_name):
    """Delete a recipe from the cookbook."""
    recipe_name = recipe_name.lower()
    for key in list(cookbook.keys()):
        if key.lower() == recipe_name:
            del cookbook[key]
            print(f"Recipe '{key}' deleted.")
            return
    print(f"Recipe '{recipe_name}' not found.")


def add_recipe():
    """Add a new recipe to the cookbook via user input."""
    name = input("Enter a name:\n")
    
    ingredients = []
    print("Enter ingredients:")
    while True:
        ingredient = input()
        if ingredient:
            ingredients.append(ingredient)
        else:
            break
    
    meal = input("Enter a meal type:\n")
    while True:
        prep_time_input = input("Enter a preparation time:\n")
        try:
            prep_time = int(prep_time_input)
            break
        except ValueError:
            print("Please enter a valid number.")
    
    cookbook[name] = {
        "ingredients": ingredients,
        "meal": meal,
        "prep_time": prep_time,
    }
    print(f"Recipe '{name}' added successfully.")


def print_cookbook():
    """Print all recipes in the cookbook."""
    for recipe_name, recipe in cookbook.items():
        print(f"Recipe for {recipe_name}:")
        print(f"Ingredients list: {recipe['ingredients']}")
        print(f"To be eaten for {recipe['meal']}.")
        print(f"Takes {recipe['prep_time']} minutes of cooking.")
        print()


def main():
    """Main program loop for the cookbook."""
    print("Welcome to the Python Cookbook !")
    
    while True:
        print("List of available options:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")
        
        choice = input("Please select an option:\n>> ")
        
        if choice == "1":
            add_recipe()
        elif choice == "2":
            recipe_name = input("Please enter a recipe name to delete:\n>> ")
            delete_recipe(recipe_name)
        elif choice == "3":
            recipe_name = input("Please enter a recipe name to get its details:\n>> ")
            print_recipe(recipe_name)
        elif choice == "4":
            print_cookbook()
        elif choice == "5":
            print("Cookbook closed. Goodbye !")
            break
        else:
            print("Sorry, this option does not exist.")
        print()


if __name__ == "__main__":
    main()