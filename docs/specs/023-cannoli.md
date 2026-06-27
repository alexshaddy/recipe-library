# Specification: Expand Cannoli from Notebook Source

**Ticket:** TICKET-023  
**Recipe:** `dessert/cannoli.md`  
**Objective:** Align the cannoli recipe with the notebook source (p.24) for both shell and filling, and expand instructions, notes, and variations per digitization skill spec.

## Design

### 1. Ingredients
We need to align exactly with notebook for both shell and filling. The current shell amount is marked [ESTIMATED]; we must replace with exact count or weight from notebook. The filling ingredients also may need adjustment.

Since we don't have the notebook, we will instruct the implementer to read notebook p.24 and extract:
- Shell ingredients: likely flour, sugar, salt, butter, egg, vinegar or wine, maybe cocoa? Typical cannoli shell: flour, sugar, salt, butter, egg, Marsala wine or vinegar.
- Filling: ricotta, sugar, vanilla, chocolate chips or candied fruit (maybe exact amounts).

We will provide a template that the implementer can fill in after checking the notebook.

For the spec, we will outline the expected structure.

**Shell (makes about 12-15 shells):**
- 2 cups all-purpose flour
- 2 tablespoons granulated sugar
- 1/2 teaspoon salt
- 2 tablespoons unsalted butter, melted
- 1 egg
- 1/4 cup Marsala wine (or dry white wine or vinegar)
- Oil for frying (vegetable or canola)

**Filling:**
- 2 cups whole-milk ricotta, drained overnight in cheesecloth
- 1/2 cup granulated sugar
- 1 teaspoon vanilla extract
- 1/2 cup mini chocolate chips or chopped candied citrus
- Pinch of cinnamon (optional)

**For finishing:**
- Powdered sugar for dusting
- Chopped pistachios or cherries for dipping ends (optional)

### 2. Instructions
Expand to 8–10 steps covering both shell and filling, with bolded action titles, sensory cues, inline timing.

We'll break into two sections but present as sequential steps.

1. **Prepare the Shell Dough** – In a mixing bowl, combine 2 cups flour, 2 tbsp sugar, and 1/2 tsp salt. Cut in 2 tbsp melted butter until the mixture resembles coarse crumbs. Beat in 1 egg and 1/4 cup Marsala wine, stirring with a fork until a shaggy dough forms. Turn onto a lightly floured surface and knead for 1–2 minutes until smooth and elastic. The dough should feel firm but pliable, not sticky. Wrap in plastic and rest at room temperature for 30 minutes.
2. **Roll and Cut the Dough** – After resting, divide the dough into 4 portions. Working with one piece at a time (keep others covered), roll out on a floured surface to a thickness of about 1/16 inch (1.5 mm), almost transparent. You should be able to see the outline of your hand through it. Use a 4-inch round cutter to cut circles; gather scraps, re-roll, and cut more until you have about 12–15 circles.
3. **Wrap the Cannoli Tubes** – Wrap each dough circle tightly around a greased cannoli tube (metal or wood), overlapping the edges by about 1/2 inch. Seal the seam with a dab of beaten egg white or water. The shell should be snug but not stretched; you should see a slight gap at the ends.
4. **Heat the Oil** – Pour oil into a deep, heavy pot to a depth of 2 inches. Heat over medium-high until a deep-fry thermometer reads 350°F (175°C). A cube of bread should brown in about 15 seconds, and the oil should shimmer but not smoke.
5. **Fry the Shells** – Carefully slide 2–3 wrapped tubes into the hot oil, being careful not to splash. Fry for 2–3 minutes, turning occasionally with tongs, until the shells are golden brown and crisp, and the bubbles around them become smaller and slower. They should sound crisp when tapped.
6. **Drain and Cool** – Using tongs, remove the shells from the oil and let excess oil drip off for a few seconds, then place on a wire rack set over a baking sheet. While still warm, gently twist and remove the metal tubes; the shells should slide out easily. Let cool completely; they will crisp up further as they cool.
7. **Prepare the Filling** – While the shells cool, place 2 cups drained ricotta in a bowl. Add 1/2 cup sugar and 1 tsp vanilla. Using a hand mixer or whisk, beat until smooth and creamy, about 1–2 minutes. Fold in 1/2 cup chocolate chips or candied fruit. The mixture should be thick enough to hold its shape when scooped.
8. **Fill the Shells** – Just before serving, transfer the filling to a piping bag fitted with a large star tip. Hold each shell upright and pipe the filling from one end, then filling from both ends, meeting in the middle, until the shell is full but not overstuffed. The filling should be visible at the ends.
9. **Garnish and Serve** – Dip the filled ends in chopped pistachios, mini chocolate chips, or candied orange if desired. Dust lightly with powdered sugar. Serve immediately.
10. **Store Components Separately** – Keep unfilled shells in an airtight container at room temperature for up to 2 days. Keep filling refrigerated in an airtight container for up to 3 days. Do not fill ahead of time or the shells will soften.

### 3. Notes & Variations
- **Cook's Notes (2):**
  1. Rolling the dough paper-thin is essential for authentic, crisp cannoli shells; thicker shells taste doughy and absorb too much oil.
  2. Filling the shells just before serving prevents the moisture from the ricotta from softening the crisp fried shell.
- **Make-Ahead / Storage:**
  - Shells stay crisp in an airtight container at room temperature for 2 days; if they soften, re-crisp in a 350°F oven for 3–5 minutes.
  - Filling keeps refrigerated for 3 days; stir before use.
  - Assembled cannoli are best eaten within 2 hours of filling.
- **Scaling:**
  - The shell dough scales linearly; maintain the ratio of 4 cups flour to 1/2 cup liquid (egg + wine).
  - The filling scales linearly; keep the ratio of 4 parts ricotta to 1 part sugar.
- **Variations (1):**
  - **Chocolate-Dipped Cannoli:** After filling, dip one end of each cannoli in melted dark chocolate, then in chopped nuts, and let set on parchment.

### 4. Frontmatter & Metadata
- Update `prep_time`: "40 min [ACTIVE]" (includes dough resting)
- Update `cook_time`: "20 min [ACTIVE]" (frying)
- Keep `inactive_time`: "30 min [PASSIVE]" (draining/filling prep) – we can adjust.
- Update `total_time`: "1 hr 30 min"
- Set `date_modified`: "2026-06-27"
- Change `status` from "draft" to "reviewed"
- Ensure tags include `technique/dough`, `technique/fry`, `technique/pipe`.
- Verify existing fields (cuisine: italian, dietary_tags: vegetarian) remain accurate.
- `base_servings`: 12 cannoli (as before)
- `serving_unit`: "cannoli"
- `scaling_notes`: "Shells and filling scale separately; keep shells airtight and dry until filling."

### 5. Verification
- Confirm ingredient list matches notebook (exact amounts for shell and filling).
- Ensure instructions are 8–10 steps with bolded titles, sensory cues, timing.
- Confirm notes include at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- Validate frontmatter correctness.

## Implementation Notes
- No code changes; edit the existing markdown file.
- Implementer should open notebook p.24 to extract exact ingredient amounts and adjust the above template accordingly.
- Quality reviewer should verify against notebook source and spec.
- Documentation updater should ensure no related cross-references needed.

### Acceptance Criteria
- [ ] Ingredients list matches notebook (shell and filling exact amounts).
- [ ] Instructions are 8–10 steps with bolded action titles, sensory cues, inline timing.
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter fields updated as described.
- [ ] Status set to `reviewed`, date_modified set to 2026-06-27.
- [ ] No unrelated changes introduced.