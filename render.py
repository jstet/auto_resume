
from jinja2 import Environment, FileSystemLoader
import subprocess
from rich.console import Console
import json

console = Console()

json_file = "data.json"
template_file = "templates/template.tex"
latex_file = "CV.tex"
latex_dir = "latex/"
out_file = "CV.pdf"

console.log("Starting.")

with open('data.json') as f:
    data = json.load(f)

name = data["name"]
console.print(f"Hello {name}, this script will now autogenerate your CV.")


environment = Environment(loader=FileSystemLoader("./"), trim_blocks=True, block_start_string='@@',block_end_string='@@',variable_start_string='@=', variable_end_string='=@')

template = environment.get_template(template_file)

with open(latex_dir + latex_file, 'w') as f:
    f.write(template.render(
        data
    ))
    

console.rule("Pandoc doing it's work...")

p = subprocess.Popen(["pdflatex", latex_file], cwd=latex_dir)
p.wait()

p = subprocess.Popen(["mv", latex_dir + out_file, out_file])
p.wait()

console.rule()

console.log("Done!")

console.print(f'Find your CV in the file "{out_file}".')