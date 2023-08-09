#!/usr/bin/python3
import subprocess

def main():
    # Run 'git add .' command
    subprocess.run(['git', 'add', '.'])

    # Request commit message from user
    commit_message = input("Enter commit message: ")

    # Run 'git commit' command with the provided commit message
    subprocess.run(['git', 'commit', '-m', commit_message])

    # Run 'git push' command
    subprocess.run(['git', 'push'])

if __name__ == "__main__":
    main()
