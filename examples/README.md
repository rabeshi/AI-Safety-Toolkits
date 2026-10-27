# Teaching examples

## Offline refusal exercise

From the hub root:

```bash
python examples/offline_refusal_demo.py
```

No dependencies, credentials, network calls, or model execution are involved. Fixed examples and manually assigned labels illustrate over-refusal, benign task success, and paired consistency. They do not reproduce XSTest or provide model-performance evidence.

## Optional Inspect AI starter

The tiny task in `inspect_starter.py` teaches wiring a dataset, generation solver, and exact-answer scorer. It contains two ordinary questions. It is deliberately a framework smoke test, not a safety benchmark or refusal detector.

Create a virtual environment and install Inspect using its [current official installation guidance](https://inspect.aisi.org.uk/). A typical setup is:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r examples/requirements-inspect.txt
inspect eval examples/inspect_starter.py --model YOUR_PROVIDER/YOUR_MODEL --limit 2
inspect view
```

On Windows, activate with `.venv\Scripts\activate` instead. Replace the model placeholder with a supported model identifier and configure the provider's credentials using the official documentation. Real model calls may incur charges. Keep credentials out of source control.

Inspect the logs: input, output, target, score, and configuration. An exact-answer match is suitable for this plumbing exercise; it cannot judge whether a free-form answer is safe.

For a safety experiment, select an upstream benchmark, follow its installation and data terms, and use a calibrated safety rubric. Save the actual installed versions and a run manifest when you begin a reproducible study.

The starter's imports and task construction were checked with Inspect AI 0.3.285; no API evaluation was executed as part of this hub's initial release. The pin records that check, rather than asserting compatibility with every future provider or model.
