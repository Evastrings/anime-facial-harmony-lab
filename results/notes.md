Baseline Evaluation Report
Model: stable-diffusion-v1-5 (base, no fine-tuning)
Date: January 22, 2026
Evaluator: Elijah
Total Images: 48 (4 archetypes × 4 emotions × 3 CFG values)

📊 Executive Summary
MetricCountPercentagePerfect Harmony ⭐⭐⭐816.7%Acceptable ⭐⭐2143.8%Broken ⭐1939.6%
Key Findings

✅ Neutral works best across all archetypes (61% success rate)
⚠️ Energetic archetype is broken (only neutral works - 17% total success)
❌ Anger is catastrophic (8% success rate overall)
🎯 Stoic is most stable (47% success rate)


🔥 Top 3 Failure Patterns
1. Soft × Angry = Complete Failure (100% broken)
All 3 CFG values failed. The model cannot reconcile "soft/gentle" archetype with "angry" emotion.
2. Energetic × Happy/Sad/Angry = Major Struggles (83% broken)
Only neutral works for energetic characters. The model defaults to "shy/confused" instead of expressive.
3. Melancholic × Happy/Angry = Contradiction (83% broken)
Model struggles with melancholic characters showing positive or aggressive emotions.

⚙️ CFG Sensitivity Analysis
CFG 5.0 (Low Guidance)
AspectRatingProsLess distortion, cleaner shapesConsEmotions too subtle, features undefinedBest forNeutral emotions, melancholic archetypeWorst forAnger (needs more definition)
CFG 7.0 (Medium Guidance) ⭐ RECOMMENDED
AspectRatingProsBalanced clarity and coherenceConsSome teeth/distortion artifactsBest forMost archetype × emotion combosVerdictUse as baseline CFG
CFG 9.0 (High Guidance)
AspectRatingProsStrong emotional definitionConsFrequent distortion, competing signalsBest forSoft × neutral, melancholic × happy (rare wins)Worst forEnergetic archetype (creates shock/confusion)

Verdict: CFG 7.0 is optimal for most cases. CFG 9.0 causes more harm than good.


📈 Archetype × Emotion Success Matrix
ArchetypeNeutralHappySadAngryTotal SuccessSoft67%44%33%0%36%Stoic67%44%44%33%47% ⭐Energetic67%0%0%0%17% ⚠️Melancholic44%11%67%0%31%

🔍 Failure Pattern Analysis
Type A: Feature Isolation (31% of failures)
Definition: One facial feature tells a different emotional story.
Pattern: Mouths are the weakest link. Eyes often work, but mouths fail to express the emotion.
Examples:

soft__happy__cfg5.0 - Missing mouth entirely
soft__angry__cfg7.0 - Straight line mouth on intended angry face
stoic__happy__cfg9.0 - Downward curved mouth (sad) with happy prompt
energetic__happy__cfg7.0 - Shows shyness instead of happiness
energetic__angry__cfg7.0 - Mouth doesn't match eyes
melancholic__happy__cfg5.0 - No signs of happiness despite prompt
melancholic__angry__cfg7.0 - Missing mouth entirely

Count: ~15 images

Type B: Intensity Mismatch (17% of failures)
Definition: Emotion is correct but intensity is wrong.
Pattern: "Soft" and "Melancholic" archetypes suppress emotional intensity. Anger consistently comes out too weak.
Examples:

soft__neutral__cfg7.0 - Facial expression too flat
soft__angry__cfg9.0 - Face too flat for anger emotion
stoic__sad__cfg5.0 - Blur between anger and sadness (not distinct enough)
energetic__sad__cfg7.0 - Displays subtle sadness (too subtle for energetic)
melancholic__sad__cfg7.0 - Competing signals between sadness and neutral

Count: ~8 images

Type C: Emotional Drift (25% of failures)
Definition: Model generates a different emotion than prompted.
Pattern: Model has default emotional biases:

Soft → defaults to sadness
Energetic → defaults to surprise/worry
Melancholic → defaults to neutral/pouting

Examples:

soft__neutral__cfg5.0 - Displays subtle signs of sadness (not neutral)
stoic__happy__cfg5.0 - Competing signals (shyness, sadness, blushing)
energetic__neutral__cfg7.0 - Shows worried expression (not neutral)
energetic__angry__cfg9.0 - Express shock instead of anger
melancholic__angry__cfg5.0 - Pouting rather than angry

Count: ~12 images

Type D: Style Override (17% of failures)
Definition: Visual style choices overwhelm emotional clarity.
Pattern: Higher CFG (9.0) increases distortion. Model prioritizes "anime aesthetic" over emotional coherence.
Examples:

soft__happy__cfg9.0 - Shows emotion but shape is distorted
stoic__neutral__cfg7.0 - Teeth visible (breaks neutral stoicism)
stoic__angry__cfg7.0 - Jawline too angled (style overpowers emotion)
energetic__sad__cfg5.0 - Close-up view, didn't show overall expression
energetic__sad__cfg7.0 - Drew more than one face
melancholic__neutral__cfg7.0 - Distorted face and facial features
melancholic__angry__cfg9.0 - Distorted eyes, no pupil

Count: ~8 images

