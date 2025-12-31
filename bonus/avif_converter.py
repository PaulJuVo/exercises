from PIL import Image
import pillow_avif
import os
from pathlib import Path

# Ordner
input_dir = "input"
output_dir = "output"

# Zielgrößen (Breite x Höhe)
sizes = [
    (300, 225),
    (768, 577),
    (1024, 769),
    (1536, 1153),
    (2048, 1538),
]

os.makedirs(output_dir, exist_ok=True)

print('start script')
index = 1
for jpg_path in Path(input_dir).glob("*.JPG"):
    
    name = jpg_path.stem  # z.B. "6"

    img = Image.open(jpg_path).convert("RGB")

    # 1️⃣ Originalgröße
    img.save(
        f"{output_dir}/{index}.avif",
        format="AVIF",
        quality=50,
        speed=6
    )

    # 2️⃣ Skalierte Versionen
    for w, h in sizes:
        resized = img.resize((w, h), Image.Resampling.LANCZOS)
        resized.save(
            f"{output_dir}/{index}-{w}x{h}.avif",
            format="AVIF",
            quality=50,
            speed=6
        )

    print(f"{index}.jpg → fertig")
    index += 1

print("Alle Dateien verarbeitet ✔")
