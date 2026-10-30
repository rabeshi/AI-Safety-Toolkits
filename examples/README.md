# Tutorial code

Each file goes with a step-by-step tutorial on the website (`docs/tutorials/`). Run everything from the
repository root.

| File | Tutorial | Needs |
| --- | --- | --- |
| `01_offline_refusal_demo.py` | [Score an evaluation by hand](../docs/tutorials/01-offline-refusal.md) | Python only |
| `02_first_inspect_eval.py` | [Your first Inspect eval](../docs/tutorials/02-first-inspect-eval.md) | `requirements.txt` |
| — | [Run a real benchmark](../docs/tutorials/03-run-a-benchmark.md) | `requirements.txt` + API key |
| `04_refusal_eval.py` + `data/refusal_prompts.csv` | [Build a refusal eval with a judge](../docs/tutorials/04-build-a-refusal-eval.md) | `requirements.txt` + API key |
| `05_judge_agreement.py` | [Check your judge](../docs/tutorials/05-judge-agreement.md) | Python only |
| `06_prompt_injection.py` | [Test an agent for prompt injection](../docs/tutorials/06-prompt-injection.md) | `requirements.txt` + API key |

```bash
python -m pip install -r examples/requirements.txt   # Python 3.11+
inspect eval examples/04_refusal_eval.py --model mockllm/model   # free offline wiring check
```

All datasets and outputs here are small and hand-written for teaching. They are not benchmarks and say nothing
about any real model.
