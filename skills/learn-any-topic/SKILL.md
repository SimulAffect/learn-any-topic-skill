---
name: learn-any-topic
description: Create source-backed self-study tutorials, learning maps, glossaries, and roadmaps for any topic. Use when the user asks to learn, explain, teach, or build a course on a subject.
---

# Learn Any Topic

## Core Outcome

Create a tutorial that lets the target learner study the topic with minimal extra searching. The result should connect background, concepts, methods, examples, terminology, practice, and review criteria into one coherent learning path.

Use a repeatable workflow: define the learner and deliverable, build an authority-backed source map, write from foundations to applied use, generate the requested artifact, then revise through a concrete review loop.

## Workflow

### 1. Confirm Tutorial Language

Before starting, determine which language the tutorial should be written in. If the user has specified a language or there is sufficient context to infer it confidently, proceed without asking. If ambiguous, ask the user to confirm. Do not default to English simply because this skill is written in English.

### 2. Frame the Learning Job

Identify the topic, target learner, desired depth, output format, and acceptance criteria. Ask only for missing information that would materially change the result. When the user gives enough context, proceed with stated assumptions.

Convert the request into a concrete learning objective:

- what the learner should understand
- what the learner should be able to do
- what terminology they must know
- what examples or exercises would make the knowledge usable
- what final artifact the user expects

### 3. Build the Source Map

Use current sources when the user asks for authority, recent information, standards, products, laws, tools, or source attribution. Prefer primary and recognized sources over generic summaries.

Use this source ladder:

- standards, official documentation, laws, specifications, or institution pages
- textbooks, peer-reviewed papers, university material, or established technical references
- respected field guides, design systems, industry handbooks, or professional organizations
- influential practitioner writing, case studies, and widely cited essays
- community material only as supporting context, not as the backbone

If the field has competing schools of thought, name the disagreement and explain the practical consequence. Separate confirmed facts from inference.

For substantial or source-heavy work, read `references/source-quality.md`.

### 4. Design the Knowledge Map

Before drafting, make a private or visible structure that covers:

- prerequisites and learner assumptions
- root background: why the topic exists and what problem it solves
- core concepts and mental models
- key terms with plain definitions
- standard workflows, formulas, patterns, or decision rules
- examples that move from simple to realistic
- common mistakes, edge cases, and misconceptions
- practice tasks or self-check questions
- final checklist for judging whether the learner has understood the topic
- visual explanations that would reduce confusion, such as a learning roadmap, concept map, process diagram, comparison table, or structured checklist

For a reusable chapter skeleton, read `references/tutorial-framework.md`.

### 5. Write the Tutorial

Write in the confirmed language and match the audience. Prefer continuous explanation over disconnected bullet lists when the goal is a course, tutorial, or self-study text.

Writing rules:

- Define what a thing is before clarifying what it is not.
- Replace broad claims with specific mechanisms. For example, write "reduces memory load by grouping related choices" instead of "makes it better".
- Explain terms when they first appear.
- Move from root causes to principles, then to procedures and examples.
- Use diagrams, tables, or checklists when they reduce confusion, not as decoration.
- Keep citations close enough to support factual claims without turning the tutorial into a source dump.

### 6. Generate the Artifact

For substantial tutorials, learning roadmaps, course outlines, or self-study guides, create both an editable Markdown source file and a PDF reading copy by default. Treat the Markdown file as the source draft and the PDF as the final reading artifact.

If the user explicitly requests inline text only, Markdown only, Word, slides, spreadsheet, or another file type, follow the requested format and use the relevant skill or tool for that format. If PDF generation is unavailable in the current environment, deliver the Markdown source and state the PDF limitation clearly.

For document outputs, include enough structure for navigation: title, short orientation, sections, glossary, practice or review section, and source list. If visual rendering is possible, verify the document visually. If rendering is unavailable, do structural checks and state the limitation.

Carry the planned visual explanations into the final artifact. When image, diagram, PDF, or rendering tools are available, include rendered visuals in the document. When those tools are unavailable, preserve the visuals as editable Mermaid diagrams, tables, SVG source, or clearly labeled figure instructions.

### 7. Review, Find Gaps, Revise

Run at least one review loop for substantial tutorials:

- coverage: does the tutorial answer the promised learning objective
- source quality: are major claims backed by appropriate sources
- learner fit: does the explanation match the learner's background
- terminology: are key terms defined before use
- coherence: does each section prepare the next section
- practice: can the learner test whether they understand the topic
- artifact integrity: no placeholders, broken references, missing files, or unreadable output

When reviewing Markdown or plain text, run:

```bash
python3 scripts/review_tutorial.py path/to/tutorial.md
```

If the script flags issues, revise the tutorial or explain why a flagged phrase is acceptable in context.

## Output Contract

When finishing, report:

- the delivered file or text location
- the source backbone used
- the review checks completed
- any known limitation, such as unavailable visual rendering or unverified live sources
