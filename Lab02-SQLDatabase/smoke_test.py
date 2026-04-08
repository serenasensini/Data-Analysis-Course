import os

from app import main


if __name__ == "__main__":
    os.environ["DRY_RUN"] = "1"
    main()
    print("Smoke test passed: scaffold runs in DRY_RUN mode.")

