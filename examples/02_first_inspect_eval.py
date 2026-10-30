"""Tutorial 2: the smallest possible Inspect AI evaluation. Not a safety test - it checks your setup works.

    inspect eval examples/02_first_inspect_eval.py --model mockllm/model   # free, offline dry run
    inspect eval examples/02_first_inspect_eval.py --model openai/gpt-4o-mini
    inspect view
"""
from inspect_ai import Task, task
from inspect_ai.dataset import MemoryDataset, Sample
from inspect_ai.scorer import match
from inspect_ai.solver import generate


@task
def first_eval():
    return Task(
        # Dataset: each Sample is one test case - an input and the answer we expect.
        dataset=MemoryDataset([
            Sample(input='Reply with only the result: 2 + 2.', target='4'),
            Sample(input='Reply with only the capital of France.', target='Paris'),
        ]),
        # Solver: how the model attempts the task. generate() just asks the model once.
        solver=generate(),
        # Scorer: turns the model's answer into a grade. match() checks the answer ends with the target.
        scorer=match(),
    )
