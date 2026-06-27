# Changelog

All notable changes to the Recipe Library are documented in this file.

## 2026-06-27 — Tier 1 Source Mismatch Fixes & Title-Only Reconstructions

### Fixed

- **Ryu Confit Egg Yolk** (`recipes/condiment/ryu-confit-egg-yolk.md`) — Replaced 2-step stub (just "1 egg yolk" + "salt [TO VERIFY]") with complete recipe from notebook source. Ingredients now include egg yolks, neutral oil, sesame oil, gochugaru, chili flakes. Full 6-step confit method at 160°F/71°C for ~55 minutes with sensory cues, temperature tolerance guidance, two variations (soy-cured, garlic-infused), make-ahead/storage, and scaling (TICKET-003).

### Added

- **Miso Butter** (`recipes/condiment/miso-butter.md`) — Savory compound butter with white miso, mirin, honey, optional scallions and sesame seeds. Created from title-only addendum (TICKET-005 / TICKET-016). 7-step method with whipping, shaping, and chilling guidance.
- **Miso-Glazed Eggplant** (`recipes/dinner/miso-glazed-eggplant.md`) — Nasu dengaku-style eggplant with 3:2:1 miso:mirin:sake glaze. Created from title-only addendum (TICKET-008). 7-step method with scoring, broiling, and glaze-caramelization technique.
- **Miso Butterfish** (`recipes/dinner/miso-butterfish.md`) — Nobu-style saikyo-yaki with sablefish/black cod. Created from title-only addendum (TICKET-012). 8-step method covering 2–3 day marinade, broiling, and optional pan-sear.

### Fixed

- **Ricotta** (`recipes/condiment/ricotta.md`) — Replaced incorrect ingredient amounts (1 gal milk + 1 cup cream + ¼ cup acid) with notebook-accurate data (½ gal milk + ½ cup lemon juice + 1 tsp salt). Expanded from 3-step stub to 7 steps with sensory cues, timing, curd-watching guidance (TICKET-001).

### Infrastructure

- Added test suite at `tests/test_ticket_005_miso_butter.py` validating Miso Butter recipe structure and content.

### Structural

- **5.13 Kat Dinner** (`recipes/dinner/5-13-kat-dinner.md`) — Archived menu stub; added `occasion/menu-planning` tag, component descriptions, and chimichurri cross-reference (TICKET-039).
- **6.21 Pop-Up Dinner Menu** (`recipes/dinner/6-21-pop-up-dinner-menu.md`) — Archived menu stub; added `occasion/menu-planning` tag, course descriptions with numbering (TICKET-039).
- **Legro-th Meal Prep** (`recipes/lunch/legro-th-meal-prep.md`) — Expanded from meal-prep sketch into 3 complete mini-recipes (Bacon Fried Rice, Pasta Sauce, Sautéed Mushrooms and Vegetables) with specific amounts, full methods, and batch assembly guidance (TICKET-039).
