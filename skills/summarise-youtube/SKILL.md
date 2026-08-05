---
name: summarise-youtube
description: Summarise a YouTube video from its URL, printing the summary in the conversation.
disable-model-invocation: true
---

# Summarise YouTube

Fetch a YouTube video's subtitles with `yt-dlp`, read them, and print a summary in the conversation. The user invokes this as `/summarise-youtube <url>`.

## Process

### 1. Fetch the subtitles

Download the subtitle track to the scratchpad directory, skipping the video itself:

```
yt-dlp --skip-download --write-subs --write-auto-subs --sub-lang en --sub-format vtt \
  --convert-subs vtt -o '<scratchpad>/subs.%(ext)s' '<url>'
```

`--write-auto-subs` covers videos that have only auto-generated captions, so this works whether or not the uploader added their own. The output file lands at `<scratchpad>/subs.en.vtt`.

If no subtitle file is produced, the video has no English captions available. Say so and stop - there is no transcript to summarise, and guessing from the title is not a summary.

### 2. Read the transcript

Read the `.vtt` file. It carries WebVTT timestamp cues and often repeats each line as captions scroll; read past that noise to the spoken content underneath.

### 3. Print the summary

Write the summary straight into the conversation, in two clearly separated sections.

**Summary** - a tone-neutral account of what the video actually says: its main claims, the through-line, and any conclusion it reaches, in enough depth that the user does not need to watch it. Lead with a one-sentence gist, then the substance. Ground it in the transcript; never pad with what the title implies but the words do not support. Report the content, do not judge it.

**Editorial take** - under its own heading so it can never be mistaken for the neutral summary, give your own assessment: how convincing the argument is, where it is one-sided or unsupported, what it leaves out, whether the claims hold up. This is the one place opinion belongs; keep it out of the summary above.

Exclude advertising entirely from both sections. Sponsor reads, ad segments, and product plugs are not part of the video's argument - do not summarise them, quote them, or mention that they occurred.
