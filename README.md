# Quarto Thesis Template (JU School of Engineering)

A Quarto **book** project that produces a single, formatted PDF thesis for
the School of Engineering at Jönköping University. The chapters below act as
a guide on how to write each part of the thesis; replace the guide text with
your own content as you go.

Designed to run out of the box on the school's
**[jupyter.ju.se](https://jupyter.ju.se)** JupyterHub, which has Python,
Jupyter, Quarto and a TeX distribution preinstalled. Students are expected to
write the thesis on that server; everything is done from the JupyterLab
interface, with no terminal and nothing to install.

For background on the Quarto + Python + LaTeX workflow, see
[python.ju.se](https://python.ju.se) and in particular the
[writing documentation guide](https://python.ju.se/ProgrammingFundamentals/writing_documentation.html),
which covers Quarto installation, math syntax, code execution and the
Pandoc-to-LaTeX pipeline in more detail than this README.

## Project layout

```
_quarto.yml                  Book configuration (chapters, format, metadata)
index.qmd                    Abstract. Filename is fixed: Quarto book
                             requires an `index.qmd` as the entry point.
preface.qmd                  Preface and acknowledgements
abbreviations.qmd            List of abbreviations + nomenclature
introduction.ipynb           Chapter 1: Introduction
theory.ipynb                 Chapter 2: Theoretical background
methodology.ipynb            Chapter 3: Methodology
results.ipynb                Chapter 4: Results
analysis.ipynb               Chapter 5: Analysis
discussion.ipynb             Chapter 6: Discussion
conclusions.ipynb            Chapter 7: Conclusions
references.qmd               References (auto-populated from references.bib)
appendix.qmd                 Appendices
references.bib               BibTeX bibliography
ieee.csl                     Citation style: IEEE numeric (default)
apa-7th.csl                  Citation style: APA 7th edition (alternative)
before-body.tex              Title page + front-matter LaTeX partial
title.tex                    Empty Pandoc partial (title page lives in before-body.tex)
preamble.tex                 LaTeX packages and the \bm to \symbf alias for unicode-math
images/                      Figures
CHECKLIST.md                 Pre-submission checklist
```

The body chapters are `.ipynb` files so they can be opened directly in Jupyter
and so code cells can produce computed tables and figures. The front matter
and appendix are plain `.qmd` files because they rarely need executable code.

## Building the PDF

On [jupyter.ju.se](https://jupyter.ju.se): open any chapter and click **PDF**
in the toolbar (the same choices sit in the **Quarto** menu). See
[Working on jupyter.ju.se](#working-on-jupyterjuse) below for the whole flow.

On your own computer, from the project root:

```bash
quarto render
```

The rendered book is `<title>.pdf` next to `_quarto.yml`.

**A book always renders whole.** Rendering one chapter, whether with the PDF
button or with `quarto render theory.ipynb`, still produces the complete
thesis PDF; that is how Quarto book projects work for PDF output. Use the
live preview while drafting if you want something faster than a full build.

## Editing the title page metadata

Title, authors, examiner, supervisor and similar fields are set once at the
top of `_quarto.yml`:

```yaml
book:
  title: "Title of the Thesis"
  author:
    - "First Author"
    - "Second Author"
  date: 2026-05-15           # ISO date; date-format below controls display
  date-format: "MMMM YYYY"

thesis-type: "Master Thesis"
programme: "Industrial Product Realisation"
subject-label: "THESIS WITHIN"   # the label before it on the title page
examiner: "Name of the examiner"
supervisor: "Name of the supervisor"
scope: "30 credits (second cycle)"
date-signed: "2026-05-XX"
```

`before-body.tex` consumes those values via Pandoc template substitution,
so you do not edit LaTeX by hand for the title page.

## Working on jupyter.ju.se

The school's JupyterHub at [jupyter.ju.se](https://jupyter.ju.se) is where the
thesis is meant to be written. Python, Jupyter, Quarto and TeX Live are
installed, this template is already in your account, and you need neither a
terminal nor a download.

1. Sign in at [jupyter.ju.se](https://jupyter.ju.se).
2. On the start page (the **Launcher**, opened with the **+** button above the
   file browser) look under **JTH templates** and click **New thesis**. Your
   own copy is created as `thesis1` and opened for you.
3. Write: the chapters are ordinary notebooks, `index.qmd` holds the abstract,
   and the title page fields live at the top of `_quarto.yml`.
4. Click **PDF** in the toolbar to build the thesis. A panel opens and shows
   the progress; when it says `Output created: …pdf`, the PDF is next to your
   chapters in the file browser. The first build can take a minute while LaTeX
   packages are installed.
5. **Preview** opens the thesis in a browser tab that rebuilds every time you
   save, which is the comfortable way to write. Stop it with **Quarto → Stop
   the preview**.

Do not work inside `~/templates/jth-thesis`. That folder is a read-only
reference that is kept up to date for you, and the Launcher card is what makes
your own copy of it.

### Working as a team (git version control)

The Launcher card gives you a plain folder with no git history. If two students
write together, fork this repository on GitHub, then open a terminal on the hub
(**File → New → Terminal**) and clone your fork:

```bash
git clone https://github.com/<your-account>/jth-thesis.git thesis
```

`git add`, `git commit` and `git push` then work as usual, and both authors can
pull each other's changes. This is the one part of the workflow that does need
the terminal.

### Outside jupyter.ju.se

Download or clone this repository, install
[Quarto](https://quarto.org/docs/get-started/), Python with Jupyter and a LaTeX
distribution (`quarto install tinytex` is the small option), then run
`quarto render` in the project root.

### Troubleshooting

If something in the Quarto pipeline does not behave as expected (math not
rendering, citations missing, code cells not executing), the
[writing documentation guide on python.ju.se](https://python.ju.se/ProgrammingFundamentals/writing_documentation.html)
covers the fundamentals and the most common pitfalls.

Code cells with `#| eval: false` in their first line render the listing without
executing it, which is the safer default for a thesis. Switch to `eval: true`
once the analysis is final.

## What lives where

- **Style and content guidance** is embedded in each chapter as italicised
  intro paragraphs and short worked examples.
- **Submission checklist** is in `CHECKLIST.md` at the project root (not
  rendered into the book).
- **References** are managed in `references.bib`. Cite with `@key` or
  `[@key]` and Quarto handles the rest.
- **Citation style** defaults to IEEE numeric (`ieee.csl`). To switch to
  APA 7, change one line in `_quarto.yml`:
  ```yaml
  csl: ieee.csl       # numeric, IEEE Reference Guide (default)
  # csl: apa-7th.csl  # author-date, APA 7th edition
  ```
  IEEE suits math- and engineering-heavy theses; APA 7 suits theses with
  a strong empirical or qualitative component. Ultimately the authors'
  choice, subject to the programme's submission guidelines.

## License

The template itself (Quarto sources, LaTeX partials, build scripts,
prose guidance) is released under the
[Creative Commons Attribution 4.0 International License](LICENSE)
(CC BY 4.0). Students and other supervisors are free to fork, adapt
and redistribute it for any thesis project, commercial or not, with
or without modification. The only requirement is **attribution**: cite
the author and link back to this repository in any derivative work.
See `LICENSE` for the suggested citation format.

Files that are *bundled with* the template but covered by other terms:

- `ieee.csl` and `apa-7th.csl` come from <https://www.zotero.org/styles>
  and remain under the upstream Citation Style Language project's
  licence (CC BY-SA). They are unchanged from the upstream versions.
- `images/schoolLogo.*` are the Jönköping University School of
  Engineering logos and belong to JU. They are included for student use
  of this template within JU; external forks should replace them with
  their own institution's branding.
- `images/chad.jpg` is a placeholder figure used only to demonstrate
  Quarto's image-embedding syntax. Replace it with a real figure
  before submission.

CC BY 4.0 covers *the template*, not the thesis you produce with it.
Your thesis text is your work; you decide its licence and copyright
independently of this repository.
