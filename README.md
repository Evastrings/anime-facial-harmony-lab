# Anime Facial Harmony Lab

Research project exploring emotional harmony in anime face generation through controlled fine-tuning.

## Problem
Base diffusion models struggle with unified facial expressions in anime art, particularly:
- Soft characters showing anger
- Energetic characters displaying subtle emotions
- Melancholic characters showing happiness

## Approach
1. Generate baseline images across 4 archetypes × 4 emotions
2. Evaluate facial harmony using 3-point checklist
3. Curate high-quality training data targeting failures
4. Fine-tune LoRA to teach emotional coordination
5. Measure improvement with before/after comparison

## Results
- Baseline: 16.7% perfect harmony
- Target: 50-60% perfect harmony after training

## Structure
```text
anime-facial-harmony-lab/
├── generation/      # Image generation scripts
├── evaluation/      # Harmony assessment tools
├── finetuning/      # LoRA training scripts
├── prompts/         # Structured prompt templates
├── data/            # Dataset and annotations
├── experiments/     # Generated images
└── results/         # Evaluation notes and analysis
```

## Status
🔄 Active - Currently in dataset curation phase

## Technologies
- Stable Diffusion v1.5
- Diffusers library
- LoRA fine-tuning
- Google Colab for GPU acceleration
