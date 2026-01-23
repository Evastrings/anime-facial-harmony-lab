# Dataset Strategy

## Curation Principles

### What We're Looking For
High-quality anime faces where:
1. **Emotional intent is clear** - You can name the emotion without context
2. **Features agree** - Eyes, mouth, and brows tell the same story
3. **Subtle expressions exist** - Not everything is theatrical
4. **Style is clean** - Clear line art, minimal visual noise

### What We're Avoiding
- Meme faces / chibi / extreme stylization
- Ambiguous or mixed emotions
- Heavy post-processing / filters
- NSFW content
- Copyrighted characters (unless transformative)

---

## Sources to Consider

### Tier 1: High-Quality Expression Sheets
- ArtStation character design portfolios
- Pixiv (filtered, curated)
- Official anime production materials (if licensed)
- Expression reference packs

### Tier 2: Fanart (Carefully Curated)
- High-quality fanart with clear emotional intent
- Must have clean style consistency
- Verify artist permissions if possible

### Tier 3: Synthetic (Last Resort)
- High-quality generations from other models
- Only if natural data is insufficient
- Must still meet harmony criteria

---

## Annotation Schema

For each image in `curated/`, track:

```csv
filename,archetype,emotion,harmony_score,notes
img_001.png,soft,neutral,3,"perfect eye-mouth agreement"
img_002.png,stoic,sad,2,"brows slightly too active"
```

**Harmony Score:**
- 3 = Perfect (all features agree)
- 2 = Good (minor issues)
- 1 = Usable (has issues but teachable)
- 0 = Reject (contradictory features)

**Only score 2+ goes into training.**

---

## Balance Requirements

Target distribution (adjust based on baseline results):

| Archetype    | Neutral | Happy | Sad | Angry | Total per Archetype |
|--------------|---------|-------|-----|-------|---------------------|
| Soft         | 25      | 25    | 25  | 25    | 100                 |
| Stoic        | 25      | 25    | 25  | 25    | 100                 |
| Energetic    | 25      | 25    | 25  | 25    | 100                 |
| Melancholic  | 25      | 25    | 25  | 25    | 100                 |
| **Total**    | **100** | **100**| **100**| **100**| **400**        |

**Minimum viable:** 50 images per archetype (200 total)
**Target:** 100 images per archetype (400 total)
**Ideal:** 150+ images per archetype (600+ total)

---

## Next Steps (After Baseline Evaluation)

1. **Identify weak spots** - Which archetype × emotion combos failed?
2. **Prioritize curation** - Focus on failure patterns first
3. **Collect & annotate** - Use the schema above
4. **Verify balance** - Check distribution before training
5. **Quality over quantity** - 100 perfect images > 1000 mediocre ones

---

## Dataset Hygiene

- [ ] No duplicates
- [ ] Consistent resolution (min 512×512)
- [ ] Clear face visibility
- [ ] Balanced emotion distribution
- [ ] Documented sources (for legal compliance)
- [ ] Regular backup