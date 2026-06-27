# Specification: Expand Clarified Juices from Notebook Source (Two Methods)

**Ticket:** TICKET-018  
**Recipe:** `condiment/clarified-juices.md`  
**Objective:** Align the clarified juices recipe with the notebook source (two methods: acidic agar clarification, freeze-clarification) and expand instructions, notes, and variations per digitization skill spec.

## Design

### 1. Ingredients
We need to align with notebook source for both methods. Since the notebook likely provides a base juice and then clarification agents, we will define a generic clarified juice base and then the two methods.

**Base Juice (for both methods):**
- 1 liter (1000ml) fresh fruit or vegetable juice (e.g., orange, grapefruit, tomato, celery) – strained to remove pulp
- Optional: sweetener or acid to taste (to be adjusted after clarification)

**Method 1: Acidic Agar Clarification**
- 2 grams agar-agar powder
- 20ml lemon juice or citric acid solution (to acidify to pH ~4.0)
- Water for blooming agar (if needed)

**Method 2: Freeze-Thaw Clarification**
- No additional ingredients; relies on freezing and thawing

**Equipment:**
- Fine-mesh strainer
- Cheesecloth or coffee filter
- Saucepan
- Whisk
- Thermometer (optional)
- Freezer-safe container
- Bowl for thawing

### 2. Instructions
We need to cover both methods in 6–8 steps. We'll structure as: prepare base juice, then split into two method sections, or we can write sequential steps that cover both? Better to provide two separate sets of steps within the instructions, but the requirement is 6–8 steps total. We can do:

Steps 1-3: Prepare base juice (common)
Steps 4-6: Method 1 (agar)
Steps 7-8: Method 2 (freeze) – but that would be 8 steps.

Alternatively, we can write the instructions as a choose-your-own-adventure: after base juice, you choose method. We'll do:

1. **Prepare the Base Juice** – Extract juice from fresh fruit or vegetables using a juicer or blender and strain through a fine-mesh sieve to remove pulp. Measure 1 liter of clear juice. Taste and adjust sweetness or acidity if desired (note: adjustments may affect clarification).
2. **Method 1: Acidic Agar Clarification** – In a small saucepan, sprinkle 2 grams agar-agar over 2 tablespoons of cold water to bloom for 5 minutes. Add 20ml lemon juice (or citric acid solution) to the agar mixture. Heat over medium, stirring constantly, until the agar dissolves completely and the mixture reaches a boil (about 1-2 minutes). Boil for 30 seconds to fully activate agar.
3. **Combine and Set** – Pour the hot agar mixture into the 1 liter of juice while whisking vigorously to ensure even distribution. The mixture should be slightly thickened. Immediately pour into a shallow container and refrigerate for at least 2 hours, or until firmly set into a gel.
4. **Break and Strain** – Once set, break the gel into coarse chunks using a fork or whisk. Place a cheesecloth-lined strainer over a bowl and pour the broken gel into the cloth. Let drain slowly under gravity for 1-2 hours; do not squeeze, as this can cloud the liquid. The liquid that drips through is the clarified juice.
5. **Method 2: Freeze-Thaw Clarification** – Pour the 1 liter of base juice into a freezer-safe container, leaving some headspace for expansion. Freeze solid, preferably overnight or at least 6 hours.
6. **Thaw and Drain** – Remove the frozen juice block from the freezer and place it in a cheesecloth-lined strainer set over a bowl. Allow to thaw slowly in the refrigerator (or at room temperature if monitored) for 4-6 hours. As the ice melts, the liquid will drip through the cloth, leaving behind trapped solids and cloudiness. Collect the clarified liquid.
7. **Final Storage** – For both methods, transfer the clarified juice to a clean, sealed bottle. Refrigerate and use within 3-5 days. The juice should be crystal clear and have a concentrated flavor.

### 3. Notes & Variations
- **Cook's Notes (2):**
  1. Agar clarification works best with juices that are naturally acidic or have been acidified; low-acid juices may require more lemon juice to achieve proper gelation.
  2. Freeze-thaw clarification is gentler and preserves more delicate aromatics, but requires freezer space and time; it may yield slightly less volume due to ice retention.
- **Make-Ahead / Storage:**
  - Clarified juice keeps refrigerated in an airtight container for up to 5 days.
  - For longer storage, freeze the clarified juice (not the unclarified) for up to 2 months; thaw in refrigerator.
- **Scaling:**
  - Both methods scale linearly; maintain the ratio of 2g agar per liter of juice for method 1.
  - For method 1, ensure the agar is fully dissolved and boiled; for method 2, freezing time depends on container depth and freezer temperature.
- **Variations (1):**
  - **Herb-Infused Clarified Juice:** Add a handful of fresh herbs (e.g., basil, mint) to the base juice before clarification for method 1; remove herbs before agar step. For method 2, infuse after clarification.

### 4. Frontmatter & Metadata
- `title`: "Clarified Juices"
- `slug`: "clarified-juices"
- `meal_type`: condiment
- `cuisine`: international (technique-based)
- `course`: condiment
- `dietary_tags`: [vegetarian, vegan, gluten-free] (depends on juice source; we'll keep generic)
- `season`: all-year
- `prep_time`: "15 min [ACTIVE]" (juice extraction and prep)
- `cook_time`: "5 min [ACTIVE]" (for agar method; zero for freeze)
- `inactive_time`: "2 to 8 hr [PASSIVE]" (setting or freezing/thawing)
- `total_time`: "2 to 8 hr 20 min"
- `base_servings`: 1 liter
- `serving_unit`: "milliliter"
- `scaling_notes`: "Scale ingredients linearly; ensure adequate container size for setting or freezing."
- `source_type`: "handwritten" (from addendum)
- `source_name`: "Chef's Recipe Notebook"
- `source_url`: ""
- `source_page`: "" (unknown)
- `origin_notes`: "Created from title-only addendum; based on two clarification techniques from notebook."
- `difficulty`: "medium"
- `key_equipment`: ["juicer or blender", "fine-mesh sieve", "saucepan", "whisk", "cheesecloth", "container", "freezer"]
- `tags`: ["recipe/condiment", "technique/clarification", "technique/agar", "technique/freeze-thaw"]
- `protein`: [] (none)
- `status`: "reviewed"
- `date_added`: "2026-06-27"
- `date_modified`: "2026-06-27"

### 5. Verification
- Confirm recipe includes both clarification methods with appropriate ingredients.
- Ensure instructions cover both methods in 6–8 steps with bolded titles, sensory cues, timing.
- Confirm notes include at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- Validate frontmatter fields per ticket requirements.

### Implementation Notes
- No code changes; create new markdown file at `recipes/condiment/clarified-juices.md`.
- Implementer should create the file with the above content.
- Quality reviewer should verify against ticket requirements and spec.
- Documentation updater should ensure no related cross-references needed.

### Acceptance Criteria
- [ ] File created at correct path.
- [ ] Ingredients list includes base juice and clarification agents (agar, acid) for method 1.
- [ ] Instructions are 6–8 steps with bolded action titles, sensory cues, inline timing (covering both methods).
- [ ] Contains at least 2 cook's notes, 1 variation, make-ahead/storage, scaling guidance.
- [ ] Frontmatter matches specified fields and values.
- [ ] Status set to `reviewed`, date_modified set to 2026-06-27.
- [ ] No extraneous content.