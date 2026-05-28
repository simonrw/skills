---
name: improve-writing
description: When the user wants to draft some written prose, like a technical document or a slack message, or email. This skill improves the quality of the users writing.
---

# Improve Writing

A path to higher quality written output.

## Guidance

- **Formal, neutral and professional language:** Avoid colorful or figurative language. We are writing docs that are intended to be dry and concise. There is no need to make them exciting. Avoid colloquialisms.
- **Avoid dashes and (semi)colons** Use direct and active language that avoids the need for dashes or (semi) colons. Avoid paratactic style, asyndetic construction, parenthetical construction and appositive construction.
- **Colons after list elements** If a list item has emphasised 'header' word(s) use a colon afterwards not a period. Take this list as an example.
- **Avoid bullet pointed lists:** Only use bullet pointed lists when they actually make sense and you are enumerating elements of a set. Do not use them as a general mechanism to structure text that can also be structured as paragraphs.
- **Use emphasis intentionally:** Use emphasis (bold, italic) to guide the reader through the doc. Emphasised text provides the reader with anchors when quickly glancing over a page. They serve an important role in navigation and overview.
- **Plain words first:** Use simple words and language unless a specific technical term is more precise and that precision is actually meaningful in the context. E.g. use *Send* instead of *dispatch* unless dispatch carries information the simpler verb does not.
- **No decoration:** Omit decorative language that does not add relevant meaning. Examples for this are words like *orchestration*, *pipeline*, *synergy*, *first-class*, *platform-grade*, etc...
- **Use technical vocabulary precisely, not as flair:** *Contract*, *boundary*, *observer*, *layer*, *primitive*, *interface* each carry a specific engineering meaning. Use them only when you mean exactly that. If a plainer word fits, prefer the plainer word.
- **No techno babble:** Avoid any cool sounding words just for the purpose of adding color. If a specific term carries meaning that can not be expressed otherwise/in a simple way, use it, but omit otherwise.
- **Stable terms:** Once a doc has introduced a name for a thing, do not switch to a synonym later. Either use the defined term or the plainest possible alternative — never a third invented synonym in the same doc.
- **Active voice, entity-first:** *The subscription emits an event when its plan changes* beats *An event is emitted by the system upon subscription plan change events.* Lead with the thing that acts.
- **No hedging in factual statements:** *Might*, *could*, *generally*, *typically* — if something is uncertain, it belongs in Open Questions or marked as such. If it is fact, state it directly.
- **Sections only where appropriate:** Use sections `---` only when areas of text are disjoint. Do not use them as a structuring mechanism where simple headers could be used instead.
- **Precision:** Precision is of utmost importance. If a concrete name is used, expecially when using it with code decoration (`examble`) then this name must exactly match the source code. Simplifications are not allowed, becuase if the name changes then it does not identify that concrete element anymore.
