"""
Auto-generate text captions for training images based on folder structure.
Each image gets a .txt file with the same name containing the training caption.

Run this AFTER organizing images into:
data/curated/{archetype}/{emotion}/*.png
"""

import os
import yaml
from pathlib import Path

# Load archetype and emotion definitions
def load_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

archetypes = load_yaml('prompts/archetypes.yaml')
emotions = load_yaml('prompts/emotions.yaml')

# Base template
TEMPLATE = "{archetype}, {emotion}, anime style, clean line art, emotionally unified face, balanced eyes mouth and eyebrows, no exaggerated expression"

print(f"Loaded {len(archetypes)} archetypes: {list(archetypes.keys())}")
print(f"Loaded {len(emotions)} emotions: {list(emotions.keys())}")
print()

# Process all images
curated_dir = Path('data/curated')
total_captions = 0
total_images = 0
stats = {}

print("Scanning for images...")
print()

for archetype_name in archetypes.keys():
    archetype_path = curated_dir / archetype_name
    
    if not archetype_path.exists():
        print(f"⚠ Warning: {archetype_name} folder not found - skipping")
        continue
    
    stats[archetype_name] = {}
    
    for emotion_name in emotions.keys():
        emotion_path = archetype_path / emotion_name
        
        if not emotion_path.exists():
            print(f"⚠ Warning: {archetype_name}/{emotion_name} folder not found - skipping")
            continue
        
        # Find all images in this folder
        image_files = []
        for ext in ['*.png', '*.jpg', '*.jpeg', '*.webp']:
            image_files.extend(emotion_path.glob(ext))
        
        count = 0
        for img_path in image_files:
            total_images += 1
            
            # Check if caption already exists
            txt_path = img_path.with_suffix('.txt')
            if txt_path.exists():
                # Skip if already captioned
                count += 1
                total_captions += 1
                continue
            
            # Generate caption
            caption = TEMPLATE.format(
                archetype=archetypes[archetype_name]['description'],
                emotion=emotions[emotion_name]
            )
            
            # Write to .txt file with same name
            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(caption)
            
            count += 1
            total_captions += 1
        
        stats[archetype_name][emotion_name] = count
        if count > 0:
            print(f"✓ {archetype_name}/{emotion_name}: {count} captions")

print(f"\n{'='*60}")
print(f"Total images found: {total_images}")
print(f"Total captions generated: {total_captions}")
print(f"{'='*60}\n")

# Print distribution
print("Distribution by archetype:")
for arch, emotions_dict in stats.items():
    total = sum(emotions_dict.values())
    print(f"  {arch}: {total}")
    for emo, count in emotions_dict.items():
        print(f"    - {emo}: {count}")

print(f"\nNext step: Review captions in data/curated/ folders")
print(f"Then proceed to LoRA training setup!")