# Quarto Thesis Template (JU School of Engineering)

A Quarto **book** project that produces a single, formatted PDF thesis for
the School of Engineering at Jönköping University. The chapters below act as
a guide on how to write each part of the thesis; replace the guide text with
your own content as you go.

Designed to run out-of-the-box on the new **[jupyter.ju.se](https://jupyter.ju.se)**
JupyterHub (work in progress), which has Python, Jupyter, Quarto and a TeX
distribution preinstalled. Students are expected to write the thesis on
that server.

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

From the project root, run:

```bash
quarto render
```

Output appears in the project root. The rendered book is `<title>.pdf` next to `_quarto.yml`.

To render a single chapter while drafting:

```bash
quarto render theory.ipynb --to pdf
```

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
examiner: "Name of the examiner"
supervisor: "Name of the supervisor"
scope: "30 credits (second cycle)"
date-signed: "2026-05-XX"
```

`before-body.tex` consumes those values via Pandoc template substitution,
so you do not edit LaTeX by hand for the title page.

## Working on jupyter.ju.se

The recommended environment is the school's JupyterHub at
[jupyter.ju.se](https://jupyter.ju.se) (work in progress). It comes with
Python, Jupyter, Quarto and TeX Live preinstalled, so there is nothing
to install locally.

### Quick start (one terminal command)

1. Log in to <https://jupyter.ju.se>.
2. Open a terminal in Jupyter Lab (File → New → Terminal).
3. Paste this single line, press Enter:

   ```bash
   mkdir -p ~/thesis && curl -fsSL https://github.com/cenmir/jth-thesis/archive/refs/heads/main.tar.gz | tar xz -C ~/thesis --strip-components=1 && cd ~/thesis && quarto render
   ```

4. When the command finishes, the PDF is at `~/thesis/JTH-Thesis-Template.pdf`.
   Open it from the Jupyter Lab file browser to verify the build worked.

What the one-liner does, in four steps:

- `mkdir -p ~/thesis` creates the working folder.
- `curl -fsSL .../main.tar.gz` downloads the latest tarball of this
  template's `main` branch from GitHub.
- `tar xz -C ~/thesis --strip-components=1` extracts the contents
  directly into `~/thesis` (no wrapping `jth-thesis-main/` folder).
- `cd ~/thesis && quarto render` produces the first PDF so you know
  the toolchain works before you start editing.

After that, open any `.ipynb` chapter in Jupyter Lab and edit it. To
rebuild the PDF: in the terminal, run `quarto render` again. To rebuild
only the chapter you are editing: `quarto render theory.ipynb --to pdf`.

### Working as a team (git version control)

The one-liner above pulls a static snapshot, with no git history. If
two students need to collaborate, fork the template on GitHub first and
then clone your fork instead:

```bash
cd ~
git clone https://github.com/<your-account>/jth-thesis.git thesis
cd thesis
quarto render
```

That way `git add`, `git commit`, and `git push` work as expected, and
both authors can pull each other's changes.

### Troubleshooting

If something in the Quarto pipeline does not behave as expected (math
not rendering, citations missing, code cells not executing), the
[writing documentation guide on python.ju.se](https://python.ju.se/ProgrammingFundamentals/writing_documentation.html)
covers the fundamentals and the most common pitfalls.

Code cells with `#| eval: false` in their first line render the listing
without executing it, which is the safer default for a thesis. Switch to
`eval: true` once the analysis is final.

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
