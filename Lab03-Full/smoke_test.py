import os

from app import main


if __name__ == "__main__":
    os.environ["DRY_RUN"] = "1"
    main()
    print("Smoke test OK: app avviata in modalita DRY_RUN.")

