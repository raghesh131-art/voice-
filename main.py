from speech import get_voice_input
from translator import text_to_code
from executor import run_code

def main():
    command = get_voice_input()

    if command:
        code = text_to_code(command)
        run_code(code)

if __name__ == "__main__":
    main()