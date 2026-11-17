# Your first OpenVoiceOS skill

A skill teaches a voice assistant something new. This one is the smallest
there is: say **"hello from my skill"** and it answers. Make it yours, change
the sentences, and watch [Emkay](https://emkay.ai) – OpenVoiceOS in the
browser – answer the new ones a second after you save.

**👉 The friendly guide: <https://dev.emkay.ai>**

## Three ways to start

| | What you need | How |
|---|---|---|
| **In the browser** | nothing | Open [vscode.dev](https://vscode.dev), add the *Emkay Dev* extension, open an empty folder and run **Emkay: New skill** ([the guide](https://dev.emkay.ai)). |
| **GitHub Codespaces** | a GitHub account | **Use this template** → *Create a new repository*, then **Code → Codespaces → Create codespace**. You get VS Code with a text-only OpenVoiceOS and [ovos-tui-client](https://github.com/andlo/ovos-tui-client) running. |
| **On your PC** | VS Code and Docker | Make your repository from the template, clone it and *Reopen in Container* – the same workshop as Codespaces. |

When you make a repository from this template, a small workflow renames
the skill after your repository (`you/coffee-facts` becomes
`ovos-skill-coffee-facts`, skill id `ovos-skill-coffee-facts.you`) and
then removes itself.

## What is in a skill

```
ovos_skill_hello/
  __init__.py              the code: what happens when an intent is heard
  locale/
    en-US/
      hello.intent         the sentences you can say, one per line
      hello.dialog         what the skill answers (one line is picked)
      skill.json           name, description and examples, for the skill store
    da-DK/ de-DE/ …        the same in Danish, German, … – all twelve of Emkay's
                           languages; add any language as a folder
test/end2end/
  golden_utterances_<lang>.jsonl  sentences that must reach this skill, per language
tests/test_skill.py        quick checks (pytest)
pyproject.toml             the package: name, dependencies, the skill id
```

## Try it

- **Emkay Dev (VS Code):** *Emkay: Run the skill in Emkay* (Ctrl+Alt+E) opens
  Emkay next to your code and loads the skill; type under Emkay to talk to
  it. Every save loads it again. *Emkay: Test the skill* sends the golden
  utterances and shows ✓ / ✗ in the Testing view.
- **ovos-tui-client (Codespaces, Dev Container):** run `ovos-tui` in the
  terminal, type to talk, `Ctrl+P` → *Test* runs the same golden
  utterances against a full OpenVoiceOS. After changing the skill:
  `bash .devcontainer/ovos.sh restart`.
- **pytest:** `pytest -q` – no OpenVoiceOS needed.

The golden utterances are judged by
[ovos-routing-judge](https://pypi.org/project/ovos-routing-judge/) in
all three places, so a sentence that passes in Emkay passes in
ovos-tui-client and in the [Emkay store](https://store.emkay.ai)'s
checks too.

## When it works

Push it to GitHub and publish it on PyPI (`python -m build`, `twine upload`)
– then anyone can install it on their OpenVoiceOS, and it can be listed in
the [Emkay store](https://store.emkay.ai). More on writing skills:
[the OpenVoiceOS technical manual](https://openvoiceos.github.io/ovos-technical-manual/).
