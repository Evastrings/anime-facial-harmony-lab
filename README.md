# Anime Facial Harmony Lab

**Research project exploring emotional coordination in anime face generation through controlled fine-tuning.**

> **Status:** 🔄 Paused - Foundation model research phase  
> **Next:** Testing anime-native base models (Anything V3, AnimagineXL)

---

## Problem Statement

Base Stable Diffusion models struggle with **emotionally coherent anime facial expressions**. Generated faces often have:
- Eyes showing one emotion, mouth showing another
- Inconsistent eyebrow tension
- Mixed or contradictory emotional signals

**Example:** A "happy" prompt might generate smiling lips with confused eyes and neutral brows.

---

## Approach

### Phase 1: Baseline Evaluation ✅

Generated 48 test images across:
- **4 archetypes:** Soft, Stoic, Energetic, Melancholic
- **4 emotions:** Neutral, Happy, Sad, Angry
- **3 CFG scales:** 5.0, 7.0, 9.0

**Results:**
- **16.7%** perfect harmony (8/48 images)
- **43.8%** acceptable (21/48 images)
- **39.6%** broken (19/48 images)

**Key Findings:**
- Neutral emotion works best (61% success)
- Anger is catastrophic (8% success rate)
- Energetic archetype collapses (17% total success)
- Stoic is most stable (47% success)

[Full evaluation report](results/notes.md)

---

### Phase 2: Dataset Curation ✅

Collected **417 training images** targeting failure patterns:

| Archetype | Count | Priority |
|-----------|-------|----------|
| Stoic | 162 | Baseline stability |
| Energetic | 107 | Fix happy/angry/sad |
| Melancholic | 84 | Fix happy/angry |
| Soft | 64 | Fix angry |

**Distribution per emotion:**
- Neutral: ~30%
- Happy: ~25%
- Sad: ~25%
- Angry: ~20%

**Curation criteria:**
- Clear emotional intent
- Eyes-mouth-brows agreement
- Clean anime style (512×512+)
- SFW content only

---

### Phase 3: LoRA Fine-Tuning Experiments ⚠️

#### Attempt 1: Conservative LoRA
**Config:**
- Base: Stable Diffusion v1.5
- LoRA Rank: 16
- Epochs: 12
- Learning Rate: 5e-5

**Results:**
- Final Loss: **0.154** (very high)
- Model barely learned
- Missing features, distorted faces

**Diagnosis:** LoRA too weak to override base model biases.

---

#### Attempt 2: Aggressive LoRA
**Config:**
- Base: Stable Diffusion v1.5
- LoRA Rank: 64 (4x increase)
- Epochs: 30
- Learning Rate: 2e-4 (4x increase)

**Results:**
- Final Loss: **0.028** (good convergence)
- Partial improvement in some archetypes
- Still significant issues:
  - Multiple random images/collages
  - Missing facial features (no mouth/eyes)
  - Wrong emotions (neutral instead of angry)
  - Blurry/undefined features

**Example failures:**
- `soft_angry`: Still generates neutral faces
- `energetic_happy`: Multiple collaged images
- `melancholic_happy`: Vertical mouth artifacts

---

## Core Issue: Foundation Model Limitations

**Root Cause:** Stable Diffusion v1.5 was trained on:
- Realistic Western faces
- Generic anime (not expression-focused)
- Stock photography

**It lacks foundational understanding of anime facial coordination.**

LoRA fine-tuning attempts to teach something the base model has **zero architectural basis** for understanding.

**Analogy:** Teaching calculus to someone who doesn't know basic arithmetic.

---

## Next Phase: Foundation Model Switch

### Hypothesis
Anime-native base models already understand facial anatomy. LoRA would only need to **refine** emotions, not teach from scratch.

### Candidate Models

| Model | Strengths | Use Case |
|-------|-----------|----------|
| **Anything V3/V5** | Best anime quality, stable | Primary candidate |
| **AnimagineXL** | Strong emotion rendering | Test alternative |
| **CounterfeitXL** | Excellent facial control | Backup option |

### Planned Tests

1. **Zero-shot baseline** (no fine-tuning)
   - Generate same 48 test prompts
   - Compare harmony scores vs SD 1.5
   
2. **Prompt engineering** (no training)
   - Test improved prompt formats
   - Add negative prompts for artifacts
   
3. **Light LoRA** (if needed)
   - Lower rank (16-32)
   - Fewer epochs (10-15)
   - Moderate LR

