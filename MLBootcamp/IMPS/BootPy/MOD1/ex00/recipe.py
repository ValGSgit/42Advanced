import sys


class Recipe:
    """A cooking recipe with its main characteristics."""

    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, description, recipe_type):
        try:
            # name: non-empty string
            if not isinstance(name, str) or name == "":
                raise ValueError("name must be a non-empty string")
            self.name = name

            # cooking_lvl: int from 1 to 5
            if not isinstance(cooking_lvl, int) or isinstance(cooking_lvl, bool):
                raise ValueError("cooking_lvl must be an int")
            if not 1 <= cooking_lvl <= 5:
                raise ValueError("cooking_lvl must range from 1 to 5")
            self.cooking_lvl = cooking_lvl

            # cooking_time: int in minutes, no negative numbers
            if not isinstance(cooking_time, int) or isinstance(cooking_time, bool):
                raise ValueError("cooking_time must be an int")
            if cooking_time < 0:
                raise ValueError("cooking_time cannot be negative")
            self.cooking_time = cooking_time

            # ingredients: list of non-empty strings
            if not isinstance(ingredients, list):
                raise ValueError("ingredients must be a list")
            if not all(isinstance(i, str) and i != "" for i in ingredients):
                raise ValueError("ingredients must be a list of non-empty strings")
            self.ingredients = ingredients

            # description: string (can be empty)
            if not isinstance(description, str):
                raise ValueError("description must be a string")
            self.description = description

            # recipe_type: "starter", "lunch" or "dessert"
            if recipe_type not in ("starter", "lunch", "dessert"):
                raise ValueError(
                    'recipe_type must be "starter", "lunch" or "dessert"')
            self.recipe_type = recipe_type

        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)

    def __str__(self):
        """Returns the string to print with the recipe's info"""
        txt = ""
        txt += f"Recipe name: {self.name}\n"
        txt += f"Cooking level: {self.cooking_lvl}\n"
        txt += f"Cooking time: {self.cooking_time} minutes\n"
        txt += f"Ingredients: {', '.join(self.ingredients)}\n"
        txt += f"Description: {self.description}\n"
        txt += f"Recipe type: {self.recipe_type}\n"
        return txt
