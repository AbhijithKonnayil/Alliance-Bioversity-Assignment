# Task 3 — Mock Transcription & Follow-up Question Generator

This module provides a tiny, deterministic mock transcription generator and a simple rule-based follow-up questions.

Files
- `main.py` — Contains `generate_mock_transcription()` and `generate_follow_up_questions()`.
- `rules.py` — Rule set used to map keywords to follow-up questions.
- `mock_audio.py` — File containing sample question text used as "mock audio" transcriptions.

Usage examples

From the project root, run Python interactively:

```bash
python main.py yellow
```

Output

```

Transcription: The paddy leaves are turning yellow in some patches. I also noticed a few insects on the lower leaves. Water level is normal. What should I do?

Follow-up Questions:
1: Are the yellow leaves at the bottom or top of the plant?
2: Did you apply fertilizer recently?

```