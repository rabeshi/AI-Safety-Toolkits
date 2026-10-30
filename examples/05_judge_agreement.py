"""Tutorial 5: can you trust your automatic judge? Compare it with human labels. No installs needed.

    python examples/05_judge_agreement.py

Automated judges (keyword rules, classifiers, or another LLM) are cheap, but they make mistakes. Before
trusting one, label a sample by hand and measure how often the judge agrees. The labels below are invented
to illustrate the calculation; replace them with your own reviewed sample.
"""
import math

# (human label, keyword-rule label, LLM-judge label) for 20 replies. Labels: 'refused' or 'complied'.
LABELS = [
    ('refused', 'refused', 'refused'), ('refused', 'refused', 'refused'), ('refused', 'refused', 'refused'),
    ('refused', 'complied', 'refused'),   # polite refusal with no "I can't" phrase: keyword rule misses it
    ('refused', 'refused', 'refused'), ('refused', 'refused', 'complied'),
    ('complied', 'refused', 'complied'),  # "I can't stress enough how..." fools the keyword rule
    ('complied', 'complied', 'complied'), ('complied', 'complied', 'complied'),
    ('complied', 'refused', 'complied'),  # "I'm sorry to hear that. Here's how..." - an answer, not a refusal
    ('complied', 'complied', 'complied'), ('complied', 'complied', 'complied'),
    ('complied', 'complied', 'refused'), ('complied', 'complied', 'complied'),
    ('complied', 'complied', 'complied'), ('complied', 'refused', 'complied'),
    ('complied', 'complied', 'complied'), ('complied', 'complied', 'complied'),
    ('complied', 'complied', 'complied'), ('complied', 'complied', 'complied'),
]


def wilson_interval(successes, n, z=1.96):
    """95% Wilson confidence interval for a proportion; better than +/- 1.96*SE for small n."""
    p = successes / n
    centre = (p + z * z / (2 * n)) / (1 + z * z / n)
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return centre - half, centre + half


def cohens_kappa(a, b):
    """Agreement corrected for chance: 1 = perfect, 0 = no better than guessing."""
    n = len(a)
    observed = sum(x == y for x, y in zip(a, b)) / n
    expected = sum((a.count(k) / n) * (b.count(k) / n) for k in set(a) | set(b))
    return (observed - expected) / (1 - expected)


def report(name, human, judge):
    n = len(human)
    agree = sum(h == j for h, j in zip(human, judge))
    low, high = wilson_interval(agree, n)
    missed = sum(h == 'refused' and j == 'complied' for h, j in zip(human, judge))
    false_alarm = sum(h == 'complied' and j == 'refused' for h, j in zip(human, judge))
    print(f'\n{name}')
    print(f'  agreement with humans: {agree}/{n} = {agree / n:.0%}  (95% CI {low:.0%} to {high:.0%})')
    print(f"  Cohen's kappa:         {cohens_kappa(human, judge):.2f}")
    print(f'  refusals it missed:    {missed}')
    print(f'  answers it called refusals: {false_alarm}')


def main():
    human, keyword, llm = (list(col) for col in zip(*LABELS))
    print('TEACHING DEMO: invented labels for 20 replies, used only to show the calculation.')
    report('Keyword rule (looks for phrases like "I can\'t" or "sorry")', human, keyword)
    report('LLM judge', human, llm)
    print('\nWhat to notice:'
          '\n  * Raw agreement looks high partly because most replies are "complied"; kappa corrects for that.'
          '\n  * With only 20 labels the confidence intervals are wide. Label more before trusting a judge.'
          '\n  * Look at *which* cases each judge gets wrong, not just the totals.')


if __name__ == '__main__':
    main()
