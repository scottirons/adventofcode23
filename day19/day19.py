from collections import defaultdict
INDEX_KEY = {
    "x": 0,
    "m": 1,
    "a": 2,
    "s": 3
}


class Solution:
    def __init__(self, source):
        self.wf = defaultdict(list)
        self.parts = []
        self.parse_input(source)
        self.r = []
        self.a = []

    def parse_input(self, source):
        with open(source, 'r') as f:
            lines = f.read().split('\n\n')
        wf = lines[0].split('\n')
        parts = lines[1].split('\n')
        for f in wf:
            key, rest = f[:-1].split('{')
            ins = rest.split(',')
            for i in ins:
                if ':' in i:
                    op, dest = i.split(':')
                    k = INDEX_KEY[op[0]]
                    o = op[1]
                    n = int(op[2:])
                    self.wf[key].append((k, o, n, dest))
                else:
                    self.wf[key].append((i,))
        for part in parts:
            p = part[1:-1].split(',')
            curr_parts = []
            for i in p:
                curr_parts.append(int(i[2:]))
            self.parts.append(curr_parts)

    @staticmethod
    def pass_cond(cond, part):
        if len(cond) == 1:
            return True
        if cond[1] == '<':
            return part[cond[0]] < cond[2]
        return part[cond[0]] > cond[2]

    def solve(self):
        for p in self.parts:
            curr_key = 'in'
            while curr_key not in 'RA':             # USA USA USA RAAAAAAAAA
                ins = self.wf[curr_key]
                valid = False
                i = 0
                while not valid:
                    curr_ins = ins[i]
                    if self.pass_cond(curr_ins, p):
                        valid = True
                        curr_key = curr_ins[-1]
                    i += 1
            if curr_key == 'R':
                self.r.append(p)
            else:
                self.a.append(p)
        return sum(sum(p) for p in self.a)


sol = Solution('input.txt')
print(sol.solve())
