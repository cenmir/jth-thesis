# Before submission

Run through every item. Distilled from supervisor reviews; each item
caught real issues in previous theses.

## Front matter

- [ ] Title page date filled in (not "2026-XX-XX")
- [ ] Examiner, supervisor, co-supervisor fields filled in
- [ ] Abstract written (not the template placeholder)
- [ ] Preface / Acknowledgements present and signed
- [ ] List of Abbreviations populated
- [ ] Nomenclature populated (if mathematical symbols are used)
- [ ] Table of Contents, List of Figures, List of Tables render correctly. Search the rendered PDF for "??", "?@", and "No table of figures entries found"

## Cross-references

- [ ] No literal `?@sec-foo` or `?@fig-bar` in the rendered PDF. Search the source for `?@` before rendering
- [ ] Every figure has a `{#fig-name}` label and is referenced from prose as `@fig-name`
- [ ] Every table has a caption line `: caption {#tbl-name}` below the table and is referenced from prose as `@tbl-name`
- [ ] Every equation referenced from prose has a `{#eq-name}` label
- [ ] Captions are not doubled (no "Figure 2.3: Figure 3: ...")

## Language and style

- [ ] No em dashes (`—`) or double dashes (`--`) as appositive separators. Global search-and-replace
- [ ] No AI-style filler: "delve into", "it is worth noting", "state-of-the-art", "leverage", "robust", "this indicates that", "furthermore, it is important to"
- [ ] No `\cdot` between variables (only between numbers or in vector dot products)
- [ ] No code identifiers in prose or equations (use `$P_\text{stab}$`, not `stab_p`)
- [ ] No Swedish placeholders left in body or headings ("Skriva här", "Lägg in...", "Måste förbättras", "SE ÖVER", "(källa)")
- [ ] No yellow / highlighted draft text
- [ ] No template instruction text left in chapter openings ("This chapter introduces...", "Typically, this chapter is used to...")
- [ ] Pick British or American spelling and apply consistently
- [ ] Spell-check pass after content is stable

## Citations

- [ ] In-text citations clickable in the PDF (test by clicking `[1]`)
- [ ] DOI / URL links clickable and resolving
- [ ] No web-source citations that should be footnotes (tutoring sites, marketing pages, Wikipedia, dictionaries). Move to `^[footnote]` syntax or replace with peer-reviewed sources

## Engineering content

- [ ] Every research question is explicitly answered in Conclusions (verbatim "RQ1: ...", "RQ2: ...")
- [ ] Every claim is supported by data, validated against experiments, requirements or benchmark
- [ ] Theory sections are referenced later in method or results. If not, cut them
- [ ] Stakeholder needs are translated to measurable engineering targets with units (not qualitative themes)
- [ ] Self-critical discussion: model and calibration limitations, sources of error, honest equipment shortcomings
- [ ] Tangible deliverable named (calibrated model, prototype, workflow, code)