🎯 Dataset Curation Strategy
Priority 1: Critical Failures (60% of effort)
Total Target: 180 images
ComboSuccess RateImages NeededFocusSoft × Angry0/3 (0%)40Gentle characters showing controlled angerEnergetic × Happy0/3 (0%)40Expressive characters with clear joyEnergetic × Angry0/3 (0%)40Dynamic anger (not shock)Melancholic × Happy1/3 (33%)30Subtle happiness on sad-looking charactersMelancholic × Angry0/3 (0%)30Restrained anger with sad eyes

Priority 2: Needs Improvement (30% of effort)
Total Target: 85 images
ComboSuccess RateImages NeededFocusSoft × Sad2/3 (67%)20Clear eye-mouth sadness agreementSoft × Happy2/3 (67%)20Clean facial structure, no distortionStoic × Sad2/3 (67%)20Clear sadness despite restrained expressionEnergetic × Sad0/3 (0%)25Expressive sadness (not subtle)

Priority 3: Minor Tweaks (10% of effort)
Total Target: 35 images

Neutral across all archetypes (generally works, needs refinement)
Stoic × Neutral/Happy (already decent, polish only)


📝 Detailed Image Reviews
<details>
<summary><b>SOFT Archetype (Click to expand)</b></summary>
Neutral

cfg5.0: ⭐⭐ - Mouth curved, shows subtle sadness
cfg7.0: ⭐⭐ - Expression too flat
cfg9.0: ⭐⭐⭐ - Perfect unified harmony ✅

Happy

cfg5.0: ⭐ - Missing mouth, doesn't match emotion
cfg7.0: ⭐⭐⭐ - Slight pupil distortion
cfg9.0: ⭐ - Emotion present but face distorted

Sad

cfg5.0: ⭐⭐ - Mouth doesn't match emotional intent
cfg7.0: ⭐⭐ - Visible eyebag, no competing signals
cfg9.0: ⭐ - Mouth displays different emotion

Angry

cfg5.0: ⭐ - No anger, distorted lower jaw
cfg7.0: ⭐⭐ - No anger signs, straight line mouth
cfg9.0: ⭐⭐ - Too flat for anger

</details>
<details>
<summary><b>STOIC Archetype (Click to expand)</b></summary>
Neutral

cfg5.0: ⭐⭐ - Unified emotion, good
cfg7.0: ⭐⭐ - Teeth visible, otherwise balanced
cfg9.0: ⭐⭐ - Slight shyness hint, eyes okay

Happy

cfg5.0: ⭐⭐ - Competing signals (shyness, sadness, blushing)
cfg7.0: ⭐⭐⭐ - Eyes too wide for stoic ✅
cfg9.0: ⭐ - Downward curved mouth, eyes too wide

Sad

cfg5.0: ⭐⭐ - Blur between anger and sadness
cfg7.0: ⭐ - Narrow sad eyes, insufficient detail
cfg9.0: ⭐⭐⭐ - Clear sadness, slight eye width issue ✅

Angry

cfg5.0: ⭐⭐ - Distorted features, emotion visible
cfg7.0: ⭐⭐ - Shows intent, angled jawline
cfg9.0: ⭐⭐ - Eyes too large, upset not angry

</details>
<details>
<summary><b>ENERGETIC Archetype (Click to expand)</b></summary>
Neutral

cfg5.0: ⭐⭐⭐ - Perfect match, no competing signals ✅
cfg7.0: ⭐ - Shows worried expression
cfg9.0: ⭐⭐ - Eyes narrow, mouth curved downward

Happy

cfg5.0: ⭐ - Mouth doesn't display emotion
cfg7.0: ⭐ - Distorted lower face, shows shyness
cfg9.0: ⭐ - Eyes and brows don't match

Sad

cfg5.0: ⭐ - Close-up view, no overall expression
cfg7.0: ⭐⭐ - Subtle sadness, drew multiple faces
cfg9.0: ⭐ - Face twitching, not sadness

Angry

cfg5.0: ⭐ - Competing signals, incoherent features
cfg7.0: ⭐ - Mouth doesn't match, wrong emotion
cfg9.0: ⭐ - Shows shock instead of anger

</details>
<details>
<summary><b>MELANCHOLIC Archetype (Click to expand)</b></summary>
Neutral

cfg5.0: ⭐⭐ - Eyes match mouth, no competing signals
cfg7.0: ⭐ - Distorted face and features
cfg9.0: ⭐⭐ - No competing signals, no exaggeration

Happy

cfg5.0: ⭐ - No signs of happiness
cfg7.0: ⭐ - Flat mouth, brows don't support
cfg9.0: ⭐⭐⭐ - Slight upward curve, works for melancholic ✅

Sad

cfg5.0: ⭐⭐⭐ - Perfect harmony, unified emotion ✅
cfg7.0: ⭐⭐ - Mouth doesn't show sadness
cfg9.0: ⭐ - Distorted features, visible eyebag

Angry

cfg5.0: ⭐⭐ - Pouting expression, not angry
cfg7.0: ⭐ - No mouth, visible eyebags
cfg9.0: ⭐ - Distorted eyes, no pupil, neutral not angry

</details>
