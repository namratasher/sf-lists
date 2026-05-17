"""Builds favicon.png (64x64) and apple-touch-icon.png (180x180)."""
from PIL import Image, ImageDraw, ImageFont

ACCENT = (210, 74, 42)
BG = (235, 235, 229)
WHITE = (255, 255, 255)

def make(size, out):
    img = Image.new("RGB", (size, size), ACCENT)
    d = ImageDraw.Draw(img)
    font_size = int(size * 0.5)
    font = ImageFont.truetype("/usr/share/fonts/opentype/urw-base35/P052-Bold.otf", font_size)
    text = "SF"
    bbox = d.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (size - tw) // 2 - bbox[0]
    y = (size - th) // 2 - bbox[1] - size // 22
    d.text((x, y), text, font=font, fill=WHITE)
    img.save(out, "PNG", optimize=True)
    print("Wrote", out, img.size)

make(64,  "/sessions/laughing-sweet-knuth/mnt/outputs/favicon.png")
make(180, "/sessions/laughing-sweet-knuth/mnt/outputs/apple-touch-icon.png")
