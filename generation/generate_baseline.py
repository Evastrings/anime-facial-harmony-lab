import torch
import yaml
import os
from diffusers import StableDiffusionPipeline
from itertools import product
from PIL import Image
import sys

# -----------------------------
# Config
# -----------------------------
MODEL_ID = "runwayml/stable-diffusion-v1-5"
OUTPUT_DIR = "experiments/baseline"
CFG_VALUES = [5.0, 7.0, 9.0]
SEED = 42
NUM_STEPS = 30
IMAGE_SIZE = 512

# -----------------------------
# Device Detection
# -----------------------------
def get_device():
    """Automatically detect best available device"""
    if torch.cuda.is_available():
        print(f"✓ CUDA available: {torch.cuda.get_device_name(0)}")
        return "cuda"
    elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
        print("✓ MPS (Apple Silicon) available")
        return "mps"
    else:
        print("⚠ Using CPU (this will be slow)")
        return "cpu"

DEVICE = get_device()

# -----------------------------
# Load prompts with error handling
# -----------------------------
def load_yaml(path):
    """Load YAML with helpful error messages"""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"ERROR: {path} not found. Create it first!")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"ERROR: Invalid YAML in {path}: {e}")
        sys.exit(1)

try:
    archetypes = load_yaml("prompts/archetypes.yaml")
    emotions = load_yaml("prompts/emotions.yaml")
    with open("prompts/templates.txt", "r", encoding="utf-8") as f:
        TEMPLATE = f.read().strip()
except Exception as e:
    print(f"ERROR loading prompts: {e}")
    sys.exit(1)

# -----------------------------
# Prepare pipeline
# -----------------------------
print(f"\nLoading model: {MODEL_ID}")
print("This may take a few minutes on first run...")

try:
    pipe = StableDiffusionPipeline.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.float16 if DEVICE == "cuda" else torch.float32,
        safety_checker=None
    ).to(DEVICE)
    
    # Enable memory optimizations only for CUDA
    if DEVICE == "cuda":
        try:
            pipe.enable_xformers_memory_efficient_attention()
            print("✓ xFormers enabled")
        except Exception:
            print("⚠ xFormers not available, using default attention")
    
    print("✓ Model loaded successfully\n")
    
except Exception as e:
    print(f"ERROR loading model: {e}")
    print("\nTroubleshooting:")
    print("1. Check internet connection")
    print("2. Try: pip install --upgrade diffusers transformers")
    sys.exit(1)

# -----------------------------
# Generation loop
# -----------------------------
os.makedirs(OUTPUT_DIR, exist_ok=True)

total_images = len(archetypes) * len(emotions) * len(CFG_VALUES)
print(f"Generating {total_images} images...")
print(f"Output: {OUTPUT_DIR}\n")

generator = torch.Generator(device=DEVICE).manual_seed(SEED)
count = 0

for (arch_name, arch_data), (emo_name, emo_desc), cfg in product(
    archetypes.items(), emotions.items(), CFG_VALUES
):
    count += 1
    
    prompt = TEMPLATE.format(
        archetype=arch_data["description"],
        emotion=emo_desc
    )
    
    filename = f"{arch_name}__{emo_name}__cfg{cfg}.png"
    filepath = os.path.join(OUTPUT_DIR, filename)
    
    # Skip if already exists
    if os.path.exists(filepath):
        print(f"[{count}/{total_images}] {arch_name} × {emo_name} @ CFG={cfg}")
        print(f"  ⏭ Already exists: {filename}\n")
        continue
    
    print(f"[{count}/{total_images}] {arch_name} × {emo_name} @ CFG={cfg}")
    
    try:
        image = pipe(
            prompt=prompt,
            guidance_scale=cfg,
            num_inference_steps=NUM_STEPS,
            generator=generator,
            height=IMAGE_SIZE,
            width=IMAGE_SIZE
        ).images[0]
        
        image.save(filepath)
        print(f"  ✓ Saved: {filename}\n")
        
    except Exception as e:
        print(f"  ✗ FAILED: {e}\n")
        continue

print(f"\n{'='*50}")
print(f"Generation complete!")
print(f"Images saved to: {OUTPUT_DIR}")
print(f"Next step: Review harmony using evaluation/harmony_checklist.md")
print(f"{'='*50}")