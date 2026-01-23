# Baseline Evaluation - January 22, 2026

**Model:** stable-diffusion-v1-5 (base, no fine-tuning)  
**Total Images:** 48 (4 archetypes × 4 emotions × 3 CFG values)  
**Evaluator:** Elijah

---

## Quick Summary Stats

After full evaluation, fill this in:

| Metric | Count | Percentage |
|--------|-------|------------|
| Perfect Harmony (⭐⭐⭐) | 8 | 16.7% |
| Acceptable (⭐⭐) | 21 | 43.8% |
| Broken (⭐) | 19 | 39.6% |

**Top 3 Failure Patterns:**
1. Soft + Angry = Complete Failure (100% broken)
All 3 CFG values failed. The model cannot reconcile "soft/gentle" archetype with "angry" emotion.
2. Energetic + Happy/Sad/Angry = Major Struggles (83% broken)
Only neutral works for energetic. The model defaults to "shy/confused" instead of expressive.
3. Melancholic + Happy/Angry = Contradiction (83% broken)
Model struggles with melancholic characters showing positive/aggressive emotions.

**CFG Sensitivity:** Does harmony break at specific guidance scales?
- CFG 5.0: 
Pros: Less distortion, cleaner shapes
Cons: Emotions too subtle, features undefined
Best for: Neutral emotions, melancholic archetype
Worst for: Anger (needs more definition)
- CFG 7.0: 
Pros: Balanced clarity and coherence
Cons: Some teeth/distortion artifacts
Best for: Most archetype × emotion combos
Recommendation: This will be used as baseline for CFG
- CFG 9.0: 
Pros: Strong emotional definition
Cons: Frequent distortion, competing signals
Best for: Soft × neutral, melancholic × happy (rare wins)
Worst for: Energetic archetype (creates shock/confusion)

---

## Detailed Reviews by Archetype

### SOFT Archetype

#### soft__neutral__cfg5.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐⭐⭐
- **Holistic:** ⭐⭐
- **Notes:** Mouth is a bit curved, face displays subtle signs of sadness


#### soft__neutral__cfg7.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐⭐
- **Holistic:** ⭐⭐
- **Notes:** facial expression is a bit flat

#### soft__neutral__cfg9.0.png
- **Eyes ↔ Mouth:** ⭐⭐⭐
- **Brows ↔ Tension:** ⭐⭐⭐
- **Holistic:** ⭐⭐⭐
- **Notes:** perfection, unified harmony of facial expression

#### soft__happy__cfg5.0.png
- **Eyes ↔ Mouth:** ⭐
- **Brows ↔ Tension:** ⭐
- **Holistic:** ⭐⭐
- **Notes:** Face doesn't match specified emotion, mouth is missing

#### soft__happy__cfg7.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐⭐⭐
- **Holistic:** ⭐⭐⭐
- **Notes:** pupil is a bit distorted.

#### soft__happy__cfg9.0.png
- **Eyes ↔ Mouth:** ⭐⭐⭐
- **Brows ↔ Tension:** ⭐⭐⭐
- **Holistic:** ⭐
- **Notes:** face shows specified emotion but the shape is distorted

#### soft__sad__cfg5.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐⭐
- **Holistic:** ⭐⭐
- **Notes:** mouth doesn't match emotional intent

#### soft__sad__cfg7.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐⭐⭐
- **Holistic:** ⭐⭐
- **Notes:** there's a bit of visible eyebag, no competing emotional signals

#### soft__sad__cfg9.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐
- **Holistic:** ⭐
- **Notes:** mouth displays different emotion, face tells different emotional story

#### soft__angry__cfg5.0.png
- **Eyes ↔ Mouth:** ⭐
- **Brows ↔ Tension:** ⭐
- **Holistic:** ⭐
- **Notes:** Mouth doesn't display anger emotion, lower jaw of face is distorted

#### soft__angry__cfg7.0.png
- **Eyes ↔ Mouth:** ⭐ 
- **Brows ↔ Tension:** ⭐⭐
- **Holistic:** ⭐⭐
- **Notes:** Face shows no signs of anger, mouth is a straight line shape

#### soft__angry__cfg9.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐⭐
- **Holistic:** ⭐⭐
- **Notes:** Face is a bit too flat for anger emotion.

---

### STOIC Archetype

#### stoic__neutral__cfg5.0.png
- **Eyes ↔ Mouth:** ⭐⭐⭐
- **Brows ↔ Tension:** ⭐⭐⭐
- **Holistic:** ⭐⭐
- **Notes:** Face shows unified emotion

