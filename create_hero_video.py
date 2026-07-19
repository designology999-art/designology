from PIL import Image, ImageDraw, ImageFont
import imageio.v2 as imageio
import numpy as np
import os

out_path = 'assets/videos/hero-video.mp4'
os.makedirs(os.path.dirname(out_path), exist_ok=True)

W, H = 1280, 720
fps = 24
frames = []

# Load a font if available; fall back to default
font_path = None
for candidate in ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', '/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf']:
    if os.path.exists(candidate):
        font_path = candidate
        break

font = ImageFont.truetype(font_path, 42) if font_path else ImageFont.load_default()
small_font = ImageFont.truetype(font_path, 28) if font_path else ImageFont.load_default()

# Create a cinematic construction journey sequence with 20 scenes.
scenes = [
    ("Empty Plot", "A premium plot ready for a dream home", 0, 0.0),
    ("Surveying", "Precision land survey and architectural planning", 0.9, 0.0),
    ("Blueprint", "Detailed architectural plans and structural design", 1.8, 0.0),
    ("Excavation", "Clearing and excavation begin for the foundation", 2.7, 0.0),
    ("Foundation", "Strong foundation work and footing preparation", 3.6, 0.0),
    ("RCC Structure", "Columns, beams and core structure rise", 4.5, 0.0),
    ("Brick Walls", "Walls take shape with durable masonry", 5.4, 0.0),
    ("Roof Slab", "The roof slab is completed with precision", 6.3, 0.0),
    ("Exterior Finish", "Plaster, texture and facade detailing begin", 7.2, 0.0),
    ("Paint & Glass", "Luxury finishes and modern exterior glazing", 8.1, 0.0),
    ("Landscaping", "Gardens, pathways and outdoor elegance", 9.0, 0.0),
    ("Main Entrance", "Grand entry with bold architectural presence", 9.9, 0.0),
    ("Living Room", "A refined luxury living space takes shape", 10.8, 0.0),
    ("Kitchen", "Premium modular kitchen with elegant detailing", 11.7, 0.0),
    ("Master Bedroom", "A serene, statement master suite", 12.6, 0.0),
    ("Children Room", "Bright, contemporary family spaces", 13.5, 0.0),
    ("Guest Bedroom", "Comfortable hospitality-inspired guest quarters", 14.4, 0.0),
    ("Bathroom", "Spa-inspired luxury bathroom finishes", 15.3, 0.0),
    ("Study & Dining", "Home office, study and dining elegance", 16.2, 0.0),
    ("Final Home", "Completed dream home with terrace and drone view", 17.1, 0.0),
]

