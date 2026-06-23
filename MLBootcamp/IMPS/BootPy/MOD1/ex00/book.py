from datetime import datetime

from recipe import Recipe


class Book:
    """A cookbook holding recipes sorted by type."""

    def __init__(self, name):
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = datetime.now()
        self.recipes_list = {
            "starter": [],
            "lunch": [],
            "dessert": [],
        }

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name and returns the instance"""
        for recipes in self.recipes_list.values():
            for recipe in recipes:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        print(f"Recipe '{name}' not found in the book.")
        return None

    def get_recipes_by_types(self, recipe_type):
        """Gets all recipes names for a given recipe_type"""
        if recipe_type not in self.recipes_list:
            print(f"Error: '{recipe_type}' is not a valid recipe type.")
            return []
        return [recipe.name for recipe in self.recipes_list[recipe_type]]

    def add_recipe(self, recipe):
        """Adds a recipe to the book and updates last_update"""
        if not isinstance(recipe, Recipe):
            print("Error: argument must be a Recipe instance.")
            return
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()