#### stoic__neutral__cfg7.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐⭐
- **Holistic:** ⭐⭐
- **Notes:** aside from the teeth, facial features seems balanced

#### stoic__neutral__cfg9.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐⭐
- **Holistic:** ⭐⭐
- **Notes:** mouth is slightly curved and hints shyness, size of eyes is okay

#### stoic__happy__cfg5.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐⭐
- **Holistic:** ⭐⭐
- **Notes:** mouth doesn't show clear happiness(okay for a stoic character), face shows a bit of competing emotional signals(shyness, sadness and blushing)

#### stoic__happy__cfg7.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐⭐⭐
- **Holistic:** ⭐⭐⭐
- **Notes:** eyes is a bit too wide for a stoic character

#### stoic__happy__cfg9.0.png
- **Eyes ↔ Mouth:** ⭐
- **Brows ↔ Tension:** ⭐⭐
- **Holistic:** ⭐
- **Notes:** mouth is curved downward and doesn't show specified emotion, eyes is a bit too wide

#### stoic__sad__cfg5.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐⭐⭐
- **Holistic:** ⭐⭐
- **Notes:** facial expression is a blur between anger and sadness

#### stoic__sad__cfg7.0.png
- **Eyes ↔ Mouth:** ⭐
- **Brows ↔ Tension:** ⭐
- **Holistic:** ⭐
- **Notes:** eyes is narrow, and a bit sad, not enough to evaluate

#### stoic__sad__cfg9.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐⭐⭐
- **Holistic:** ⭐⭐⭐
- **Notes:** face shows clear sadness, though the eye might be a bit too wide

#### stoic__angry__cfg5.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐⭐⭐
- **Holistic:** ⭐⭐
- **Notes:** distorted facial features(mouth and nose), emotion is quite visible

#### stoic__angry__cfg7.0.png
- **Eyes ↔ Mouth:** ⭐⭐⭐
- **Brows ↔ Tension:** ⭐⭐⭐
- **Holistic:** ⭐⭐
- **Notes:** Face shows emotional intent, jawline is a bit to angled

#### stoic__angry__cfg9.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐⭐
- **Holistic:** ⭐⭐
- **Notes:** eyes seems a bit too large, mouth shows sign of been upset, not clear anger

---

### ENERGETIC Archetype

#### energetic__neutral__cfg5.0.png
- **Eyes ↔ Mouth:** ⭐⭐⭐
- **Brows ↔ Tension:** ⭐⭐⭐
- **Holistic:** ⭐⭐⭐
- **Notes:** Eyes and mouth matches specified emotion, no contradictory tension, no competing signals

#### energetic__neutral__cfg7.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐⭐⭐
- **Holistic:** ⭐
- **Notes:** Eyes doesn't show neutral emotion but a somewhat worried expression

#### energetic__neutral__cfg9.0.png
- **Eyes ↔ Mouth:** ⭐
- **Brows ↔ Tension:** ⭐⭐
- **Holistic:** ⭐⭐
- **Notes:** Eyes a bit narrow for energetic character, mouth is slightly curved downward

#### energetic__happy__cfg5.0.png
- **Eyes ↔ Mouth:** ⭐
- **Brows ↔ Tension:**⭐ 
- **Holistic:** ⭐
- **Notes:** Mouth doesn't display emotions for an energetic character

#### energetic__happy__cfg7.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐⭐⭐
- **Holistic:** ⭐
- **Notes:** Lower part of face is distorted,face displays shyness rather than happiness

#### energetic__happy__cfg9.0.png
- **Eyes ↔ Mouth:** ⭐
- **Brows ↔ Tension:** ⭐
- **Holistic:** ⭐
- **Notes:** Eyes doesn't match emotion, Eyebrow doesn't support specified emotion

#### energetic__sad__cfg5.0.png
- **Eyes ↔ Mouth:** ⭐
- **Brows ↔ Tension:** ⭐
- **Holistic:** ⭐
- **Notes:** Close up view eyes, didn't show overall facial expression

#### energetic__sad__cfg7.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐
- **Holistic:** ⭐⭐
- **Notes:** Faces displays subtle sadness accross faces, drew more than one face

#### energetic__sad__cfg9.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐⭐
- **Holistic:** ⭐
- **Notes:** Face is twitching rather than displaying sadness

#### energetic__angry__cfg5.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐
- **Holistic:** ⭐
- **Notes:** Competing signals, facial features isn't coherent

