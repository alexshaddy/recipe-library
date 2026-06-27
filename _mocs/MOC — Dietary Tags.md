# MOC — Dietary Tags

Browse recipes by dietary needs and preferences — vegan, vegetarian, gluten-free, dairy-free, keto, paleo, and more.

---

## ⭐ Featured

- [[baba-ghanoush]] — *Smoky vegan eggplant dip*
- [[ricotta]] — *Handmade fresh vegetarian cheese*
- [[dolma]] — *Naturally gluten-free stuffed grape leaves*
- [[chimichurri-chicken-empanadas]] — *Dairy-free empanadas*
- [[cold-smoked-baklava]] — *Vegan smoked baklava, chef experiment*

---

## All Recipes

```dataview
TABLE dietary_tags, meal_type, cuisine
FROM "recipes"
WHERE status != "archived"
SORT title ASC
```