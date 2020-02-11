import os

from dotenv import load_dotenv


if __name__ == "__main__":
    load_dotenv(verbose=True)
    print(os.getenv("CI_URL"))
    print(os.getenv("CI_USERNAME"))
    print(os.getenv("CI_TOKEN"))
    print(os.getenv("GIT_PAT"))
