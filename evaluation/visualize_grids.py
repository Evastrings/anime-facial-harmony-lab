"""
Create comparison grids from generated images.
Makes it easier to spot harmony patterns across archetypes/emotions.
"""
import os
from PIL import Image, ImageDraw, ImageFont
import re

INPUT_DIR = "experiments/baseline"
OUTPUT_DIR = "results/grids"
GRID_SIZE = (512, 512)  # Size of each cell
MARGIN = 10
LABEL_HEIGHT = 40

def parse_filename(filename):
    """Extract archetype, emotion, cfg from filename"""
    # Format: archetype__emotion__cfgX.X.png
    match = re.match(r"(.+?)__(.+?)__cfg([0-9.]+)\.png", filename)
    if match:
        return {
            'archetype': match.group(1),
            'emotion': match.group(2),
            'cfg': float(match.group(3))
        }
    return None

def create_emotion_grid(archetype, cfg_value):
    """Create grid showing one archetype across all emotions at fixed CFG"""
    emotions = ['neutral', 'happy', 'sad', 'angry']
    
    # Grid: 2×2 (4 emotions)
    grid_w = 2 * GRID_SIZE[0] + 3 * MARGIN
    grid_h = 2 * GRID_SIZE[1] + 3 * MARGIN + LABEL_HEIGHT
    
    canvas = Image.new('RGB', (grid_w, grid_h), 'white')
    draw = ImageDraw.Draw(canvas)
    
    # Try to load a font, fallback to default
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()
    
    # Title
    title = f"{archetype.upper()} @ CFG={cfg_value}"
    draw.text((MARGIN, 10), title, fill='black', font=font)
    
    # Place images
    positions = [(0, 0), (1, 0), (0, 1), (1, 1)]
    
    for emotion, (col, row) in zip(emotions, positions):
        filename = f"{archetype}__{emotion}__cfg{cfg_value}.png"
        filepath = os.path.join(INPUT_DIR, filename)
        
        x = MARGIN + col * (GRID_SIZE[0] + MARGIN)
        y = LABEL_HEIGHT + MARGIN + row * (GRID_SIZE[1] + MARGIN)
        
        if os.path.exists(filepath):
            img = Image.open(filepath).resize(GRID_SIZE)
            canvas.paste(img, (x, y))
            
            # Label
            draw.text((x + 5, y + 5), emotion, fill='yellow', font=font)
        else:
            # Missing image placeholder
            draw.rectangle([x, y, x + GRID_SIZE[0], y + GRID_SIZE[1]], 
                          fill='gray', outline='red', width=3)
            draw.text((x + 10, y + 10), f"MISSING\n{emotion}", fill='white', font=font)
    
    return canvas

def create_cfg_comparison_grid(archetype, emotion):
    """Create grid showing one archetype+emotion across all CFG values"""
    cfg_values = [5.0, 7.0, 9.0]
    
    # Grid: 3×1 (3 CFG values)
    grid_w = 3 * GRID_SIZE[0] + 4 * MARGIN
    grid_h = GRID_SIZE[1] + 2 * MARGIN + LABEL_HEIGHT
    
    canvas = Image.new('RGB', (grid_w, grid_h), 'white')
    draw = ImageDraw.Draw(canvas)
    
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()
    
    # Title
    title = f"{archetype.upper()} - {emotion.upper()} (CFG Sweep)"
    draw.text((MARGIN, 10), title, fill='black', font=font)
    
    # Place images
    for idx, cfg in enumerate(cfg_values):
        filename = f"{archetype}__{emotion}__cfg{cfg}.png"
        filepath = os.path.join(INPUT_DIR, filename)
        
        x = MARGIN + idx * (GRID_SIZE[0] + MARGIN)
        y = LABEL_HEIGHT + MARGIN
        
        if os.path.exists(filepath):
            img = Image.open(filepath).resize(GRID_SIZE)
            canvas.paste(img, (x, y))
            
            # Label
            draw.text((x + 5, y + 5), f"CFG={cfg}", fill='yellow', font=font)
        else:
            draw.rectangle([x, y, x + GRID_SIZE[0], y + GRID_SIZE[1]], 
                          fill='gray', outline='red', width=3)
    
    return canvas

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    archetypes = ['soft', 'stoic', 'energetic', 'melancholic']
    emotions = ['neutral', 'happy', 'sad', 'angry']
    cfg_values = [5.0, 7.0, 9.0]
    
    print("Creating emotion comparison grids...")
    for archetype in archetypes:
        for cfg in cfg_values:
            grid = create_emotion_grid(archetype, cfg)
            output_path = os.path.join(OUTPUT_DIR, f"{archetype}_emotions_cfg{cfg}.png")
            grid.save(output_path)
            print(f"  ✓ Saved: {archetype}_emotions_cfg{cfg}.png")
    
    print("\nCreating CFG comparison grids...")
    for archetype in archetypes:
        for emotion in emotions:
            grid = create_cfg_comparison_grid(archetype, emotion)
            output_path = os.path.join(OUTPUT_DIR, f"{archetype}_{emotion}_cfg_sweep.png")
            grid.save(output_path)
            print(f"  ✓ Saved: {archetype}_{emotion}_cfg_sweep.png")
    
    print(f"\n{'='*50}")
    print(f"Grids saved to: {OUTPUT_DIR}")
    print(f"Total grids created: {len(archetypes) * len(cfg_values) + len(archetypes) * len(emotions)}")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()