import os
import unicodedata

# Path to glyphs file (relative to /code/)
IGLYPH_FILE = "../data/glyphs_1200.txt"

# Load glyphs from file
def load_iglyphs(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        # Read all text, strip whitespace/newlines
        glyph_text = f.read().replace("\n", "").strip()
    glyphs_list = list(glyph_text)  # Split into individual Unicode chars
    return glyphs_list

# Get crude size from Unicode spec
def get_unicode_size(glyph_in):
    width = unicodedata.east_asian_width(glyph_in)
    # Map width to a crude "size" score (arbitrary units)
    size_map = {
        "N": 1.0,   # Narrow (most Latin, symbols)
        "W": 2.0,   # Wide (CJK-like)
        "F": 2.0,   # Full-width
        "H": 0.5,   # Half-width
        "A": 1.5,   # Ambiguous (guess middle)
        "Na": 1.0   # Neutral (default to narrow)
    }
    return size_map.get(width, 1.0)  # Default to 1.0 if unknown


# Main
if __name__ == "__main__":
    if os.path.exists(IGLYPH_FILE):
        iglyphs = load_iglyphs(IGLYPH_FILE)
        print(f"Loaded {len(iglyphs)} iglyphs")

        # Score sizes and categorize
        iglyph_sizes = [(ig, get_unicode_size(ig)) for ig in iglyphs]

        # Filter half-width (0.5), full-width/wide (2.0), and ambiguous (1.5)
        half_width = [ig for ig, size in iglyph_sizes if size == 0.5]
        full_width = [ig for ig, size in iglyph_sizes if size == 2.0]
        ambiguous = [ig for ig, size in iglyph_sizes if size == 1.5]

        # Print and count
        print("\nHalf-width iglyphs (size 0.5):")
        print("".join(half_width))
        print(f"Count: {len(half_width)}")

        print("\nFull-width/Wide iglyphs (size 2.0):")
        print("".join(full_width))
        print(f"Count: {len(full_width)}")

        print("\nAmbiguous iglyphs (size 1.5):")
        print("".join(ambiguous))
        print(f"Count: {len(ambiguous)}")

        # Recap stats
        sizes = [s for _, s in iglyph_sizes]
        print(f"\nMin size: {min(sizes)}, Max size: {max(sizes)}, Avg size: {sum(sizes) / len(sizes):.2f}")
    else:
        print(f"File not found at {IGLYPH_FILE}")