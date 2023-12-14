class Solution:
    def __init__(self, source):
        self.notes = self.parse(source)

    def parse(self, source):
        with open(source, "r") as f:
            notes = f.read().split('\n\n')
        return [note.split('\n') for note in notes]

    @staticmethod
    def off_by_one(a, b):
        dif = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                dif += 1
        return dif == 1

    def solve(self, part_b: bool):
        result = 0
        for note in self.notes:
            horizontal = 0
            vertical = 0
            for i in range(len(note) - 1):
                stack = note[0:i+1]
                curr_count = 0
                swap = False
                for j in range(i + 1, len(note)):
                    if not stack:
                        if part_b == swap:
                            horizontal = max(horizontal, curr_count)
                        break
                    elif stack[-1] == note[j]:
                        stack.pop()
                        curr_count += 1
                        if j == len(note) - 1:
                            if part_b == swap:
                                horizontal = max(horizontal, curr_count + len(stack))
                            break
                    elif self.off_by_one(stack[-1], note[j]) and not swap and part_b:
                        stack.pop()
                        swap = True
                        curr_count += 1
                        if j == len(note) - 1:
                            horizontal = max(horizontal, curr_count + len(stack))
                            break
                    elif stack[-1] != note[j]:
                        break
            for i in range(len(note[0]) - 1):
                swap = False
                stack = [''.join(n[j] for n in note) for j in range(i + 1)]
                curr_count = 0
                for j in range(i + 1, len(note[0])):
                    next_line = ''.join(n[j] for n in note)
                    if not stack:
                        if part_b == swap:
                            vertical = max(vertical, curr_count)
                        break
                    elif stack[-1] == next_line:
                        stack.pop()
                        curr_count += 1
                        if j == len(note[0]) - 1:
                            if part_b == swap:
                                vertical = max(vertical, curr_count + len(stack))
                            break
                    elif self.off_by_one(stack[-1], next_line) and not swap and part_b:
                        stack.pop()
                        curr_count += 1
                        swap = True
                        if j == len(note[0]) - 1:
                            vertical = max(vertical, curr_count + len(stack))
                            break
                    elif stack[-1] != next_line:
                        break
            result += (100 * horizontal + vertical)
        return result


sol = Solution("input.txt")
print(sol.solve(False))
print(sol.solve(True))
