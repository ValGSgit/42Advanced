from book import Book
from recipe import Recipe

# --- Create some valid recipes ---
tourte = Recipe(
    "Tourte",
    3,
    60,
    ["flour", "eggs", "butter", "apples"],
    "A delicious apple pie",
    "dessert",
)

salad = Recipe(
    "Caesar Salad",
    1,
    15,
    ["lettuce", "croutons", "parmesan"],
    "",  # description can be empty
    "starter",
)

pasta = Recipe(
    "Pasta Carbonara",
    2,
    25,
    ["pasta", "eggs", "bacon", "parmesan"],
    "Classic Italian pasta",
    "lunch",
)

# --- Test __str__ ---
print("=== str(tourte) ===")
to_print = str(tourte)
print(to_print)

book = Book("My Cookbook")
print("=== Book created ===")
print(f"Name: {book.name}")
print(f"Creation date: {book.creation_date}")
print(f"Last update:   {book.last_update}\n")


book.add_recipe(tourte)
book.add_recipe(salad)
book.add_recipe(pasta)
print(f"Last update after adds: {book.last_update}\n")

print("=== get_recipe_by_name('Pasta Carbonara') ===")
found = book.get_recipe_by_name("Pasta Carbonara")
print(f"Returned instance: {found.name}\n")

print("=== get_recipe_by_name('Unknown') ===")
book.get_recipe_by_name("Unknown")
print()

# --- get_recipes_by_types ---
print("=== get_recipes_by_types('dessert') ===")
print(book.get_recipes_by_types("dessert"), "\n")

# --- Error handling: not a Recipe ---
print("=== add_recipe('not a recipe') ===")
book.add_recipe("not a recipe")
print()

print("=== add_recipe(shit) ===")
book.add_recipe(Recipe("Warm Shit", 5, 69, ["Food", "Water", "Gastric fluid"], "In the mood for chocolate but youre diabetic? no problem!", \
                    "dessert"))

last = str(book.get_recipe_by_name("Warm Shit"))
print(last)

# --- Error handling: invalid recipe (uncomment to test the exit) ---
# bad = Recipe("Bad", 9, 10, ["x"], "", "dessert")  # cooking_lvl out of range
