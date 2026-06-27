# MOC — Occasion & Season

Browse recipes by occasion (weeknight, holiday, entertaining, meal-prep) and season (spring, summer, fall, winter).

---

## ⭐ Featured

- [[6-21-pop-up-dinner-menu]] — *Summer pop-up dinner, chef's tasting menu*
- [[savory-meat-loaf]] — *Quick weeknight dinner*
- [[never-a-lump-turkey-gravy]] — *Holiday essential, lump-free*
- [[kick-ass-cookies]] — *Classic comfort cookies*
- [[breezy-beach-collins]] — *Refreshing summer cocktail*
- [[never-grainy-carnation-pumpkin-pie]] — *Fall pumpkin pie, never grainy*

---

## All Recipes

```dataview
TABLE occasion, season, meal_type
FROM "recipes"
WHERE status != "archived"
SORT occasion ASC
```