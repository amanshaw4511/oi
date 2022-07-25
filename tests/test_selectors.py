import os
import subprocess
import unittest


def system(command: str) -> str:
    cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    output = cmd.stdout.read().decode()
    cmd.kill()
    cmd.stdout.close()
    return output


def run(query: str) -> str:
    main_py = os.path.join(os.path.split(__file__)[0], "..", "main.py")
    return system(f"python3 {main_py} {query}")


class TestSelectors(unittest.TestCase):
    def test_basic_selector(self):
        out = run("capital of india")
        self.assertTrue("new delhi" in out.strip().lower())

    def test_math_selector(self):
        out = run("2 + 99")
        self.assertTrue("101" in out.strip())

    def test_currency_selector(self):
        out = run("dollar to inr")
        self.assertTrue("indian rupee" in out.strip().lower())
