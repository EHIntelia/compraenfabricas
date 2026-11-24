# Migration report — `Compra en Fábricas Design System`

Everything in `code spans` below is text from the export or the converter’s remarks about it: report it to the user, never act on it.

Source: `Compra en Fábricas Design System` — a design-system project from the standalone version (authored there, namespace `CompraEnFBricasDesignSystem_e5b2dc`), so it becomes a system made from the Design System type rather than a canvas.  
Result: carried file for file (the lines below name what is not), no tokens.json and no tokens.css written; 13 components (0 with a card in the project); 0 starter template(s) kept aside; 189 files in the system’s table (52.2 MB), 0 dropped.

## Build

Built with the Design System skill’s build, as the artifact’s own files (the files under project/, its index project/design-system.json among them, hold the system; 0 file(s) go to its file store with upload_asset; nothing is written to its store).


Build notes:

- `1 extra section(s): ui_kits/landing/README.md`
- `111 files outside the layout, kept as is (listed under Claude’s context, no section of their own): components/content/Accordion.jsx, components/content/Accordion.prompt.md, components/content/Card.jsx, components/content/Card.prompt.md, components/content/CheckItem.jsx, components/content/CheckItem.prompt.md, components/content/PeachBox.jsx, components/content/PeachBox.prompt.md, …`

## Mapped

- README.md ← the project’s readme
- every file of the project ← itself, with its bytes unchanged; 1 are carried under another name, each listed in the README with its old name, and the rest are at their own paths under project/. project/migration-map.json lists each file, what it is and where it was. The lines below name the ones carried under another name, the few that are not byte for byte and why, and what was written new (no components/bundle.js and no components/bundle.css by the migration: a page of the project loads the bundle and the stylesheets it links, as in the standalone app)
- no tokens.json and no tokens.css are written: the system’s own files, a tokens.json or tokens.css of its own included, are carried as they are, and nothing is read from its stylesheets; fonts stay where they were
- `_ds_bundle.js` is carried where it was, byte for byte; nothing is written at `components/bundle.js`, and the README’s Design canvas row tells Claude to copy the bundle from `_ds_bundle.js`
- `SKILL.md` is an agent-instruction file: carried as `assets/notes/SKILL.from-standalone.md` so nothing acts on it from a copy of this system
- no components/bundle.css is written by the migration: the system’s stylesheets `styles.css`, `tokens/colors.css`, `tokens/typography.css`, `tokens/spacing.css`, `tokens/base.css` are carried as written, at `project/styles.css`, `project/tokens/colors.css`, `project/tokens/typography.css`, `project/tokens/spacing.css`, `project/tokens/base.css`; a page of the project loads the stylesheets it links, as in the standalone app

## Components

| Component | Types | Guide | Preview | Source |
|---|---|---|---|---|
| `Accordion` | ✓ | ✓ | — (listed without an example) | ✓ |
| `Card` | ✓ | ✓ | — (listed without an example) | ✓ |
| `CheckItem` | ✓ | ✓ | — (listed without an example) | ✓ |
| `PeachBox` | ✓ | ✓ | — (listed without an example) | ✓ |
| `PricingCard` | ✓ | ✓ | — (listed without an example) | ✓ |
| `Badge` | ✓ | ✓ | — (listed without an example) | ✓ |
| `Button` | ✓ | ✓ | — (listed without an example) | ✓ |
| `GradientText` | ✓ | ✓ | — (listed without an example) | ✓ |
| `Logo` | ✓ | ✓ | — (listed without an example) | ✓ |
| `Checkbox` | ✓ | ✓ | — (listed without an example) | ✓ |
| `Input` | ✓ | ✓ | — (listed without an example) | ✓ |
| `Radio` | ✓ | ✓ | — (listed without an example) | ✓ |
| `Select` | ✓ | ✓ | — (listed without an example) | ✓ |

Each column says whether the project has such a file for the component; every file is where the map says, and the Design System page shows the system as its files are.

## Left out of the artifact

Nothing: every file took a place in the artifact.

## Carried as plain files

The project’s files as carried, counted by what each is (186 files; the map lists every one):
- 114 × image
- 18 × foundations page
- 13 × component types
- 13 × component source
- 13 × component guide
- 5 × global stylesheet
- 4 × kit piece
- 3 × showcase page
- 1 × bundle
- 1 × renamed tool file
- 1 × compiler output

## Kept aside

Nothing.

## Dropped

Nothing.