# Create frames for a 17.4-second loop.
for scene_idx, (title, subtitle, start_time, _) in enumerate(scenes):
    for frame_idx in range(int(fps * 0.8)):
        img = Image.new('RGB', (W, H), (10, 15, 20))
        draw = ImageDraw.Draw(img)

        # Sky gradient
        for y in range(H):
            t = y / H
            r = int(8 + 35 * t)
            g = int(18 + 62 * t)
            b = int(28 + 70 * t)
            draw.line([(0, y), (W, y)], fill=(r, g, b))

        # Ground / site base
        draw.rectangle([0, int(H * 0.68), W, H], fill=(23, 34, 44))
        draw.rectangle([0, int(H * 0.68), W, H], outline=(60, 84, 102), width=2)

        # Create scene-specific architectural sketches and shapes
        if title == 'Empty Plot':
            draw.rectangle([int(W*0.15), int(H*0.55), int(W*0.85), int(H*0.72)], fill=(145, 110, 70))
            draw.rectangle([int(W*0.17), int(H*0.57), int(W*0.83), int(H*0.70)], outline=(220, 200, 170), width=4)
            draw.text((int(W*0.23), int(H*0.28)), 'Empty Plot', fill=(255, 255, 255), font=font)
            draw.text((int(W*0.23), int(H*0.36)), 'Ready for vision and structure', fill=(220, 230, 240), font=small_font)
        elif title == 'Surveying':
            draw.rectangle([int(W*0.18), int(H*0.58), int(W*0.82), int(H*0.72)], fill=(90, 122, 152))
            draw.line([(int(W*0.22), int(H*0.62)), (int(W*0.78), int(H*0.62))], fill=(255, 255, 255), width=4)
            draw.line([(int(W*0.22), int(H*0.66)), (int(W*0.70), int(H*0.66))], fill=(255, 255, 255), width=4)
            draw.line([(int(W*0.22), int(H*0.70)), (int(W*0.64), int(H*0.70))], fill=(255, 255, 255), width=4)
            draw.text((int(W*0.22), int(H*0.28)), 'Surveying', fill=(255, 255, 255), font=font)
            draw.text((int(W*0.22), int(H*0.36)), 'Precision measurements and site planning', fill=(220, 230, 240), font=small_font)
        elif title == 'Blueprint':
            draw.rectangle([int(W*0.20), int(H*0.24), int(W*0.80), int(H*0.76)], fill=(247, 247, 247))
            draw.rectangle([int(W*0.22), int(H*0.26), int(W*0.78), int(H*0.74)], outline=(80, 100, 128), width=4)
            draw.line([(int(W*0.28), int(H*0.34)), (int(W*0.72), int(H*0.34))], fill=(40, 84, 125), width=3)
            draw.line([(int(W*0.28), int(H*0.42)), (int(W*0.70), int(H*0.42))], fill=(60, 111, 166), width=3)
            draw.line([(int(W*0.28), int(H*0.50)), (int(W*0.66), int(H*0.50))], fill=(80, 133, 192), width=3)
            draw.text((int(W*0.22), int(H*0.18)), 'Blueprint', fill=(255, 255, 255), font=font)
        elif title == 'Excavation':
            draw.rectangle([int(W*0.18), int(H*0.58), int(W*0.82), int(H*0.72)], fill=(72, 95, 110))
            draw.rectangle([int(W*0.23), int(H*0.54), int(W*0.77), int(H*0.62)], fill=(117, 89, 61))
            draw.rectangle([int(W*0.26), int(H*0.50), int(W*0.74), int(H*0.56)], fill=(160, 126, 88))
            draw.text((int(W*0.22), int(H*0.28)), 'Excavation', fill=(255, 255, 255), font=font)
            draw.text((int(W*0.22), int(H*0.36)), 'Site is shaped for a strong foundation', fill=(220, 230, 240), font=small_font)
        elif title == 'Foundation':
            draw.rectangle([int(W*0.20), int(H*0.56), int(W*0.80), int(H*0.72)], fill=(120, 120, 120))
            draw.rectangle([int(W*0.24), int(H*0.54), int(W*0.76), int(H*0.58)], fill=(200, 200, 200))
            draw.rectangle([int(W*0.28), int(H*0.52), int(W*0.72), int(H*0.56)], fill=(220, 220, 220))
            draw.text((int(W*0.22), int(H*0.28)), 'Foundation', fill=(255, 255, 255), font=font)
        elif title == 'RCC Structure':
            draw.rectangle([int(W*0.24), int(H*0.46), int(W*0.76), int(H*0.72)], fill=(170, 180, 190))
            draw.rectangle([int(W*0.28), int(H*0.42), int(W*0.72), int(H*0.46)], fill=(237, 241, 245))
            draw.line([(int(W*0.30), int(H*0.46)), (int(W*0.30), int(H*0.72))], fill=(255, 255, 255), width=6)
            draw.line([(int(W*0.46), int(H*0.46)), (int(W*0.46), int(H*0.72))], fill=(255, 255, 255), width=6)
            draw.line([(int(W*0.62), int(H*0.46)), (int(W*0.62), int(H*0.72))], fill=(255, 255, 255), width=6)
            draw.line([(int(W*0.30), int(H*0.54)), (int(W*0.62), int(H*0.54))], fill=(255, 255, 255), width=6)
            draw.text((int(W*0.20), int(H*0.28)), 'RCC Columns & Beams', fill=(255, 255, 255), font=font)
        elif title == 'Brick Walls':
            draw.rectangle([int(W*0.24), int(H*0.46), int(W*0.76), int(H*0.72)], fill=(175, 128, 94))
            draw.rectangle([int(W*0.26), int(H*0.44), int(W*0.74), int(H*0.72)], outline=(230, 206, 183), width=4)
            draw.line([(int(W*0.28), int(H*0.46)), (int(W*0.28), int(H*0.72))], fill=(226, 194, 160), width=6)
            draw.line([(int(W*0.46), int(H*0.46)), (int(W*0.46), int(H*0.72))], fill=(226, 194, 160), width=6)
            draw.line([(int(W*0.64), int(H*0.46)), (int(W*0.64), int(H*0.72))], fill=(226, 194, 160), width=6)
            draw.text((int(W*0.22), int(H*0.28)), 'Brick Walls', fill=(255, 255, 255), font=font)
        elif title == 'Roof Slab':
            draw.rectangle([int(W*0.20), int(H*0.40), int(W*0.80), int(H*0.72)], fill=(210, 220, 230))
            draw.rectangle([int(W*0.20), int(H*0.40), int(W*0.80), int(H*0.72)], outline=(86, 102, 123), width=6)
            draw.text((int(W*0.22), int(H*0.28)), 'Roof Slab', fill=(255, 255, 255), font=font)
        elif title == 'Exterior Finish':
            draw.rectangle([int(W*0.20), int(H*0.42), int(W*0.80), int(H*0.72)], fill=(210, 180, 150))
            draw.rectangle([int(W*0.22), int(H*0.40), int(W*0.78), int(H*0.72)], outline=(255, 255, 255), width=4)
            draw.text((int(W*0.20), int(H*0.28)), 'Exterior Finish', fill=(255, 255, 255), font=font)
        elif title == 'Paint & Glass':
            draw.rectangle([int(W*0.18), int(H*0.38), int(W*0.82), int(H*0.72)], fill=(150, 168, 182))
            draw.rectangle([int(W*0.22), int(H*0.34), int(W*0.78), int(H*0.38)], fill=(255, 255, 255))
            draw.rectangle([int(W*0.28), int(H*0.40), int(W*0.36), int(H*0.56)], fill=(80, 120, 160))
            draw.rectangle([int(W*0.40), int(H*0.40), int(W*0.48), int(H*0.56)], fill=(80, 120, 160))
            draw.rectangle([int(W*0.54), int(H*0.40), int(W*0.62), int(H*0.56)], fill=(80, 120, 160))
            draw.text((int(W*0.20), int(H*0.28)), 'Paint & Glass', fill=(255, 255, 255), font=font)
        elif title == 'Landscaping':
            draw.rectangle([int(W*0.10), int(H*0.48), int(W*0.90), int(H*0.72)], fill=(72, 132, 85))
            draw.ellipse([int(W*0.20), int(H*0.34), int(W*0.30), int(H*0.44)], fill=(120, 175, 110))
            draw.ellipse([int(W*0.40), int(H*0.32), int(W*0.56), int(H*0.44)], fill=(95, 150, 95))
            draw.ellipse([int(W*0.66), int(H*0.34), int(W*0.78), int(H*0.44)], fill=(120, 180, 110))
            draw.text((int(W*0.22), int(H*0.28)), 'Landscaping', fill=(255, 255, 255), font=font)
        elif title == 'Main Entrance':
            draw.rectangle([int(W*0.24), int(H*0.38), int(W*0.76), int(H*0.72)], fill=(92, 86, 91))
            draw.rectangle([int(W*0.30), int(H*0.46), int(W*0.70), int(H*0.72)], fill=(154, 140, 130))
            draw.rectangle([int(W*0.42), int(H*0.42), int(W*0.58), int(H*0.52)], fill=(255, 255, 255))
            draw.text((int(W*0.22), int(H*0.28)), 'Main Entrance', fill=(255, 255, 255), font=font)
        elif title == 'Living Room':
            draw.rectangle([int(W*0.18), int(H*0.40), int(W*0.82), int(H*0.72)], fill=(230, 221, 205))
            draw.rectangle([int(W*0.24), int(H*0.50), int(W*0.76), int(H*0.66)], fill=(140, 125, 110))
            draw.text((int(W*0.22), int(H*0.28)), 'Luxury Living Room', fill=(255, 255, 255), font=font)
        elif title == 'Kitchen':
            draw.rectangle([int(W*0.18), int(H*0.40), int(W*0.82), int(H*0.72)], fill=(240, 233, 220))
            draw.rectangle([int(W*0.24), int(H*0.48), int(W*0.76), int(H*0.66)], fill=(140, 150, 175))
            draw.text((int(W*0.22), int(H*0.28)), 'Modular Kitchen', fill=(255, 255, 255), font=font)
        elif title == 'Master Bedroom':
            draw.rectangle([int(W*0.22), int(H*0.42), int(W*0.78), int(H*0.72)], fill=(208, 199, 181))
            draw.rectangle([int(W*0.28), int(H*0.48), int(W*0.72), int(H*0.64)], fill=(140, 115, 95))
            draw.text((int(W*0.22), int(H*0.28)), 'Master Bedroom', fill=(255, 255, 255), font=font)
        elif title == 'Children Room':
            draw.rectangle([int(W*0.22), int(H*0.42), int(W*0.78), int(H*0.72)], fill=(184, 208, 220))
            draw.rectangle([int(W*0.28), int(H*0.48), int(W*0.72), int(H*0.64)], fill=(115, 145, 170))
            draw.text((int(W*0.22), int(H*0.28)), 'Children\'s Bedroom', fill=(255, 255, 255), font=font)
        elif title == 'Guest Bedroom':
            draw.rectangle([int(W*0.22), int(H*0.42), int(W*0.78), int(H*0.72)], fill=(196, 212, 198))
            draw.rectangle([int(W*0.28), int(H*0.48), int(W*0.72), int(H*0.64)], fill=(122, 147, 126))
            draw.text((int(W*0.22), int(H*0.28)), 'Guest Bedroom', fill=(255, 255, 255), font=font)
        elif title == 'Bathroom':
            draw.rectangle([int(W*0.22), int(H*0.42), int(W*0.78), int(H*0.72)], fill=(230, 241, 245))
            draw.rectangle([int(W*0.32), int(H*0.48), int(W*0.68), int(H*0.64)], fill=(160, 195, 215))
            draw.text((int(W*0.22), int(H*0.28)), 'Luxury Bathroom', fill=(255, 255, 255), font=font)
        elif title == 'Study & Dining':
            draw.rectangle([int(W*0.18), int(H*0.40), int(W*0.82), int(H*0.72)], fill=(220, 224, 231))
            draw.rectangle([int(W*0.24), int(H*0.48), int(W*0.42), int(H*0.64)], fill=(140, 145, 155))
            draw.rectangle([int(W*0.48), int(H*0.48), int(W*0.76), int(H*0.64)], fill=(140, 145, 155))
            draw.text((int(W*0.22), int(H*0.28)), 'Study & Dining', fill=(255, 255, 255), font=font)
        elif title == 'Final Home':
            draw.rectangle([int(W*0.14), int(H*0.30), int(W*0.86), int(H*0.72)], fill=(210, 184, 146))
            draw.rectangle([int(W*0.16), int(H*0.32), int(W*0.84), int(H*0.70)], outline=(255, 255, 255), width=6)
            draw.rectangle([int(W*0.28), int(H*0.46), int(W*0.72), int(H*0.64)], fill=(255, 255, 255))
            draw.rectangle([int(W*0.24), int(H*0.36), int(W*0.76), int(H*0.44)], fill=(240, 230, 210))
            draw.ellipse([int(W*0.15), int(H*0.22), int(W*0.30), int(H*0.33)], fill=(110, 180, 110))
            draw.ellipse([int(W*0.70), int(H*0.22), int(W*0.86), int(H*0.33)], fill=(110, 180, 110))
            draw.text((int(W*0.22), int(H*0.18)), 'Dream Home', fill=(255, 255, 255), font=font)
            draw.text((int(W*0.22), int(H*0.24)), 'Completed luxury residence', fill=(235, 240, 245), font=small_font)

        # Overlay gradient and captions
        overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
        draw_overlay = ImageDraw.Draw(overlay)
        draw_overlay.rectangle([0, 0, W, H], fill=(0, 0, 0, 45))
        draw_overlay.rectangle([0, int(H*0.78), W, H], fill=(0, 0, 0, 80))
        img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')

        draw = ImageDraw.Draw(img)
        draw.text((int(W*0.08), int(H*0.82)), title, fill=(255, 255, 255), font=font)
        draw.text((int(W*0.08), int(H*0.88)), subtitle, fill=(220, 228, 236), font=small_font)

        frames.append(np.array(img))

# Add a few extra frames for smooth loop
for _ in range(int(fps * 1.2)):
    frames.append(frames[-1])

imageio.mimsave(out_path, frames, fps=fps, codec='libx264', quality=8, macro_block_size=1)
print('Created', out_path)