4. **ControlNet** (complex option)
   - Reference image guidance
   - Highest quality, most complex

---

## Repository Structure

```
anime-facial-harmony-lab/
├── prompts/
│   ├── archetypes.yaml          # Character archetype definitions
│   ├── emotions.yaml             # Emotion descriptions
│   └── templates.txt             # Prompt templates
│
├── data/
│   ├── curated/                  # Training images (not in git)
│   ├── generate_captions.py      # Caption generation script
│   ├── generate_improved_captions.py
│   └── README.md                 # Dataset documentation
│
├── generation/
│   ├── generate_baseline.py      # Baseline image generation
│   └── config.yaml
│
├── evaluation/
│   └── visualize_grids.py        # Grid comparison tool
│
├── finetuning/
│   ├── lora_training_v1.ipynb    # Conservative LoRA (failed)
│   ├── lora_training_v2.ipynb    # Aggressive LoRA (partial)
│   └── lora_config.yaml
│
├── experiments/
│   ├── baseline/                 # SD 1.5 baseline (48 images)
│   ├── lora_v1/                  # LoRA v1 results
│   └── lora_v2/                  # LoRA v2 results
│
├── results/
│   ├── notes.md                  # Full evaluation report
│   └── grids/                    # Comparison grids
│
└── README.md                     # This file
```

---

## Key Learnings

### 1. Systematic Evaluation is Critical
The 3-point harmony checklist (eyes↔mouth, brows↔tension, holistic coherence) provided clear, reproducible failure diagnosis.

### 2. Foundation Model Selection > Fine-Tuning Technique
No amount of LoRA optimization can compensate for fundamental architectural limitations.

### 3. Loss Convergence ≠ Quality
LoRA v2 achieved low loss (0.028) but still produced poor results. The model learned the training distribution but couldn't generalize to coherent facial expressions.

### 4. Data Curation Strategy Matters
Focusing on Priority 1 failures (0% baseline success) was correct, but requires a foundation model capable of learning the task.

### 5. Multiple Image Artifacts = Training Data Issue
Collage/multi-face outputs indicate training data contamination with expression sheets or the base model's poor anime understanding.

---

## Technologies Used

- **Stable Diffusion v1.5** (base model)
- **Diffusers** (Hugging Face library)
- **PEFT/LoRA** (parameter-efficient fine-tuning)
- **Google Colab** (GPU acceleration - T4)
- **Python** (PyTorch, PIL, YAML)

---

## Running the Code

### Requirements
```bash
pip install diffusers transformers accelerate peft torch torchvision
```

### Generate Baseline
```bash
python generation/generate_baseline.py
```

### Evaluate Results
```bash
python evaluation/visualize_grids.py
```

### Train LoRA (Google Colab)
1. Upload `data/curated.zip` to Colab
2. Run `finetuning/lora_training_v2.ipynb`
3. Download trained weights

---

## Future Work

- [ ] Test anime-native base models (Anything V3)
- [ ] Implement ControlNet-based generation
- [ ] Explore multi-modal conditioning (text + reference image)
- [ ] Investigate attention visualization for failure analysis
- [ ] Consider full model fine-tuning (Dreambooth) if LoRA insufficient
- [ ] Expand to more archetypes and emotions
- [ ] Automate harmony evaluation with vision models

---

## Research Context

This project explores challenges similar to those faced by:
- **Spellbrush** (niji·journey) - anime-specific diffusion
- **Midjourney** - artistic quality and consistency
- **Academic research** on controllable generation and facial expression synthesis

Key papers:
- "High-Resolution Image Synthesis with Latent Diffusion Models" (Stable Diffusion)
- "LoRA: Low-Rank Adaptation of Large Language Models" (PEFT technique)
- Anime-specific diffusion model papers (Anything, AnimagineXL)

---

## License & Attribution

**Research/Educational Use**

Training images sourced from Pinterest (fanart). If using this for commercial purposes, curate only permissive-licensed content.

Code and methodology: MIT License

---

## Contact

**Elijah** - [https://.linkedin.com/in/elijahakande]

Interested in controllable generation, anime AI, or artistic quality in diffusion models? Let's connect!

---

## Acknowledgments

- Hugging Face (Diffusers library)
- Stability AI (Stable Diffusion)
- Google Colab (free GPU access)
- Anime AI community (dataset inspiration)

---

*Last Updated: February 2026*

**Status: Paused pending foundation model evaluation**