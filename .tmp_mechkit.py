"""Add a MechanicsKit subsection in section 3.6, between the pandas
example and the project-wide defaults."""

import json
from pathlib import Path

ANCHOR = "### Project-wide execution defaults"

NEW_SECTION = r"""### MechanicsKit

The worked examples above use only widely-available libraries (numpy, matplotlib, sympy, pandas). For mechanical-engineering work the supervisor maintains a Python helper library, **MechanicsKit**, that bundles utilities used across thesis projects: a `Mesh` class for FEM data, a 1-based array wrapper (`OneArray`) for textbook-aligned indexing, Gaussian quadrature integration tools, plotting helpers (`patch`, `fplot`), and LaTeX-display utilities for NumPy and SymPy expressions. The library is under active development; new helpers are added each cohort.

Install once in your jupyter.ju.se terminal:

```bash
uv pip install git+https://github.com/cenmir/MechanicsKit.git
```

Update later:

```bash
uv pip install --upgrade git+https://github.com/cenmir/MechanicsKit.git
```

Full documentation: <https://python.ju.se/MechanicsKitDocs/>.

#### Labelling a symbolic equation for cross-reference

A common case: a derivation done in sympy (or printed via a MechanicsKit display helper) needs to appear in the PDF as a numbered, cross-referenceable equation, not as an unnumbered block. The Quarto pattern is the same `$$ ... $$ {#eq-name}` syntax used for hand-written equations; the trick is to *print* it from the cell, with `#| output: asis` so Quarto feeds the output back through Pandoc as markdown rather than as literal text.

```python
#| output: asis
#| eval: true

import sympy as sp

t, omega, zeta, K = sp.symbols("t omega zeta K", positive=True)
s = sp.symbols("s")
H_s = K / (s**2 + 2*zeta*omega*s + omega**2)
y_t = sp.simplify(sp.inverse_laplace_transform(H_s / s, s, t))

print(r"$$")
print(sp.latex(y_t))
print(r"$$ {#eq-step-symbolic}")
```

The prose can then refer to the result as `@eq-step-symbolic`, and the rendered PDF carries the equation under an auto-assigned number that Quarto cross-resolves on every render.

The three-print pattern is the workaround that needs no change to MechanicsKit. If you prefer a single call, MechanicsKit's LaTeX-display utility takes a one-line extension: accept an optional `label=` argument and append the `{#label}` attribute after the closing `$$`. That keeps the cell to one line per equation.

"""

p = Path('methodology.ipynb')
nb = json.loads(p.read_text(encoding='utf-8'))

for c in nb['cells']:
    if c.get('id') != 'python-quarto':
        continue
    joined = ''.join(c['source']) if isinstance(c['source'], list) else c['source']
    if ANCHOR not in joined:
        raise SystemExit("anchor heading not found")
    joined = joined.replace(ANCHOR, NEW_SECTION + ANCHOR)
    c['source'] = joined.splitlines(keepends=True)
    print(f"updated python-quarto ({len(c['source'])} lines)")
    break
else:
    raise SystemExit("python-quarto cell not found")

for c in nb['cells']:
    s = c.get('source')
    if isinstance(s, str):
        c['source'] = s.splitlines(keepends=True)

p.write_text(json.dumps(nb, indent=1, ensure_ascii=False), encoding='utf-8')
