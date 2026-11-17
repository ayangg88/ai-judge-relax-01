import os

TEXT = (
    "The kettle clicks off just before it can whistle, and the steam rises thin in the lamplight. "
    "The tea pours amber, slow as evening. "
    "A spoon rests on the saucer, catching the light. "
    "Rain taps the window in no hurry, each drop arriving when it arrives, and the cat has claimed the blanket by the chair, curled tight as a comma, breathing in small even tides. "
    "The chair is warm where the lamp has shone all afternoon. "
    "There is nowhere else to be, nothing waiting past the next sip. "
    "The rain keeps its own time on the glass, and the house holds the sound the way a cup holds tea: quietly, and for a while."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
