from functions.run_python_file import run_python_file


def run_tests():
    print("run_python_file(\"calculator\", \"main.py\")")
    print(run_python_file("calculator", "main.py"))
    print()

    print('run_python_file("calculator", "tests.py")')
    print(run_python_file("calculator", "tests.py"))
    print()

    print('run_python_file("calculator", "../main.py")')
    print(run_python_file("calculator", "../main.py"))
    print()

    print('write_file("calculator", "/tmp/temp.txt", "this should not be allowed")')
    print(run_python_file("calculator", "nonexistent.py"))
    print()


if __name__ == "__main__":
    run_tests()