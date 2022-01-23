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
        command = "python3 sin.py 60"
        sought = """0.8660254037844385
0.8660254037844386
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Exercise2(unittest.TestCase):

    def test1(self):
        command = "python3 distance.py 5"
        sought = """13.0
"""
        got = run(command, "-9 1 10 -1 1 -5 9 6 7 4")
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Exercise3(unittest.TestCase):

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

class Exercise4(unittest.TestCase):

    def test1(self):
        command = "python3 reverse.py"
        sought = """question the is that be to not or be to
"""
        got = run(command, "to be or not to be that is the question")
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)
        
class Exercise5(unittest.TestCase):

    def test1(self):
        command = "python3 transpose.py"
        sought = """1.0 4.0
2.0 5.0
3.0 6.0
"""
        got = run(command, "2 3 1 2 3 4 5 6")
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Problem1(unittest.TestCase):

    def test1(self):
        command = "python3 ring_buffer.py 10"
        sought = """Size after wrap-around is 10
55
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)
    
    def test2(self):
        command = "python3 ring_buffer.py 100"
        sought = """Size after wrap-around is 100
5050
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Problem2(unittest.TestCase):

    def test1(self):
        command = "python3 guitar_string.py 25"
        sought = """     0   0.2000
     1   0.4000
     2   0.5000
     3   0.3000
     4  -0.2000
     5   0.4000
     6   0.3000
     7   0.0000
     8  -0.1000
     9  -0.3000
    10   0.2988
    11   0.4482
    12   0.3984
    13   0.0498
    14   0.0996
    15   0.3486
    16   0.1494
    17  -0.0498
    18  -0.1992
    19  -0.0006
    20   0.3720
    21   0.4216
    22   0.2232
    23   0.0744
    24   0.2232
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

if __name__ == "__main__":
    unittest.main()
