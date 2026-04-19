def run_code(code):
    print("\n🧾 Generated Code:\n")
    print(code)

    print("\n▶️ Output:\n")
    try:
        exec(code)
    except Exception as e:
        print("❌ Error:", e)