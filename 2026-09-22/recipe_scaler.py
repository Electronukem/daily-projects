# Recipe Scaler (Medium)
# Scale ingredient amounts to a target serving count, rounding to the nearest
# quarter unit and merging duplicate ingredient names case-insensitively.
# Time: O(n) | Space: O(n)

def scale_recipe(ingredients, original_servings, target_servings):
    factor = target_servings / original_servings
    merged = {}
    for name, amount in ingredients.items():
        key = name.strip().lower()
        scaled = amount * factor
        rounded = round(scaled * 4) / 4
        merged[key] = merged.get(key, 0) + rounded
    return merged

# Tests
assert scale_recipe({"Flour": 2.0, "flour": 1.0, "Sugar": 0.5}, 4, 6) == {"flour": 4.5, "sugar": 0.75}
assert scale_recipe({"Butter": 1}, 3, 5) == {"butter": 1.75}
print("All tests passed!")
