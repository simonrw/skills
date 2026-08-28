---
name: make-note
description: When performing a research task, or using the openspec-explore skill, take a note in my personal notion notebook. Or when asked to continue an investigation from a personal note
---

# Take research notes

I will quite often use AI and agents to explore or research a topic. I want all previous research tasks, logs, and notes captured in a central place so that I can refer back to them later without having to open up the agentic session.

## Notebook location

Use the notion connector/mcp to create a new note in my Notion "Personal notebook". If the user doesn't specify where this notebook is, ask them for a link.

## Notebook structure

Each new research note should be added as a page in the Notion database. The title should be descriptive but brief of the topic. 

Add a very concise summary to the summary field. Find or create relevant succinct tags that match the content. Include the original prompt that triggered the research in the original brief field.  

If you find notes existing that also seem to relate to the same topic, include a link in the "maybe related?" relation. 

## Continued conversation

If the user wants to continue a conversation from a linked personal note, then continue the research that the user asked for, but append new findings to the same research note. Indicate that this came from a separate session by embedding the prompt in a call-out block at the top of a new section. 
