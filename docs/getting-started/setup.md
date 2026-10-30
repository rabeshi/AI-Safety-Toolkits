# Set up your computer

You need this setup for Tutorials 2–6. [Tutorial 1](../tutorials/01-offline-refusal.md) and
[Tutorial 5](../tutorials/05-judge-agreement.md) need only Python.

## 1. Install Python and Git

- **Python 3.11 or newer** (Inspect Evals requires 3.11). Download it from [python.org](https://www.python.org/downloads/). On Windows, tick
  *"Add python.exe to PATH"* during installation.
- **Git**, to download this repository: [git-scm.com](https://git-scm.com/downloads).

Check both work by opening a terminal (PowerShell on Windows, Terminal on macOS/Linux):

```bash
python --version
git --version
```

!!! tip "On macOS or Linux"
    If `python` is not found, try `python3` instead, and use `python3` everywhere this guide says `python`.

## 2. Download this repository

```bash
git clone https://github.com/rabeshi/AI-Safety-Toolkits.git
cd AI-Safety-Toolkits
```

## 3. Create a virtual environment

A virtual environment keeps this project's packages separate from the rest of your computer.

=== "Windows (PowerShell)"

    ```powershell
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    ```

    If PowerShell blocks the script, run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then try again.

=== "macOS / Linux"

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

Your prompt should now start with `(.venv)`. Run the activate command again whenever you open a new terminal.

## 4. Install the tutorial packages

```bash
python -m pip install -r examples/requirements.txt
```

This installs [Inspect AI](https://inspect.aisi.org.uk/), an open-source evaluation framework from the UK AI
Security Institute, and [Inspect Evals](https://ukgovernmentbeis.github.io/inspect_evals/), a collection of
ready-made benchmarks.

Check it worked with the built-in **mock model**, which gives fake answers without any account or cost:

```bash
inspect eval examples/02_first_inspect_eval.py --model mockllm/model
```

You should see a results table. The accuracy will be 0 because the mock model doesn't really answer.

## 5. Connect a real model

To test a real model you need an API key from a provider. Keys are secret: treat them like passwords.

=== "OpenAI"

    1. Create a key at [platform.openai.com](https://platform.openai.com/api-keys).
    2. `pip install openai`
    3. Set the key and a default model:

        ```bash
        # macOS / Linux
        export OPENAI_API_KEY=sk-...
        export INSPECT_EVAL_MODEL=openai/gpt-4o-mini
        ```
        ```powershell
        # Windows PowerShell
        $env:OPENAI_API_KEY = "sk-..."
        $env:INSPECT_EVAL_MODEL = "openai/gpt-4o-mini"
        ```

=== "Anthropic"

    1. Create a key at [console.anthropic.com](https://console.anthropic.com/).
    2. `pip install anthropic`
    3. Set `ANTHROPIC_API_KEY` and `INSPECT_EVAL_MODEL=anthropic/<model-name>` the same way.

=== "Free, local (Ollama)"

    1. Install [Ollama](https://ollama.com/) and pull a small model: `ollama pull llama3.2`
    2. `pip install openai` (Inspect talks to Ollama through it)
    3. Set `INSPECT_EVAL_MODEL=ollama/llama3.2`. No key needed; it runs on your computer.

Model names change often. Check the [Inspect providers page](https://inspect.aisi.org.uk/providers.html) for the
current list and exact names.

!!! tip "Keep keys out of Git"
    Instead of typing `export` each time, put the variables in a file named `.env` in the repository folder
    (one `NAME=value` per line). Inspect reads it automatically, and this repository's `.gitignore` stops it
    from being committed.

!!! warning "Costs"
    Real model calls cost money. Always start with `--limit 10` to run just ten examples, and check the
    token count Inspect prints at the end before running more.

## 6. Optional extras

- **Docker Desktop** ([docker.com](https://www.docker.com/products/docker-desktop/)): needed for agent and
  hacking benchmarks that run inside sandboxes, such as Cybench and OSWorld.
- **The `datasets` package** (`pip install datasets`): to download datasets from Hugging Face and look at them
  yourself. Many toolkit pages include a snippet for this.

You're ready. Continue with [Tutorial 2](../tutorials/02-first-inspect-eval.md).
