# MOC — Meal Type

Browse recipes organized by meal type — breakfast, brunch, lunch, dinner, snacks, desserts, drinks, and more.

---

## ⭐ Featured

- [[buttermilk-biscuits]] — *Flaky, buttery biscuits from the chef's notebook*
- [[open-face-mushroom-sammie]] — *Quick lunch with sautéed mushrooms*
- [[chimichurri-chicken-empanadas]] — *Restaurant-adapted empanadas with chimichurri*
- [[labneh]] — *Lebanese labneh dip, part of the mezze spread*
- [[grilled-radicchio]] — *Charred radicchio, Sicilian simplicity*
- [[old-fashioned]] — *The essential whiskey cocktail*
- [[cannoli]] — *Handmade Sicilian cannoli with fresh ricotta*
- [[hummus]] — *Large-batch restaurant hummus*

---

## All Recipes

```dataview
TABLE meal_type, cuisine, total_time, difficulty
FROM "recipes"
WHERE status != "archived"
SORT meal_type ASC, title ASC
```