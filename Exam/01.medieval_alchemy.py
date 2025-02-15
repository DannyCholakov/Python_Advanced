def alchemy_process(substances, crystals):
    # Required energy levels for the potions
    required_potions = {
        110: "Brew of Immortality",
        100: "Essence of Resilience",
        90: "Draught of Wisdom",
        80: "Potion of Agility",
        70: "Elixir of Strength"
    }

    crafted_potions = []
    substances = list(map(int, substances.split(", ")))  # Convert input to list of integers
    crystals = list(map(int, crystals.split(", ")))  # Convert input to list of integers

    while substances and crystals and len(crafted_potions) < 5:
        substance = substances.pop()  # Take the last substance
        crystal = crystals.pop(0)  # Take the first crystal
        combined_energy = substance + crystal

        # Check if the combined energy matches any of the required potions
        if combined_energy in required_potions and required_potions[combined_energy] not in crafted_potions:
            crafted_potions.append(required_potions[combined_energy])  # Craft the potion
        else:
            # Try to craft the highest possible potion that is less than the combined energy
            possible_potion = None
            for energy in sorted(required_potions.keys(), reverse=True):
                if energy < combined_energy and required_potions[energy] not in crafted_potions:
                    possible_potion = energy
                    break

            if possible_potion:
                crafted_potions.append(required_potions[possible_potion])  # Craft the potion
                # Remove the substance and return the crystal with reduced energy
                crystals.append(crystal - 20 if crystal - 20 > 0 else 0)
            else:
                # If no potion can be crafted, return the crystal with reduced energy
                crystals.append(crystal - 5 if crystal - 5 > 0 else 0)
                # Remove the substance

        # Remove exhausted crystals
        crystals = [crystal for crystal in crystals if crystal > 0]

    # Print the results
    if len(crafted_potions) == 5:
        print("Success! The alchemist has forged all potions!")
    else:
        print("The alchemist failed to complete his quest.")

    if crafted_potions:
        print(f"Crafted potions: {', '.join(crafted_potions)}")

    if substances:
        print(f"Substances: {', '.join(map(str, substances[::-1]))}")

    if crystals:
        print(f"Crystals: {', '.join(map(str, crystals))}")


# User input
substances_input = input()  # Input the substances
crystals_input = input()  # Input the crystals

alchemy_process(substances_input, crystals_input)
