# Draws the 18 November 2026 world-news front page (1024x1024 PNG).
# Run once locally to produce entry.png; main.py copies it in the grader.
from PIL import Image, ImageDraw, ImageFont
import textwrap

W, H = 1024, 1024
PAPER = (247, 243, 233)
INK = (18, 18, 18)
RED = (178, 34, 34)
NAVY = (16, 42, 84)
GOLD = (197, 150, 40)
TEAL = (14, 107, 107)
GREY = (90, 90, 90)
LIGHT = (236, 230, 214)

FD = "/usr/share/fonts/truetype/dejavu/"
def font(name, size):
    return ImageFont.truetype(FD + name, size)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def wrap(text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def block(x, y, text, f, color, maxw, leading=None):
    leading = leading or int(f.size * 1.18)
    for ln in wrap(text, f, maxw):
        d.text((x, y), ln, font=f, fill=color)
        y += leading
    return y

def centered(y, text, f, color):
    w = d.textlength(text, font=f)
    d.text(((W - w) / 2, y), text, font=f, fill=color)
    return y + int(f.size * 1.25)

# --- Masthead ---
d.rectangle([0, 0, W, 128], fill=INK)
centered(10, "THE WORLD IN ONE DAY", font("DejaVuSerif-Bold.ttf", 54), (255, 255, 255))
centered(78, "WEDNESDAY  18  NOVEMBER  2026  ·  WORLD NEWS ROUNDUP", font("DejaVuSans-Bold.ttf", 25), GOLD)

# --- Lead story ---
d.rectangle([24, 142, 1000, 452], outline=INK, width=3)
d.rectangle([24, 142, 1000, 182], fill=RED)
d.text((40, 148), "LEAD STORY · SHENZHEN, CHINA", font=font("DejaVuSans-Bold.ttf", 24), fill=(255, 255, 255))
y = block(40, 192, "XI AND PUTIN MEET IN SHENZHEN AHEAD OF HISTORIC TRUMP–XI–PUTIN SUMMIT",
          font("DejaVuSerif-Bold.ttf", 34), INK, 620)
y = block(40, y + 4, "Xi Jinping and Vladimir Putin opened talks in Shenzhen on Wednesday, a day before the first-ever three-way summit with US President Donald Trump at APEC. Nuclear arms and the Ukraine and Iran wars top the agenda.",
          font("DejaVuSans.ttf", 21), (40, 40, 40), 620)
# simple illustration: three flags / handshake circles
for i, (label, col) in enumerate([("USA", NAVY), ("CHINA", RED), ("RUSSIA", TEAL)]):
    x0 = 695 + i * 95
    d.rectangle([x0, 210, x0 + 80, 270], fill=col, outline=INK, width=2)
    tw = d.textlength(label, font=font("DejaVuSans-Bold.ttf", 17))
    d.text((x0 + (80 - tw) / 2, 228), label, font=font("DejaVuSans-Bold.ttf", 17), fill=(255, 255, 255))
d.ellipse([755, 290, 855, 360], outline=INK, width=3)
d.text((777, 312), "APEC", font=font("DejaVuSans-Bold.ttf", 24), fill=INK)
d.text((695, 375), "Talks Wed · summit Thu 19 Nov", font=font("DejaVuSans.ttf", 17), fill=GREY)

# --- Four panels (2x2) ---
panels = [
    ("MIDDLE EAST", "US–IRAN WAR ESCALATES IN THE GULF",
     "US jets struck an IRGC missile site on Iran's Qeshm Island after a drone attack on a US base in Bahrain. Iran fired on Kuwait and Gulf shipping; oil held near $93.", RED),
    ("EUROPE · UKRAINE WAR", "UKRAINE DISABLES KERCH BRIDGE, HITS REFINERY",
     "Ukrainian strikes shut the Kerch Bridge to Crimea for a second night and hit Russia's Kirishi oil refinery, as Russian missiles struck bridges in Kyiv.", NAVY),
    ("UNITED STATES", "DEMOCRATS TAKE THE SENATE: PELTOLA WINS ALASKA",
     "Mary Peltola defeated Republican incumbent Dan Sullivan in Alaska, giving Democrats a projected 56–44 majority in the incoming US Senate.", TEAL),
    ("CLIMATE · COP31, ANTALYA", "COP31 ENTERS DECISIVE FINAL DAYS",
     "Negotiators in Antalya are working through a draft deal with 144 disputed items as the climate summit heads to its Friday 20 November deadline.", GOLD),
]
positions = [(24, 466), (516, 466), (24, 700), (516, 700)]
for (kicker, head, body, col), (x, y0) in zip(panels, positions):
    d.rectangle([x, y0, x + 484, y0 + 220], fill=(255, 255, 255), outline=INK, width=2)
    d.rectangle([x, y0, x + 484, y0 + 34], fill=col)
    d.text((x + 14, y0 + 5), kicker, font=font("DejaVuSans-Bold.ttf", 19), fill=(255, 255, 255))
    yy = block(x + 14, y0 + 44, head, font("DejaVuSerif-Bold.ttf", 24), INK, 456)
    block(x + 14, yy + 4, body, font("DejaVuSans.ttf", 19), (40, 40, 40), 456)

# --- Bottom strip: Asia weather + ticker ---
d.rectangle([24, 934, 1000, 1000], fill=NAVY)
d.text((40, 942), "ASIA WEATHER: SEVERE CYCLONE AKVAN — MASS EVACUATIONS IN ODISHA, INDIA", font=font("DejaVuSans-Bold.ttf", 20), fill=(255, 255, 255))
d.text((40, 968), "Also Wednesday: Voyager 1 reaches one light-day from Earth · ICJ: Myanmar genocide vs Rohingya", font=font("DejaVuSans.ttf", 18), fill=(210, 220, 240))

img.save("entry.png", optimize=True)
print("saved entry.png")
