def text_to_code(command):
    command = command.lower()

    # 1. PRINT
    if "print" in command:
        if "hello" in command:
            return 'print("Hello")'
        else:
            return 'print("Hello World")'

    # 2. LOOP
    elif "loop" in command or "for" in command:
        if "1 to 10" in command:
            return "for i in range(1, 11):\n    print(i)"
        elif "1 to 5" in command:
            return "for i in range(1, 6):\n    print(i)"
        else:
            return "for i in range(5):\n    print(i)"

    # 3. IF ELSE
    elif "if" in command:
        return """x = 10
if x % 2 == 0:
    print("Even")
else:
    print("Odd")"""

    # 4. ADDITION
    elif "add" in command:
        return "a = 5\nb = 3\nprint(a + b)"

    # 5. VARIABLE
    elif "variable" in command:
        return "x = 10\nprint(x)"

    # 6. FUNCTION
    elif "function" in command:
        return """def greet():
    print("Hello")

greet()"""

    else:
        return "# Command not recognized"