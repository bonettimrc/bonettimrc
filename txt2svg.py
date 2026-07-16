from pathlib import Path
import html

def generate_svg(input_path="github.txt", output_path="github.svg"):
    # Read all lines
    lines = Path(input_path).read_text(encoding="utf-8").splitlines()
    
    # Generate tspans (first line inherits x/y from <text>; others use dy)
    tspans = [f'<tspan>{html.escape(lines[0])}</tspan>'] + [
        f'<tspan x="20" dy="1.37em">{html.escape(line)}</tspan>' for line in lines[1:]
    ]
    
    # Calculate height dynamically
    height = len(lines) * 20 + 75

    # Assemble the clean SVG template (keeping the text block on a tight single line)
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 950 {height}" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#151b23" rx="10" />
  <text x="20" y="55" font-family="monospace" font-size="14" fill="#f0f6fc" xml:space="preserve">{"".join(tspans)}</text>
</svg>"""

    # Write the file
    Path(output_path).write_text(svg, encoding="utf-8")
    print(f"Success! SVG saved to {output_path}")

if __name__ == "__main__":
    generate_svg()