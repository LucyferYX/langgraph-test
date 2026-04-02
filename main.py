import json
import sys

from pipeline.pipeline import run_pipeline


def main():

    input_path = sys.argv[1]

    with open(input_path) as f:
        pr = json.load(f)

    result = run_pipeline(pr)

    with open("output/change_doc.json", "w") as f:
        json.dump(result, f, indent=2)

    print("Change documentation generated")


if __name__ == "__main__":
    main()