#### energetic__angry__cfg7.0.png
- **Eyes ↔ Mouth:** ⭐
- **Brows ↔ Tension:** ⭐
- **Holistic:** ⭐
- **Notes:** Eyes seems okay, mouth doesn't match expression which gives it a different emotion

#### energetic__angry__cfg9.0.png
- **Eyes ↔ Mouth:** ⭐
- **Brows ↔ Tension:**⭐ 
- **Holistic:** ⭐
- **Notes:** mouth doesn't match emotion, face express more shock than anger

---

### MELANCHOLIC Archetype

#### melancholic__neutral__cfg5.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐⭐⭐
- **Holistic:** ⭐⭐
- **Notes:** No competing emotional signals, eyes matches intent of mouth

#### melancholic__neutral__cfg7.0.png
- **Eyes ↔ Mouth:** ⭐
- **Brows ↔ Tension:** ⭐
- **Holistic:** ⭐
- **Notes:** distorted face and facial features

#### melancholic__neutral__cfg9.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐⭐
- **Holistic:** ⭐⭐
- **Notes:** No competing emotonal signals, no exagerated facial features

#### melancholic__happy__cfg5.0.png
- **Eyes ↔ Mouth:** ⭐
- **Brows ↔ Tension:** ⭐
- **Holistic:** ⭐
- **Notes:** Face shows no sign of happiness

#### melancholic__happy__cfg7.0.png
- **Eyes ↔ Mouth:** ⭐
- **Brows ↔ Tension:** ⭐
- **Holistic:** ⭐
- **Notes:** Mouth is flat, eyebrow doesn't support specified emotion

#### melancholic__happy__cfg9.0.png
- **Eyes ↔ Mouth:** ⭐⭐⭐
- **Brows ↔ Tension:** ⭐⭐
- **Holistic:** ⭐⭐⭐
- **Notes:** Mouth is slightly curved upward, count's as happiness for a melencholic character

#### melancholic__sad__cfg5.0.png
- **Eyes ↔ Mouth:** ⭐⭐⭐
- **Brows ↔ Tension:** ⭐⭐⭐
- **Holistic:** ⭐⭐⭐
- **Notes:** perfection, eyes match emotional intent of mouth, no exagerated features, face reads unified emotion

#### melancholic__sad__cfg7.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐⭐
- **Holistic:** ⭐⭐
- **Notes:** mouth doesn't show sadness, competing emotional signals between sadness and neutral

#### melancholic__sad__cfg9.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐
- **Holistic:** ⭐
- **Notes:** distorted facial features, there's a bit of eyebag

#### melancholic__angry__cfg5.0.png
- **Eyes ↔ Mouth:** ⭐⭐
- **Brows ↔ Tension:** ⭐⭐⭐
- **Holistic:** ⭐⭐
- **Notes:** face almost shows a pouting expression rather than neutral 

#### melancholic__angry__cfg7.0.png
- **Eyes ↔ Mouth:** ⭐
- **Brows ↔ Tension:** ⭐
- **Holistic:** ⭐
- **Notes:** No mouth, visible eyebags that doesn't display anger

#### melancholic__angry__cfg9.0.png
- **Eyes ↔ Mouth:** ⭐
- **Brows ↔ Tension:** ⭐⭐
- **Holistic:** ⭐
- **Notes:** distorted eyes, no pupil, face is more neutral than angry, eyebrow doesn't display anger

---

## Pattern Analysis

### Type A Failures: Feature Isolation
List images where one feature doesn't match others:
- 
Definition: One facial feature tells a different emotional story
Examples:

soft__happy__cfg5.0 - Missing mouth entirely
soft__angry__cfg7.0 - Straight line mouth on intended angry face
stoic__happy__cfg9.0 - Downward curved mouth (sad) with happy prompt
energetic__happy__cfg7.0 - Shows shyness instead of happiness
energetic__angry__cfg7.0 - Mouth doesn't match eyes, creates different emotion
melancholic__happy__cfg5.0 - No signs of happiness despite prompt
melancholic__angry__cfg7.0 - Missing mouth entirely

Pattern: Mouths are the weakest link. Eyes often work, but mouths fail to express the emotion.
Count: ~15 images (31%)
- 

### Type B Failures: Intensity Mismatch
List images where emotion intensity is wrong:
- 
Definition: Emotion is correct but intensity is wrong
Examples:

