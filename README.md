# Render a nice looking LaTeX resume with data you enter into a simple JSON file. 

Resumes contain information that is well suited for compact data formats such as JSON. Instead of relearning LaTeX and browsing a complex .tex file every time your resume needs updating, this script allows you to quickly edit a neat .json file and then render your resume to .pdf. 

The script was written with python and uses a [premade LaTex template](https://github.com/liantze/AltaCV).

## Setup

I only tested the setup on linux, so no guarantees this will work for other OS.


### A: Edit data.json.

There is an example .json file included in this repo (aka info about me). Edit the existing values or add new objects (in the demonstrated format) as you wish.

### B: Install the packages listed in requirements.txt

Whether you set up an evironment for this is your choice. You can install the packages with this command for example:

```
python -m pip install -r requirements.txt
```
### C: Make sure the pdflatex utility is installed on your OS

On Arch you can install the package "texlive-most" for example.

### D: Render the PDF 

```
python render.py
```

## Customization

- If you want to change the look of the resume, consult the documentation of the [LaTex template](https://github.com/liantze/AltaCV) this project is based on.
- Add new variables to template.tex by enclosing them with double dollar signs, e.g. 
    ```
    $$variable$$. 
    ```
- Enclose jinja2 logic blocks like this:
    ```
    %$ logic $%
    ```
    I chose these characters because they don't destroy the LaTeX syntax (code editors will not mark them)

## Sources and helpful links

- The Latex template was made using: https://github.com/liantze/AltaCV
- A list of icons u can use in the CV: https://texdoc.org/serve/fontawesome5/0
