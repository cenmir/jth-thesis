# Quarto Thesis Template (JU School of Engineering)

A Quarto **book** project that produces a single, formatted PDF thesis for
the School of Engineering at Jönköping University. The chapters below act as
a guide on how to write each part of the thesis; replace the guide text with
your own content as you go.

Designed to run out-of-the-box on the new **jupyter.ju.se** JupyterHub, which
has Python, Jupyter, Quarto and a TeX distribution preinstalled.

## Project layout

```
_quarto.yml                  Book configuration (chapters, format, metadata)
index.qmd                    Abstract (entry point of the book)
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
apa.csl                      Citation style (APA)
titlepage.tex                Custom title page (reads metadata from _quarto.yml)
before-body.tex              Front-matter / TOC LaTeX partial
title.tex                    Empty Pandoc partial (titlepage handled elsewhere)
preamble.tex                 LaTeX packages (amsmath, bm, scrlayer-scrpage, float)
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

Output appears in `_output/`. The rendered book is `_output/<title>.pdf`.

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
  date: "May 2026"

thesis-type: "Master Thesis"
programme: "Industrial Product Realisation"
examiner: "Name of the examiner"
supervisor: "Name of the supervisor"
scope: "30 credits (second cycle)"
date-signed: "2026-05-XX"
```

`titlepage.tex` consumes those values, so you do not edit LaTeX by hand for
the title page.

## Working on jupyter.ju.se

1. Log in to https://jupyter.ju.se
2. Open a terminal: `git clone <your fork of this repo>`
3. Open any `.ipynb` chapter in the Jupyter Lab interface and edit it
4. From the terminal, run `quarto render` to produce the PDF

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

## License

Pick a license, put it here.
