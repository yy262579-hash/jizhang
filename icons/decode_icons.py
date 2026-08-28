from pathlib import Path
import base64

OUT = Path(__file__).resolve().parent


def main():
    files = list(OUT.glob("*.b64"))
    if not files:
        raise SystemExit("no .b64 icon files")
    for blob in files:
        name = blob.name[:-4]
        (OUT / name).write_bytes(base64.b64decode(blob.read_text(encoding="ascii")))
        print("wrote", name)


if __name__ == "__main__":
    main()
