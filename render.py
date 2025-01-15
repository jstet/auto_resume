import os
import subprocess
from jinja2 import Environment, FileSystemLoader
from rich.console import Console
import json

console = Console()

json_file = "data.json"
template_file = "templates/template.tex"
latex_dir = "latex/"
latex_file = os.path.join(latex_dir, "CV.tex")
out_file = os.path.join(latex_dir, "CV.pdf")

console.log("Starting.")

os.makedirs(latex_dir, exist_ok=True)

try:
    with open(json_file) as f:
        data = json.load(f)
except FileNotFoundError:
    console.log(f"[red]Error: {json_file} not found.[/red]")
    exit(1)

name = data.get("name", "User")
console.print(f"Hello {name}, this script will now autogenerate your CV.")

try:
    environment = Environment(
        loader=FileSystemLoader("./"),
        trim_blocks=True,
        block_start_string='%$',
        block_end_string='$%',
        variable_start_string='$$',
        variable_end_string='$$'
    )
    template = environment.get_template(template_file)
except Exception as e:
    console.log(f"[red]Error loading template: {e}[/red]")
    exit(1)

try:
    with open(latex_file, 'w') as f:
        f.write(template.render(data))
except Exception as e:
    console.log(f"[red]Error writing LaTeX file: {e}[/red]")
    exit(1)

console.rule("Running pdflatex...")

try:
    p = subprocess.run(["pdflatex", "CV.tex"], cwd=latex_dir, check=True)
except subprocess.CalledProcessError as e:
    console.log(f"[red]Error running pdflatex: {e}[/red]")
    exit(1)

try:
    os.rename(out_file, "CV.pdf")
except FileNotFoundError:
    console.log("[red]Error: CV.pdf not found. pdflatex may have failed.[/red]")
    exit(1)

console.rule()
console.log("Done!")
console.print(f'Find your CV in the file "CV.pdf".')
