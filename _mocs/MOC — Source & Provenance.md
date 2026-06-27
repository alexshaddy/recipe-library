# MOC — Source & Provenance

Browse recipes by where they came from — cookbooks, family heirlooms, professional kitchens, URLs, and more.

---

## ⭐ Featured

- [[rooz-m3-ful]] — *Family pronunciation preserved from the chef's notebook*
- [[hummus]] — *Restaurant-scale hummus formula*
- [[chiliburgers]] — *Vintage Carnation booklet, ground beef ideas*
- [[6-21-pop-up-dinner-menu]] — *Summer pop-up dinner, chef-developed menu*

---

## All Recipes

```dataview
TABLE source_type, source_name, origin_notes, date_added
FROM "recipes"
WHERE status != "archived"
SORT source_type ASC, date_added DESC
```