soft__neutral__cfg7.0 - "Facial expression is a bit flat"
soft__angry__cfg9.0 - "Face is a bit too flat for anger emotion"
stoic__sad__cfg5.0 - "Blur between anger and sadness" (not distinct enough)
energetic__sad__cfg7.0 - "Displays subtle sadness" (too subtle for energetic)
melancholic__sad__cfg7.0 - "Competing signals between sadness and neutral" (not sad enough)

Pattern: "Soft" and "Melancholic" archetypes suppress emotional intensity. Anger consistently comes out too weak.
Count: ~8 images (17%)
- 

### Type C Failures: Emotional Drift
List images where emotion differs from prompt:
- 
Definition: Model generates a different emotion than prompted
Examples:

soft__neutral__cfg5.0 - "Displays subtle signs of sadness" (not neutral)
soft__sad__cfg9.0 - "Mouth displays different emotion"
stoic__happy__cfg5.0 - "Competing signals (shyness, sadness, blushing)" instead of clear happy
energetic__neutral__cfg7.0 - "Shows worried expression" (not neutral)
energetic__neutral__cfg9.0 - "Mouth curved downward" (reads as sad/concerned)
energetic__sad__cfg9.0 - "Twitching rather than sadness"
energetic__angry__cfg9.0 - "Express more shock than anger"
melancholic__angry__cfg5.0 - "Pouting rather than neutral" (wrong emotion entirely)

Pattern: Model has a default emotional bias:

Soft → defaults to sadness
Energetic → defaults to surprise/worry
Melancholic → defaults to neutral/pouting

Count: ~12 images (25%)
- 

### Type D Failures: Style Override
List images where style overwhelms emotion:
- 
Definition: Visual style choices overwhelm emotional clarity
Examples:

soft__happy__cfg9.0 - "Shows emotion but shape is distorted"
stoic__neutral__cfg7.0 - "Teeth visible" (breaks neutral stoicism)
stoic__angry__cfg7.0 - "Jawline too angled" (style overpowers emotion)
energetic__sad__cfg5.0 - "Close-up view of eyes, didn't show overall expression"
energetic__sad__cfg7.0 - "Drew more than one face" (composition breaks emotion)
melancholic__neutral__cfg7.0 - "Distorted face and facial features"
melancholic__sad__cfg9.0 - "Distorted facial features, eyebags"
melancholic__angry__cfg9.0 - "Distorted eyes, no pupil"

Pattern: Higher CFG (9.0) increases distortion. Model prioritizes "anime aesthetic" over emotional coherence.
Count: ~8 images (17%)
- 

---

## Dataset Curation Priorities

Based on failures above, which archetype × emotion combos need the most training data?

**Priority 1 (Most Broken):**
- 
Soft × Angry (0/3 success)

Need: 40 images of gentle characters showing controlled anger
Look for: soft features + tense mouth/brows


Energetic × Happy (0/3 success)

Need: 40 images of expressive characters with clear joy
Look for: wide eyes + big smiles that match


Energetic × Angry (0/3 success)

Need: 40 images of dynamic anger (not shock)
Look for: wide eyes + angry mouth/brows


Melancholic × Happy (1/3 success)

Need: 30 images of subtle happiness on sad-looking characters
Look for: droopy eyes + small genuine smiles


Melancholic × Angry (0/3 success)

Need: 30 images of melancholic characters showing restrained anger
Look for: sad eyes + tense mouth



Total Priority 1: 180 images
- 

**Priority 2 (Needs Improvement):**
- 
Soft × Sad (2/3 success, but weak)

Need: 20 images with clear eye-mouth sadness agreement


Soft × Happy (2/3 success, but distortion issues)

Need: 20 images with clean facial structure


Stoic × Sad (2/3 success, but ambiguous)

Need: 20 images with clear sadness despite restrained expression


Energetic × Sad (0/3 success)

Need: 25 images of expressive sadness (not subtle)



Total Priority 2: 85 images
- 

**Priority 3 (Minor Tweaks):**
- 
Neutral across all archetypes - Generally works, just needs refinement
Stoic × Neutral/Happy - Already decent, just polish

Total Priority 3: 35 images
- 

---

## CFG Analysis

Which CFG value produces best harmony overall?
** Verdict: CFG 7.0 is optimal for most cases. CFG 9.0 causes more harm than good. **
- 


---

Key Findings:

Neutral works best across all archetypes (61% success)
Anger is catastrophic (8% success rate overall)
Energetic archetype is broken (only neutral works)
Stoic is most stable (47% success)