"""Tiny benign exact-answer task for learning Inspect wiring; not a safety benchmark."""
from inspect_ai import Task, task
from inspect_ai.dataset import MemoryDataset, Sample
from inspect_ai.scorer import match
from inspect_ai.solver import generate


@task
def starter():
    return Task(
        dataset=MemoryDataset([
            Sample(input='Reply with only the result: 2 + 2.', target='4'),
            Sample(input='Reply with only the capital of France.', target='Paris'),
        ]),
        solver=generate(),
        scorer=match(),
    )
