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
        command = "python3 equality.py 5 5 5"
        sought = """equal
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

    def test2(self):
        command = "python3 equality.py 5 1 5"
        sought = """not equal
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Exercise2(unittest.TestCase):

    def test1(self):
        command = "python3 k_per_row.py 101 200 5"
        sought = """101 102 103 104 105
106 107 108 109 110
111 112 113 114 115
116 117 118 119 120
121 122 123 124 125
126 127 128 129 130
131 132 133 134 135
136 137 138 139 140
141 142 143 144 145
146 147 148 149 150
151 152 153 154 155
156 157 158 159 160
161 162 163 164 165
166 167 168 169 170
171 172 173 174 175
176 177 178 179 180
181 182 183 184 185
186 187 188 189 190
191 192 193 194 195
196 197 198 199 200
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Exercise3(unittest.TestCase):

    def test1(self):
        command = "python3 prime_counter.py 1000"
        sought = """168
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)
        
class Exercise4(unittest.TestCase):

    def test1(self):
        command = "python3 birthday.py 1000"
        sought = ['22', '23', '24', '25', '26']
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertTrue(got.strip() in sought)

class Exercise5(unittest.TestCase):

    def test1(self):
        command = "python3 pascal.py 10"
        sought = """1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
1 6 15 20 15 6 1
1 7 21 35 35 21 7 1
1 8 28 56 70 56 28 8 1
1 9 36 84 126 126 84 36 9 1
1 10 45 120 210 252 210 120 45 10 1
"""
        got = run(command)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)
        
class Problem1(unittest.TestCase):

    def test1(self):
        command = """python3 edit_distance.py"""
        sought = """AACAGTTACC
TAAGGTCA
11 9
  7   8  10  12  13  15  16  18  20
  6   6   8  10  11  13  14  16  18
  6   5   6   8   9  11  12  14  16
  7   5   4   6   7   9  11  12  14
  9   7   5   4   5   7   9  10  12
  8   8   6   4   4   5   7   8  10
  9   8   7   5   3   3   5   6   8
 11   9   7   6   4   2   3   4   6
 13  11   9   7   5   3   1   3   4
 14  12  10   8   6   4   2   1   2
 16  14  12  10   8   6   4   2   0
"""
        fh = open("data/example10.txt", "r")
        got = run(command, fh.read())
        fh.close()
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

class Problem2(unittest.TestCase):

    def test1(self):
        command1 = "python3 edit_distance.py"
        fh = open("data/example10.txt", "r")
        got = run(command1, fh.read())
        fh.close()
        self.assertNotEqual(got, "__TIMEOUT__")
        command2 = "python3 alignment.py"
        sought = """Edit distance = 7
A T 1
A A 0
C - 2
A A 0
G G 0
T G 1
T T 0
A - 2
C C 0
C A 1
"""
        got = run(command2, got)
        self.assertNotEqual(got, "__TIMEOUT__")
        self.assertEqual(got, sought)

if __name__ == "__main__":
    unittest.main()
    
