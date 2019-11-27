class Job:
    def __init__(self, time: int, fine: int, index: int):
        self.fine = fine
        self.length = time
        self.fine_per_day: float = fine / time
        self.index = index

    def __lt__(self, other):
        if self.fine_per_day < other.fine_per_day:
            return True
        elif self.fine_per_day == other.fine_per_day:
            return self.index > other.index


def optimal_order(jobs: list) -> list:
    jobs.sort()
    result = []
    for e in reversed(jobs):
        result.append(e.index)
    return result


def solve_problem(jobs: list) -> None:
    ans = optimal_order(jobs)
    for i, x in enumerate(ans):
        if i > 0:
            print(" ", end="")
        print(x, end="")
    print()


test_cases = int(input())
for x in range(test_cases):
    input()
    number_of_jobs = int(input())
    jobs = []
    for i in range(number_of_jobs):
        time, fine = map(int, input().split())
        job = Job(time, fine, i + 1)
        jobs.append(job)
    solve_problem(jobs)
    if x < test_cases - 1:
        print()  # seperate by newline
