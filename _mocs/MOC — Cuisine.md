# MOC — Cuisine

Browse recipes by cuisine — Italian, Japanese, Mexican, French, American, and more.

---

## ⭐ Featured

- [[hummus]] — *Restaurant-scale Middle Eastern chickpea dip*
- [[cannoli]] — *From-scratch Sicilian pastry with fresh ricotta*
- [[yakiniku-salt-slab]] — *Japanese Wagyu cooked on a salt slab*
- [[foie-gras]] — *French fine-dining foie gras course*
- [[old-fashioned]] — *Classic American whiskey cocktail*
- [[dolma]] — *Lebanese stuffed grape leaves, family recipe*

---

## All Recipes

```dataview
TABLE cuisine, meal_type, total_time
FROM "recipes"
WHERE status != "archived"
SORT cuisine ASC, title ASC
```