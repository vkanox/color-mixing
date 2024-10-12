while True:
    # User input
    color_one = input("Choose the first color you want to mix: ").strip().lower()
    color_two = input("Choose the second color: ").strip().lower()

    # Dictionary of color combinations with common names
    color_combinations = {
        # Primary and Secondary Colors
        "red + blue": "Purple",
        "red + yellow": "Orange",
        "blue + yellow": "Green",
        "orange + blue": "Brown",
        "purple + yellow": "Brown",
        "green + red": "Brown",
        "blue + green": "Teal",
        "red + green": "Brown",
        "red + purple": "Magenta",
        "cyan + red": "Pink",
        "cyan + blue": "Teal",

        # Variations with Black, White, and Gray
        "red + black": "Dark Red",
        "blue + black": "Navy",
        "yellow + black": "Dark Yellow",
        "green + black": "Dark Green",
        "purple + black": "Dark Purple",
        "pink + black": "Dark Pink",
        "white + red": "Pink",
        "white + blue": "Light Blue",
        "white + yellow": "Light Yellow",
        "white + green": "Mint Green",
        "white + purple": "Lavender",
        "gray + red": "Pinkish Gray",
        "gray + blue": "Blue Gray",
        "gray + yellow": "Light Gray",
        "gray + green": "Sage Green",
        
        # Shades and Tints
        "red + white": "Pink",
        "blue + white": "Light Blue",
        "yellow + white": "Light Yellow",
        "green + white": "Mint",
        "purple + white": "Lavender",
        "orange + white": "Light Orange",
        "brown + white": "Light Brown",
        "pink + white": "Light Pink",
        
        # Other Common Combinations
        "red + orange": "Coral",
        "orange + yellow": "Gold",
        "yellow + green": "Lime",
        "blue + orange": "Brown",
        "blue + purple": "Lavender",
        "green + blue": "Teal",
        "green + yellow": "Lime",
        "pink + red": "Light Pink",
        "pink + yellow": "Peach",
        "brown + red": "Dark Brown",
        "brown + yellow": "Tan",
        "brown + green": "Olive",
        
        # Miscellaneous Combinations
        "purple + pink": "Lavender",
        "cyan + yellow": "Light Green",
        "cyan + green": "Turquoise",
        
        # Additional Common Combinations
        "violet + yellow": "Brown",
        "violet + red": "Magenta",
        "gold + red": "Orange",
        "gold + blue": "Green",
        "silver + black": "Gray",
        "silver + blue": "Steel Blue",
        "silver + red": "Pink",
        "brown + black": "Dark Brown",
        "brown + white": "Light Brown",
        
        # More Simple Combinations
        "red + gray": "Pinkish Gray",
        "red + blue": "Purple",
        "blue + yellow": "Green",
        "green + blue": "Teal",
        "orange + green": "Brown",
        "blue + pink": "Light Purple",
        "green + pink": "Light Green",
        "purple + teal": "Dark Purple",
        "light red + blue": "Light Purple",
        "gold + silver": "Light Gold",
        "light orange + blue": "Peach",
        "green + yellow": "Lime",
        "blue + red": "Purple",
        "light gray + pink": "Light Pink",
        "pink + teal": "Light Teal",
        "light green + yellow": "Light Lime",
        "dark gray + blue": "Steel Blue",
    }

    # Check if the combination exists
    combination1 = f"{color_one} + {color_two}"
    combination2 = f"{color_two} + {color_one}"

    if combination1 in color_combinations:
        print(f"The color created by mixing {color_one} and {color_two} is {color_combinations[combination1]}.")
    elif combination2 in color_combinations:
        print(f"The color created by mixing {color_two} and {color_one} is {color_combinations[combination2]}.")
    else:
        print("Sorry, that color combination was not found.")

    # Ask if the user wants to mix more colors
    restart = input("Do you want to mix more colors? (yes/no): ").strip().lower()
    if restart != "yes":
        print("Thank you for using my color mixer. Goodbye!")
        break
