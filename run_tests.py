import datetime, os, signal, subprocess, sys, time, unittest

def run(command, stdin = None, timeout = 30):
    """
    Runs the specified command using specified standard input (if any) and
    returns the output on success. If the command doesn't return within the
    specified time (in seconds), "__TIMEOUT__" is returned.
    """

    start = datetime.datetime.now()
    process = subprocess.Popen(command.split(),
                               stdin = subprocess.PIPE, 
                               stdout = subprocess.PIPE,
                               stderr = subprocess.STDOUT)
    if not stdin is None:
        process.stdin.write(bytes(stdin, 'utf-8'))
    process.stdin.close()
    while process.poll() is None:
        time.sleep(0.1)
        now = datetime.datetime.now()
        if (now - start).seconds > timeout:
            os.kill(process.pid, signal.SIGKILL)
            os.waitpid(-1, os.WNOHANG)
            return "__TIMEOUT__"
    result = process.stdout.read().decode("utf-8")
    process.stdout.close()
    return result

class Exercise1(unittest.TestCase):

    def test1(self):
        command = "python3 sum_of_ints.py 100"
        sought = """5050
5050
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Exercise2(unittest.TestCase):

    def test1(self):
        command = "python3 bits.py 1010010010011110001011111"
        sought = """zeros = 11, ones = 14, total = 25
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Exercise3(unittest.TestCase):

    def test1(self):
        command = "python3 reverse.py bolton"
        sought = """notlob
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

    def test2(self):
        command = "python3 reverse.py amanaplanacanalpanama"
        sought = """amanaplanacanalpanama
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Exercise4(unittest.TestCase):

    def test1(self):
        command = "python3 palindrome.py bolton"
        sought = """False
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)
        
    def test2(self):
        command = "python3 palindrome.py amanaplanacanalpanama"
        sought = """True
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)
        
class Exercise5(unittest.TestCase):

    def test1(self):
        command = "python3 rational.py 100"
        sought = """3.1315929035585515
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)
        
class Problem1(unittest.TestCase):

    def test1(self):
        command = "python3 blob_finder.py 25 180.0 data/run_1/frame00000.jpg"
        sought = """7 Beads:
37 (220.0270, 122.8919)
36 (297.8333, 394.5000)
39 (312.3077, 215.8205)
31 (433.7742, 375.4839)
32 (475.5000, 44.5000)
31 (525.2903, 443.2903)
35 (632.7714, 154.5714)
13 Blobs:
37 (220.0270, 122.8919)
1 (254.0000, 223.0000)
17 (255.4118, 233.8824)
23 (265.8261, 316.4348)
36 (297.8333, 394.5000)
39 (312.3077, 215.8205)
23 (373.0000, 357.1739)
19 (390.8421, 144.8421)
31 (433.7742, 375.4839)
32 (475.5000, 44.5000)
31 (525.2903, 443.2903)
24 (591.0000, 399.5000)
35 (632.7714, 154.5714)
"""
        got = run(command)
        got = got[85:]
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Problem2(unittest.TestCase):

    def test1(self):
        command = "python3 bead_tracker.py 25 180.0 25.0 data/run_1/%s" \
                  %(" data/run_1/".join(sorted(os.listdir("data/run_1"))[:2]))
        sought = """7.1833
4.7932
2.1693
5.5287
5.4292
4.3962

"""
        got = run(command)
        got = got[85:]
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Problem3(unittest.TestCase):

    def test1(self):
        command1 = "python3 bead_tracker.py 25 180.0 25.0 data/run_1/%s" %(" data/run_1/".join(sorted(os.listdir("data/run_1"))[:2]))
        got = run(command1)
        got = got[85:]
        command2 = "python3 avogadro.py"
        got = run(command2, got)
        sought = """Boltzman = 1.173701e-23
Avogadro = 7.084062e+23
"""
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

if __name__ == "__main__":
    unittest.main()
