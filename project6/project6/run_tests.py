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

class Problem1(unittest.TestCase):

    def test1(self):
        command = "python3 nearest_insertion.py"
        sought = """(110.0, 225.0)
(161.0, 280.0)
(157.0, 443.0)
(283.0, 379.0)
(306.0, 360.0)
(325.0, 554.0)
(397.0, 566.0)
(490.0, 285.0)
(552.0, 199.0)
(343.0, 110.0)
Tour distance = 1566.136305
Number of points = 10
"""
        fh = open("data/tsp10.txt", "r")
        got = run(command, fh.read())
        fh.close()
        got = got[85:]
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

    def test2(self):
        command = "python3 smallest_insertion.py"
        sought = """(110.0, 225.0)
(283.0, 379.0)
(306.0, 360.0)
(343.0, 110.0)
(552.0, 199.0)
(490.0, 285.0)
(397.0, 566.0)
(325.0, 554.0)
(157.0, 443.0)
(161.0, 280.0)
Tour distance = 1655.746186
Number of points = 10
"""
        fh = open("data/tsp10.txt", "r")
        got = run(command, fh.read())
        fh.close()
        got = got[85:]
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

    def test3(self):
        command = "python3 nearest_insertion.py"
        sought = """(211.9338, 223.0796)
(130.9518, 202.2638)
(53.7277, 276.0534)
(10.0, 346.6937)
(24.32, 366.198)
(56.6928, 367.5756)
(99.5465, 367.5969)
(86.7809, 336.4725)
(509.4693, 426.8362)
(578.7719, 403.2444)
(512.0536, 520.2136)
(523.4022, 491.6742)
(457.7327, 520.4371)
(428.4436, 526.3642)
(416.6955, 512.8015)
(394.4477, 513.852)
(330.164, 499.7318)
(371.5071, 590.0)
Tour distance = 7389.929676
Number of points = 100
"""
        fh = open("data/tsp100.txt", "r")
        got = run(command, fh.read())
        fh.close()
        got = got[85:]
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertTrue(got.endswith(sought))

    def test4(self):
        command = "python3 smallest_insertion.py"
        sought = """(87.0681, 286.3926)
(86.7809, 336.4725)
(56.6928, 367.5756)
(24.32, 366.198)
(10.0, 346.6937)
(53.7277, 276.0534)
(58.4656, 232.0548)
(54.483, 231.6509)
(58.8089, 181.2302)
(97.2369, 149.8287)
(130.9518, 202.2638)
(211.9338, 223.0796)
(195.8223, 110.9538)
(195.4291, 96.0121)
(171.4522, 31.8651)
(233.4325, 74.1015)
(266.8353, 10.0)
(276.8106, 51.5341)
Tour distance = 4887.219040
Number of points = 100
"""
        fh = open("data/tsp100.txt", "r")
        got = run(command, fh.read())
        fh.close()
        got = got[85:]
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertTrue(got.endswith(sought))
        
if __name__ == "__main__":
    unittest.main()
    
