# long-range-ugv-nav-literature-review

HW and then, in perspective, paper about UGV long range backtracking in Unstructured Environment

## Plan

- [x] Move in Docker with LaTeX compiler
- [X] Select the theme and compile the sample paper
- [x] Add task relevant materials for this Assignment
- [+] Add the Rubrics for the paper with short annoattions and ToDos
- [+] Move in Bibliography from the PhD proposal
- [x] (+/-) Move in the ZoomCalibration research paper draft materials;
      Note: has incompatible config with the current project, Fix Later.
- [x] Add specific papers for the Literature Review.
- [ ] Move in relevant MeROS diagrams from the current project and other available images
- [ ] Launch the Snowballing tool to find more relevant papers (or at least try to do it) -- postponed
- [ ] Start the assignment draft iterations and note them here


## Information

- **README.md**: this file.

## To compile use PDF-LaTeX + Biber + PDF-LaTeX + PDF-LaTeX
![Current compilation interface](image.png)

```bash

## [Draft document composition and content](readmes/structure.md)

## Paper LaTeX structure:
`/examples/<LaTeX projetc name>` -- example projects for experiments and testing.

**[readmes/LaTeX_Workbench.md](readmes/LaTeX_Workbench.md)**:
# original guide on VSCode-based local LaTeX workbench.
# (Now all handled by the `.devcontainer` folder, so this is for additional info only.)


## Devcontainer setup:
- **.devcontainer/Dockerfile**: # Dockerfile for the local LaTeX toolbox.
- **.devcontainer/devcontainer.json**: # smooth integration into vscode devcontainer.

## Compilation
### Manual Compilation
```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

### Compile with Latexmk (TODO)
```bash
```
### For local compilation settings meanwhile see the `.vscode/settings.json` : `"latex-workshop.latex.recipes"` and other other parameter nearby for the compilation recipes.
