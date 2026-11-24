# AI Lesson Builder

Local web app for draft lesson outlines by grade and topic. Offline mode uses a template; optional live mode uses the OpenAI API with OPENAI_API_KEY and OPENAI_MODEL. Never submit student identifiers. Review outputs for accuracy and accessibility.

```bash
pip install -r requirements.txt
python app.py
# Open http://127.0.0.1:8000
python -m pytest -q
```
Independent AI-assisted demonstration. Live AI mode requires separate verification.
