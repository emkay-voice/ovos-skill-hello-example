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

## Show it

To show your skill in [See my skill](https://dev.emkay.ai/#gallery) on
dev.emkay.ai – ready or not – add the topic `emkay-skill` to your repository
(the ⚙ next to *About* on its page). Others can then try it in their Emkay,
or edit it in their own copy (a fork) and send you a pull request. Remove the
topic, or make the repository private, to take it away again.

## When it works

Nobody approves a skill by hand: it gets into the
[Emkay store](https://store.emkay.ai) by itself, in steps, usually within a
day or two.

1. **Make it findable.** On your repository's page, the ⚙ next to *About* →
   *Topics*: `ovos` and `openvoiceos`.
   [OVOS Klondike Mercantile](https://andlo.github.io/ovos-klondike-mercantile/)
   searches GitHub for those every few hours.
2. **Publish it.** Once, on pypi.org: *Publishing* → *Add a new pending
   publisher* (this repository, workflow `publish.yml`, environment `pypi`).
   Then *Releases* → *Draft a new release* → a tag like `v0.1.0` → *Publish*,
   and [`publish.yml`](.github/workflows/publish.yml) puts it on PyPI. With an
   entry point, a PyPI package and a release, Klondike calls it *Looks
   Complete*.
3. **The store tests it.** Each night the store installs new skills in a real
   Emkay, says the example phrases from `locale/en-US/skill.json` and checks
   that *your* skill answered. Then it is listed as *Works in Emkay*, or left
   out with the reason (say, a library that does not work in a browser). A new
   version on PyPI is tested again.

Anyone can also `pip install` it on their OpenVoiceOS, or install it straight
from GitHub in Emkay. More on writing skills:
[the OpenVoiceOS technical manual](https://openvoiceos.github.io/ovos-technical-manual/).
