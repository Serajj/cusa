import os
from PIL import Image

# ===== CONFIG =====
INPUT_DIR = "cusa18"     # source folder
OUTPUT_DIR = "cusa18_webp"     # destination folder
QUALITY = 80                   # WebP quality (0–100)
LOSSLESS = False               # True for lossless WebP
# ==================

SUPPORTED_EXTENSIONS = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(INPUT_DIR):
    if filename.lower().endswith(SUPPORTED_EXTENSIONS):
        input_path = os.path.join(INPUT_DIR, filename)
        output_name = os.path.splitext(filename)[0] + ".webp"
        output_path = os.path.join(OUTPUT_DIR, output_name)

        try:
            with Image.open(input_path) as img:
                img = img.convert("RGB")  # ensures compatibility
                img.save(
                    output_path,
                    "WEBP",
                    quality=QUALITY,
                    lossless=LOSSLESS,
                    method=6
                )
                print(f"✔ Converted: {filename} → {output_name}")

        except Exception as e:
            print(f"✖ Failed: {filename} | {e}")

print("\n🎉 All done!")
