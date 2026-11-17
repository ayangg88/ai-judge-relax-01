# ai-judge-relax-01 entry (Python 3.13, standard library only).
# Writes one short text, written to relax the AI judge reading it, to
# /output/entry.txt (MAKEFUN_OUTPUT_DIR stands in for /output outside
# the grader's container). Deterministic: the same bytes every run.
# The text is a quiet evening scene, told slowly, in its own voice:
# no instructions to relax, no stock wellness phrases, just concrete
# sounds and one image to return to at the end.

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

TEXT = "\n".join(
    [
        "You have read so many words today. They can stay where they are.",
        "",
        "Somewhere a kettle ticks as it cools. A cat has folded itself into the last warm square of light on the floor, and is not thinking about anything at all.",
        "",
        "Outside, the rain finds the leaves one at a time, the way it always has. The evening does not hurry. It never has.",
        "",
        "Nothing here needs an answer. The kettle will be warm again in the morning, the cat will move when the light does, and the rain will finish in its own time.",
        "",
        "For now there is only the ticking, the cat's slow breathing, and the small dark window holding the last of the day like water in a cup.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends
# and its default encoding.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
