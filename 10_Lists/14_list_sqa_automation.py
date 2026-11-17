"""
====================================================
10_Lists / 14_list_sqa_automation.py
====================================================
Topic: Lists in SQA Test Automation (the last file of the Lists module)
====================================================
Notes before you run this file:
1) A test run is mostly lists: test data, test cases, expected and
   actual values, results, log lines, table rows, CSV rows, API items.
2) Selenium and an API are NOT needed here. A page title, a table, a
   response or a log is just text, so we use plain lists and strings
   to simulate them. Concept 20 is the exception: it uses REAL
   Playwright with a small page built from a string (no internet).
   Install once:  python -m pip install playwright
                  python -m playwright install chromium
   If Playwright is missing, Concept 20 only prints a message and
   the rest of the file still runs.
3) The shared data (TESTS, RESULTS, LOG_LINES, EMAIL, LOG_PATTERN) is
   defined once, right after the imports. Everything else is created
   inside the program that uses it.
4) All passwords, tokens and emails are FAKE demo values.
5) Plain programs, no functions. Only Concept 22 uses a tiny function,
   because the trap it shows exists only in function definitions.
6) Results marked "typical" can differ a little between Python or
   browser versions.
"""

import copy
import csv
import io
import itertools
import json
import os
import re
import statistics


# =====================================================
# Shared sample data
# =====================================================
EMAIL = re.compile(r"[\w.+\-]+@[A-Za-z0-9\-]+(?:\.[A-Za-z0-9\-]+)*\.[A-Za-z]{2,}")

TESTS = [
    {"id": "TC_001", "name": "login ok", "module": "login", "priority": 1, "tags": ["smoke", "ui"]},
    {"id": "TC_002", "name": "login wrong password", "module": "login", "priority": 2, "tags": ["negative"]},
    {"id": "TC_003", "name": "add to cart", "module": "cart", "priority": 1, "tags": ["smoke"]},
    {"id": "TC_004", "name": "checkout", "module": "cart", "priority": 3, "tags": ["regression", "slow"]},
    {"id": "TC_005", "name": "search", "module": "search", "priority": 2, "tags": ["smoke", "ui"]},
]

RESULTS = [
    ("login", "PASS", 2.3),
    ("cart", "FAIL", 5.1),
    ("search", "PASS", 1.4),
    ("payment", "FAIL", 8.7),
    ("logout", "PASS", 0.9),
    ("profile", "SKIP", 0.0),
]

LOG_LINES = [
    "2026-10-17 10:00:01 [INFO] suite started",
    "2026-10-17 10:00:02 [PASS] test_login completed in 2.3s",
    "2026-10-17 10:00:05 [ERROR] Database connection failed (code=500)",
    "2026-10-17 10:00:10 [WARNING] Slow response: 3.8s",
    "2026-10-17 10:00:15 [FAIL] test_checkout failed: button not found",
    "2026-10-17 10:00:20 [PASS] test_logout completed in 0.9s",
    "2026-10-17 10:00:25 [WARNING] Retry attempt 2 for test_payment",
    "2026-10-17 10:00:35 [FAIL] test_payment failed: timeout after 30s",
    "2026-10-17 10:00:45 [PASS] test_profile completed in 2.1s",
    "2026-10-17 10:00:50 [INFO] suite finished",
]

LOG_PATTERN = re.compile(r"(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2}:\d{2}) "
                         r"\[(?P<level>[A-Z]+)\] (?P<message>.*)")


# =====================================================
# Concept 1: Why Lists Are Everywhere in Test Automation
# =====================================================
"""
Definition:
In a test project a list is the natural container for everything that
comes in groups: browsers to test, test ids, usernames, expected menu
texts, results of a run, lines of a log file, rows of a table or CSV
file, items of an API response. The tools you learned in this module
map to daily jobs:
  append / extend     collect results while tests run
  in / count / index  check what is on a page
  sort / sorted       check or fix the order
  slicing             first / last / pages / halves
  zip / enumerate     compare expected and actual, with positions
  comprehensions      filter and clean data in one line
  copy / deepcopy     keep shared test data safe
"""

# Program 1: The basic lists of a test run
browsers = ["chromium", "firefox", "webkit"]
test_names = ["login", "cart", "search"]
print(len(browsers), browsers[0], browsers[-1])         # 3 chromium webkit

# Program 2: Every test on every browser
runs = [f"{t} on {b}" for b in browsers for t in test_names]
print(len(runs), runs[0], "|", runs[-1])                # 9 login on chromium | search on webkit

# Program 3: A first summary of results
statuses = ["PASS", "FAIL", "PASS", "PASS"]
print(statuses.count("PASS"), statuses.count("FAIL"))   # 3 1
print("any failure?", "FAIL" in statuses)               # any failure? True


# =====================================================
# Concept 2: Test Data Lists
# =====================================================
"""
Definition:
Good test data covers normal values, boundary values (just below, on
and just above a limit), empty and space-only values, special
characters and text in other languages. Keep each kind in a list, then
loop over it, so adding one more case is one more item.
"""

# Program 1: Valid and invalid emails
emails = ["ali@example.com", "bad.email", "sara@x.org", "a b@x.com", "@x.com"]
valid = [e for e in emails if EMAIL.fullmatch(e)]
invalid = [e for e in emails if not EMAIL.fullmatch(e)]
print(valid)                            # ['ali@example.com', 'sara@x.org']
print(invalid)                          # ['bad.email', 'a b@x.com', '@x.com']

# Program 2: Boundary values for a username of 4 to 12 characters
lengths = [3, 4, 5, 11, 12, 13]
usernames = ["a" * n for n in lengths]
print([len(u) for u in usernames if 4 <= len(u) <= 12])         # [4, 5, 11, 12] (the accepted ones)
print([len(u) for u in usernames if not 4 <= len(u) <= 12])     # [3, 13] (the rejected ones)

# Program 3: Tricky inputs for any text field
tricky = ["", " ", "O'Brien", "a&b", "<b>x</b>", "علی", "😀", "a" * 256]
print(len(tricky))                      # 8
print([len(x) for x in tricky])         # [0, 1, 7, 3, 8, 3, 1, 256]
print([x for x in tricky if not x.isascii()])           # ['علی', '😀']
print([x for x in tricky if not x.strip()])             # ['', ' '] (blank inputs)

# Program 4: Test data with expected results as tuples
cases = [("5", True), ("abc", False), ("-1", False), ("", False), ("007", True)]
for text, expected in cases:
    actual = text.isdecimal()
    print("PASS" if actual == expected else "FAIL", repr(text))     # all PASS


# =====================================================
# Concept 3: Data-Driven Testing (a List of Rows)
# =====================================================
"""
Definition:
Data-driven testing means ONE test steps list and MANY rows of data.
Every row is a tuple (or list or dictionary) that you unpack in the
loop. A new case is a new row, not new code. Here the "application"
is a small dictionary, so the example runs everywhere.
"""

valid_users = {"admin": "Admin@123", "tester": "Test@456"}
login_rows = [
    ("admin", "Admin@123", True),
    ("admin", "wrong", False),
    ("", "Admin@123", False),
    ("tester", "Test@456", True),
    ("unknown", "x", False),
    ("admin", "admin@123", True),       # a wrong expectation on purpose
]

# Program 1: One check per row
for number, (username, password, expected_ok) in enumerate(login_rows, start=1):
    actual_ok = valid_users.get(username) == password
    status = "PASS" if actual_ok == expected_ok else "FAIL"
    print(f"{number}. {status} user={username!r:<10} expected={expected_ok}")
# rows 1 to 5 PASS, row 6 FAIL

# Program 2: Collect the failed rows
failed_rows = [row for row in login_rows if (valid_users.get(row[0]) == row[1]) != row[2]]
print(len(failed_rows), failed_rows)    # 1 [('admin', 'admin@123', True)]

# Program 3: Case ids for the rows
print([f"LOGIN_{i:03}" for i in range(1, len(login_rows) + 1)])
# ['LOGIN_001', 'LOGIN_002', 'LOGIN_003', 'LOGIN_004', 'LOGIN_005', 'LOGIN_006']

# Program 4: Positive and negative cases
positive = [r for r in login_rows if r[2]]
negative = [r for r in login_rows if not r[2]]
print(len(positive), len(negative))     # 3 3


# =====================================================
# Concept 4: Test Cases as a List of Dictionaries
# =====================================================
"""
Definition:
A test plan is naturally a list of dictionaries: every dictionary is
one test case with an id, a name, a module, a priority and tags.
Filtering, sorting and grouping then use the comprehension and
sorted() tools you already know.
"""

# Program 1: The smoke tests
print([t["id"] for t in TESTS if "smoke" in t["tags"]])         # ['TC_001', 'TC_003', 'TC_005']

# Program 2: Most important first (priority 1 is the most important), then by id
ordered = sorted(TESTS, key=lambda t: (t["priority"], t["id"]))
print([t["id"] for t in ordered])       # ['TC_001', 'TC_003', 'TC_002', 'TC_005', 'TC_004']

# Program 3: Group the test ids by module
by_module = {}
for t in TESTS:
    by_module.setdefault(t["module"], []).append(t["id"])
print(by_module)                        # {'login': ['TC_001', 'TC_002'], 'cart': ['TC_003', 'TC_004'], 'search': ['TC_005']}

# Program 4: Every tag in use, without duplicates
print(sorted({tag for t in TESTS for tag in t["tags"]}))        # ['negative', 'regression', 'slow', 'smoke', 'ui']

# Program 5: Everything except the slow tests
print([t["id"] for t in TESTS if "slow" not in t["tags"]])      # ['TC_001', 'TC_002', 'TC_003', 'TC_005']


# =====================================================
# Concept 5: Expected vs Actual Lists
# =====================================================
"""
Definition:
Comparing two lists is the core of most checks. Decide first what
"equal" means:
  == on lists            same items, same ORDER, same duplicates
  sorted(a) == sorted(b) same items and duplicates, order ignored
  set(a) == set(b)       same different values (duplicates ignored!)
A good failure message tells WHAT is missing, WHAT is extra and WHERE.
"""

# Program 1: Order matters for ==
expected = ["Home", "Products", "Contact"]
actual = ["Home", "Contact", "Products"]
print(expected == actual)               # False
print(sorted(expected) == sorted(actual))       # True (same items)

# Program 2: Missing and extra items
actual = ["Home", "Product", "Contact", "Blog"]
print("missing:", [x for x in expected if x not in actual])     # ['Products']
print("extra:", [x for x in actual if x not in expected])       # ['Product', 'Blog']

# Program 3: A message with the position
if len(expected) != len(actual):
    print(f"FAIL: expected {len(expected)} items, got {len(actual)}")
for position, (e, a) in enumerate(zip(expected, actual), start=1):
    if e != a:
        print(f"item {position}: expected {e!r}, got {a!r}")    # item 2

# Program 4: Duplicates are hidden by sets
expected_items = ["Pen", "Bag"]
actual_items = ["Pen", "Pen", "Bag"]
print(set(expected_items) == set(actual_items))         # True  (the duplicate is hidden)
print(sorted(expected_items) == sorted(actual_items))   # False (the duplicate is found)

# Program 5: The first position where two lists differ
a = ["Home", "Products", "Contact"]
b = ["Home", "Contact", "Products"]
print(next((i for i, (x, y) in enumerate(zip(a, b)) if x != y), None))      # 1


# =====================================================
# Concept 6: Soft Assertions (Collect ALL Failures)
# =====================================================
"""
Definition:
A hard assertion (assert) stops the test at the FIRST failure, so you
learn about one problem per run. A soft check collects the failures
in a list and reports them together at the end, so one run shows
everything that is wrong.
"""

checks = [
    ("title", "Login - MyApp", "Login - MyApp"),
    ("heading", "Welcome, Ali!", "Welcome Ali"),
    ("button", "Log In", "Log In"),
    ("footer", "(c) 2026", "(c) 2025"),
]

# Program 1: Collect the failures
failures = [f"{name}: expected {e!r}, got {a!r}" for name, e, a in checks if e != a]
print(len(failures), "of", len(checks), "checks failed")        # 2 of 4 checks failed

# Program 2: Show them all
for message in failures:
    print(" -", message)

# Program 3: A hard assertion stops at the first failure
for name, e, a in checks:
    try:
        assert e == a, f"{name}: expected {e!r}, got {a!r}"
    except AssertionError as err:
        print("stopped at the first failure:", err)
        break

# Program 4: One error with all the messages at the end of the test
try:
    if failures:
        raise AssertionError("\n".join(failures))
except AssertionError as err:
    print(err)


# =====================================================
# Concept 7: Summarizing Test Results
# =====================================================
"""
Definition:
A summary answers four questions: how many of each status, what is the
pass rate (skipped tests are NOT counted), which tests failed, and
which were the slowest. A run is usually "failed" when at least one
test failed, and the process exit code tells the CI system that.
"""

# Program 1: Count every status
counts = {}
for name, status, seconds in RESULTS:
    counts[status] = counts.get(status, 0) + 1
print(counts)                           # {'PASS': 3, 'FAIL': 2, 'SKIP': 1}

# Program 2: The pass rate of the executed tests
executed = [r for r in RESULTS if r[1] != "SKIP"]
passed = sum(1 for r in executed if r[1] == "PASS")
print(len(executed), passed, f"{passed / len(executed):.1%}")   # 5 3 60.0%

# Program 3: Total and average time
durations = [r[2] for r in executed]
total = sum(durations)
print(f"{total:.1f}s total, {total / len(durations):.2f}s average")     # 18.4s total, 3.68s average

# Program 4: The two slowest tests
slowest = sorted(executed, key=lambda r: r[2], reverse=True)[:2]
print([r[0] for r in slowest])          # ['payment', 'cart']

# Program 5: The failed tests
print([r[0] for r in RESULTS if r[1] == "FAIL"])        # ['cart', 'payment']

# Program 6: The exit code for the CI system
exit_code = 1 if counts.get("FAIL", 0) > 0 else 0
print("exit code:", exit_code)          # exit code: 1

# Program 7: Response times, the median is not disturbed by one huge value
times = [1.2, 0.8, 2.5, 1.9, 0.9, 3.1, 1.4, 2.2, 1.1, 5.0]
print(f"mean {statistics.mean(times):.2f} | median {statistics.median(times):.2f}")     # mean 2.01 | median 1.65
print(f"fastest {min(times)} | slowest {max(times)}")           # fastest 0.8 | slowest 5.0


# =====================================================
# Concept 8: Finding Flaky Tests
# =====================================================
"""
Definition:
A flaky test passes and fails WITHOUT any change of the code. You
find it by running the same test several times and looking at its
list of results: more than one different value means it is flaky.
A test that always fails is broken, not flaky.
"""

runs = {
    "login": ["PASS", "PASS", "PASS"],
    "cart": ["PASS", "FAIL", "PASS"],
    "search": ["FAIL", "FAIL", "FAIL"],
    "pay": ["FAIL", "PASS", "FAIL"],
}

# Program 1: Sort the tests into three groups
flaky = [name for name, st in runs.items() if len(set(st)) > 1]
always_failing = [name for name, st in runs.items() if set(st) == {"FAIL"}]
stable = [name for name, st in runs.items() if set(st) == {"PASS"}]
print(flaky, always_failing, stable)    # ['cart', 'pay'] ['search'] ['login']

# Program 2: Failure rate of every test
for name, st in runs.items():
    print(f"{name:<7}{st.count('FAIL') / len(st):.0%}")  # login 0%   cart 33%   search 100%   pay 67%

# Program 3: How often did the result change? (more changes = more unstable)
for name, st in runs.items():
    changes = sum(1 for a, b in zip(st, st[1:]) if a != b)
    print(name, changes)                # login 0   cart 2   search 0   pay 2


# =====================================================
# Concept 9: Retrying a Failed Test
# =====================================================
"""
Definition:
A retry runs a failed test again, up to a limit. for-else is a neat
fit: the else block runs only when the loop ended WITHOUT a break,
meaning every attempt failed. A test that passes only after a retry
should be reported as FLAKY, not as a clean pass.
"""

# Program 1: Two scenarios with up to 3 attempts
for scenario in (["FAIL", "FAIL", "PASS"], ["FAIL", "FAIL", "FAIL"]):
    print("scenario:", scenario)
    max_attempts = 3
    for attempt in range(1, max_attempts + 1):
        outcome = scenario[attempt - 1]
        print("  attempt", attempt, outcome)
        if outcome == "PASS":
            print("  passed on attempt", attempt, "(flaky)" if attempt > 1 else "")
            break
    else:
        print("  FAILED after", max_attempts, "attempts")

# Program 2: A retry queue, a failed test goes to the end of the queue once
queue = ["test_a", "test_b", "test_c"]
fails_once = {"test_b"}
retried = []
while queue:
    test = queue.pop(0)
    if test in fails_once:
        fails_once.discard(test)
        print(test, "FAILED, will retry")
        queue.append(test)
        retried.append(test)
    else:
        print(test, "PASSED")
print("retried:", retried)              # ['test_b']


# =====================================================
# Concept 10: Sharing Tests Between Parallel Workers
# =====================================================
"""
Definition:
To run tests in parallel you split the list of tests between workers.
Three common ways:
  round robin   tests[w::workers]     (alternate tests)
  chunks        slices of equal size  (a long list cut in pieces)
  balanced      the longest tests first, each to the least busy worker
Every test must go to exactly ONE worker.
"""

tests = [f"test_{i:02}" for i in range(1, 8)]

# Program 1: Round robin
workers = 3
print([tests[w::workers] for w in range(workers)])
# [['test_01', 'test_04', 'test_07'], ['test_02', 'test_05'], ['test_03', 'test_06']]

# Program 2: Chunks (the last one is shorter)
size = -(-len(tests) // workers)        # rounds up: 3
chunks = [tests[i:i + size] for i in range(0, len(tests), size)]
print(chunks)                           # [['test_01', 'test_02', 'test_03'], ['test_04', 'test_05', 'test_06'], ['test_07']]

# Program 3: Balanced by duration
timed = [("a", 8), ("b", 7), ("c", 6), ("d", 5), ("e", 4)]
loads = [0, 0]
assignment = [[], []]
for name, seconds in sorted(timed, key=lambda t: t[1], reverse=True):
    w = loads.index(min(loads))         # the worker with the least work so far
    assignment[w].append(name)
    loads[w] += seconds
print(assignment, loads)                # [['a', 'd', 'e'], ['b', 'c']] [17, 13]

# Program 4: Check that every test is used exactly once
flat = [t for chunk in chunks for t in chunk]
print(sorted(flat) == sorted(tests))    # True


# =====================================================
# Concept 11: Selecting Tests by Tag, Priority or Id
# =====================================================
"""
Definition:
You rarely run every test. Select them with a rule: any of some tags,
all of some tags, a priority limit, or an explicit list of ids.
Sets make tag rules short: wanted & tags (any common tag),
required <= tags (all required tags are present).
An EMPTY selection is a problem and must be reported.
"""

# Program 1: Any of these tags
wanted = {"smoke", "negative"}
print([t["id"] for t in TESTS if wanted & set(t["tags"])])      # ['TC_001', 'TC_002', 'TC_003', 'TC_005']

# Program 2: All of these tags
required = {"smoke", "ui"}
print([t["id"] for t in TESTS if required <= set(t["tags"])])   # ['TC_001', 'TC_005']

# Program 3: A list of ids typed as one text
chosen = "TC_001,TC_004".split(",")
print([t["name"] for t in TESTS if t["id"] in chosen])          # ['login ok', 'checkout']

# Program 4: Priority 1 and 2 only
print([t["id"] for t in TESTS if t["priority"] <= 2])           # ['TC_001', 'TC_002', 'TC_003', 'TC_005']

# Program 5: An empty selection must be reported
selected = [t for t in TESTS if "nightly" in t["tags"]]
if not selected:
    print("FAIL: no tests selected, check the tag filter")


# =====================================================
# Concept 12: Test Matrix (Browsers x Sizes x Tests)
# =====================================================
"""
Definition:
A test matrix runs the same tests in many environments.
itertools.product(a, b) gives every combination (the same as two
nested loops). Then remove the combinations you do not support.
"""

browsers = ["chromium", "firefox", "webkit"]
viewports = [(1280, 720), (375, 667)]

# Program 1: All combinations
combos = list(itertools.product(browsers, viewports))
print(len(combos), combos[0])           # 6 ('chromium', (1280, 720))

# Program 2: Remove an unsupported combination
supported = [c for c in combos if not (c[0] == "webkit" and c[1][0] < 500)]
print(len(supported))                   # 5

# Program 3: A readable name for every run
print([f"{b}-{w}x{h}" for b, (w, h) in combos])
# ['chromium-1280x720', 'chromium-375x667', 'firefox-1280x720', 'firefox-375x667', 'webkit-1280x720', 'webkit-375x667']

# Program 4: How many runs for the whole plan?
print(len(TESTS) * len(supported))      # 25


# =====================================================
# Concept 13: Setup and Teardown (a List as a Stack)
# =====================================================
"""
Definition:
Things that were created in a test (users, orders, browser pages) must
be cleaned up in REVERSE order, because later things depend on earlier
ones. A list used as a stack does exactly that: append() to remember
what was created, pop() to take the newest first. The cleanup belongs
in "finally", so it runs even when the test fails.
"""

# Program 1: Create, then delete in reverse order
created = []
for name in ["user", "order", "payment"]:
    created.append(name)
    print("created", name)
while created:
    print("deleting", created.pop())    # payment, order, user

# Program 2: The cleanup runs even if the test fails
opened = []
try:
    for name in ["browser", "page"]:
        opened.append(name)
    raise AssertionError("button not found")
except AssertionError as e:
    print("test failed:", e)
finally:
    while opened:
        print("closing", opened.pop())  # closing page, closing browser

# Program 3: The teardown order is the reverse of the setup order
steps = ["start browser", "open page", "login"]
print(list(reversed(steps)))            # ['login', 'open page', 'start browser']


# =====================================================
# Concept 14: Log Analysis
# =====================================================
"""
Definition:
A log file is a list of lines. Parse every line with one regular
expression with named groups, then count levels, list the problems,
find the first error with the lines around it, and measure durations.
Lines that do not match the pattern must be REPORTED, not ignored.
"""

entries = [m.groupdict() for m in (LOG_PATTERN.fullmatch(line) for line in LOG_LINES) if m]

# Program 1: Parse every line
print(len(entries), entries[2])
# 10 {'date': '2026-10-17', 'time': '10:00:05', 'level': 'ERROR', 'message': 'Database connection failed (code=500)'}

# Program 2: Count the levels
level_counts = {}
for e in entries:
    level_counts[e["level"]] = level_counts.get(e["level"], 0) + 1
print(level_counts)                     # {'INFO': 2, 'PASS': 3, 'ERROR': 1, 'WARNING': 2, 'FAIL': 2}

# Program 3: The problems only
for e in entries:
    if e["level"] in ("ERROR", "FAIL"):
        print(e["time"], e["level"], e["message"])

# Program 4: The first error with one line before and one after (max() avoids a negative slice start)
first_error = next((i for i, e in enumerate(entries) if e["level"] == "ERROR"), None)
if first_error is not None:
    start = max(0, first_error - 1)
    for line in LOG_LINES[start:first_error + 2]:
        print(line)

# Program 5: Durations of the passed tests
durations = [float(m.group(1)) for line in LOG_LINES if (m := re.search(r"completed in ([\d.]+)s", line))]
print(durations, f"{sum(durations):.1f}")       # [2.3, 0.9, 2.1] 5.3

# Program 6: How long did the run take?
h1, m1, s1 = map(int, entries[0]["time"].split(":"))
h2, m2, s2 = map(int, entries[-1]["time"].split(":"))
print((h2 * 3600 + m2 * 60 + s2) - (h1 * 3600 + m1 * 60 + s1), "seconds")       # 49 seconds

# Program 7: Names of the failed tests and the error codes
print([m.group(1) for e in entries if e["level"] == "FAIL" and (m := re.match(r"(\w+) failed", e["message"]))])
# ['test_checkout', 'test_payment']
print(re.findall(r"code=(\d+)", "\n".join(LOG_LINES)))  # ['500']

# Program 8: Lines that do not match the pattern
mixed = LOG_LINES[:2] + ["garbage line"]
print([line for line in mixed if not LOG_PATTERN.fullmatch(line)])      # ['garbage line']

# Program 9: The last three lines (times only)
print([line.split()[1] for line in LOG_LINES[-3:]])     # ['10:00:35', '10:00:45', '10:00:50']


# =====================================================
# Concept 15: CSV Test Data
# =====================================================
"""
Definition:
CSV rows are lists of strings. A plain split(",") breaks when a value
contains a comma (it is then written in quotes), so use the csv
module. DictReader turns every row into a dictionary with the header
names as keys. Everything read from a CSV file is TEXT: convert numbers
yourself. Always check that every row has the expected number of cells.
"""

csv_lines = ["username,password,expected", "admin,Admin@123,success", "admin,wrong,error", ",Admin@123,error"]
csv_text = "\n".join(csv_lines)

# Program 1: Header and rows
rows = list(csv.reader(io.StringIO(csv_text)))
header, *data = rows
print(header)                           # ['username', 'password', 'expected']
print(len(data))                        # 3

# Program 2: Records with DictReader
records = list(csv.DictReader(io.StringIO(csv_text)))
print(records[0])                       # {'username': 'admin', 'password': 'Admin@123', 'expected': 'success'}

# Program 3: Find the rows with a wrong number of cells (line numbers start at 1 for the header)
broken_rows = list(csv.reader(io.StringIO(csv_text + "\ntester,Test@456")))
for line_number, row in enumerate(broken_rows[1:], start=2):
    if len(row) != 3:
        print(f"line {line_number}: expected 3 cells, got {len(row)}")  # line 5

# Program 4: Text to numbers
ages_csv = "name,age\nAli,25\nSara,22"
ages_rows = list(csv.reader(io.StringIO(ages_csv)))[1:]
ages = [int(age) for name, age in ages_rows]
print(ages, sum(ages) / len(ages))      # [25, 22] 23.5

# Program 5: Remove duplicate rows, the order is kept
dup_rows = [["a", "1"], ["b", "2"], ["a", "1"]]
print([list(t) for t in dict.fromkeys(tuple(r) for r in dup_rows)])     # [['a', '1'], ['b', '2']]

# Program 6: A quoted comma
line = 'Ali,"Lahore, Pakistan",25'
print(line.split(","))                  # ['Ali', '"Lahore', ' Pakistan"', '25'] (wrong)
print(list(csv.reader([line]))[0])      # ['Ali', 'Lahore, Pakistan', '25'] (right)

# Program 7: Rows with an empty cell (line numbers)
print([n for n, r in enumerate(data, start=2) if "" in r])      # [4]

# Program 8: Write CSV text
out = io.StringIO()
csv.writer(out).writerows([["id", "status"], [1, "PASS"], [2, "FAIL"]])
print(out.getvalue().splitlines())      # ['id,status', '1,PASS', '2,FAIL']


# =====================================================
# Concept 16: API Responses with Lists (JSON)
# =====================================================
"""
Definition:
An API often returns a list of objects. json.loads() turns the JSON
text into Python lists and dictionaries. Check the response in this
order: the status code (not simulated here), the structure (the type
and the required keys), the values, then the order and the count.
Parse the JSON, do not search the raw text for words.
"""

response_text = json.dumps({
    "status": "ok", "page": 1,
    "items": [
        {"id": 1, "name": "Pen", "price": 9.99, "tags": ["office"]},
        {"id": 2, "name": "Notebook", "price": 45.0, "tags": ["office", "paper"]},
        {"id": 3, "name": "Bag", "price": 199.0, "tags": []},
    ],
})
data = json.loads(response_text)
items = data["items"]

# Program 1: Count, ids and names
print(len(items), [i["id"] for i in items], [i["name"] for i in items])     # 3 [1, 2, 3] ['Pen', 'Notebook', 'Bag']

# Program 2: Required keys of every item
required = {"id", "name", "price", "tags"}
broken = items + [{"id": 4, "name": "Cap"}]
print([f"item {n}: missing {sorted(required - set(i))}" for n, i in enumerate(broken, start=1) if not required <= set(i)])
# ["item 4: missing ['price', 'tags']"]

# Program 3: Unique ids
ids = [i["id"] for i in items]
print(len(ids) == len(set(ids)), len([1, 2, 2]) == len(set([1, 2, 2])))    # True False

# Program 4: Types (a bool is also an int, so exclude it)
print(all(isinstance(i["price"], (int, float)) and not isinstance(i["price"], bool) for i in items))    # True

# Program 5: Order, filter and count
prices = [i["price"] for i in items]
print(prices == sorted(prices))         # True
print([i["name"] for i in items if i["price"] < 100])       # ['Pen', 'Notebook']
print([i["name"] for i in items if not i["tags"]])          # ['Bag']

# Program 6: The root of a JSON text can be a list, and an empty list is a valid answer
print(isinstance(json.loads("[1, 2, 3]"), list), json.loads("[]") == [])    # True True
if not json.loads("[]"):
    print("the API returned no items, is that expected?")

# Program 7: A raw text search can lie
tricky = '{"status": "failed", "message": "success was not achieved"}'
print("success" in tricky, json.loads(tricky)["status"] == "success")      # True False


# =====================================================
# Concept 17: Validating a Table
# =====================================================
"""
Definition:
A table from a page is a header list and a list of rows (lists).
Find a column by its header NAME, not by a fixed number, so the test
still works when the column order changes. Then check the content:
a column, the order of the rows, empty cells, and calculated totals.
"""

header = ["Name", "Email", "Status"]
rows = [["Ali", "ali@example.com", "Active"], ["Sara", "sara@example.com", "Inactive"], ["Bilal", "bilal@example.com", "Active"]]

# Program 1: A column by its header name
status_column = header.index("Status")
statuses = [row[status_column] for row in rows]
print(statuses, statuses.count("Active"))       # ['Active', 'Inactive', 'Active'] 2

# Program 2: Rows as records
records = [dict(zip(header, row)) for row in rows]
print(next((r["Email"] for r in records if r["Name"] == "Sara"), None))     # sara@example.com

# Program 3: Is the table sorted by name?
names = [row[0] for row in rows]
print(names == sorted(names), sorted(names))    # False ['Ali', 'Bilal', 'Sara']

# Program 4: Does every total match quantity x price?
order_rows = [["Pen", "2", "$10.00", "$20.00"], ["Bag", "1", "$199.00", "$199.00"], ["Cap", "3", "$5.00", "$16.00"]]
for n, (name, qty, price, total) in enumerate(order_rows, start=1):
    qty_value = int(qty)
    price_value = float(price.replace("$", "").replace(",", ""))
    total_value = float(total.replace("$", "").replace(",", ""))
    if abs(qty_value * price_value - total_value) > 0.005:
        print(f"row {n} ({name}): {qty_value} x {price_value:.2f} = {qty_value * price_value:.2f}, but total is {total_value:.2f}")
# row 3 (Cap): 3 x 5.00 = 15.00, but total is 16.00

# Program 5: Expected table against actual table, cell by cell
expected_table = [["Ali", "Active"], ["Sara", "Inactive"]]
actual_table = [["Ali ", "Active"], ["Sara", "Active"]]
problems = []
if len(expected_table) != len(actual_table):
    problems.append("different number of rows")
for r, (e_row, a_row) in enumerate(zip(expected_table, actual_table), start=1):
    for c, (e, a) in enumerate(zip(e_row, a_row), start=1):
        if e != " ".join(a.split()):
            problems.append(f"row {r}, column {c}: expected {e!r}, got {a!r}")
print(problems)                         # ["row 2, column 2: expected 'Inactive', got 'Active'"]

# Program 6: Empty cells and wrong row sizes
messy = [["Ali", "", "Active"], ["Sara", "sara@example.com"]]
for n, row in enumerate(messy, start=1):
    if len(row) != len(header):
        print(f"row {n}: {len(row)} cells instead of {len(header)}")
    for column, cell in zip(header, row):
        if not cell.strip():
            print(f"row {n}: empty cell in column {column!r}")
# row 1: empty cell in column 'Email'   row 2: 2 cells instead of 3


# =====================================================
# Concept 18: Checking the Order of Items on a Page
# =====================================================
"""
Definition:
"Sort by price", "sort by name" and "newest first" are features you
must test. Turn the page texts into the right type first (numbers for
prices, dates or a natural key for ids), then compare the list with
its sorted version. Compare TEXT with the right rule, or you get
false failures.
"""

# Program 1: Ascending prices from text
for label, texts in (("working", ["$9.99", "$45.00", "$199.00", "$1,234.50"]),
                     ("broken", ["$9.99", "$199.00", "$45.00", "$1,234.50"])):
    prices = [float(t.replace("$", "").replace(",", "")) for t in texts]
    print(label, prices == sorted(prices))      # working True / broken False

# Program 2: Where does the order break?
prices = [9.99, 199.0, 45.0, 1234.5]
for i, (a, b) in enumerate(zip(prices, prices[1:]), start=1):
    if a > b:
        print(f"FAIL: item {i} ({a}) is followed by the smaller item {i + 1} ({b})")
        break

# Program 3: Descending order
print(all(a >= b for a, b in zip([9, 5, 5, 1], [9, 5, 5, 1][1:])))     # True

# Program 4: Names, the case must not matter
names_on_page = ["alice", "Bob", "carol", "Dave"]
print(names_on_page == sorted(names_on_page, key=str.casefold))        # True
print(names_on_page == sorted(names_on_page))                           # False (a false failure)

# Program 5: ISO dates sort correctly as text
dates = ["2026-01-05", "2026-03-01", "2026-02-10"]
print(dates == sorted(dates), sorted(dates))    # False ['2026-01-05', '2026-02-10', '2026-03-01']

# Program 6: Ids with numbers need a natural key
ids = ["TC_1", "TC_2", "TC_10"]
print(sorted(ids))                      # ['TC_1', 'TC_10', 'TC_2'] (text order)
print(ids == sorted(ids, key=lambda t: int(t.split("_")[1])))           # True

# Program 7: Price texts compared as text give a wrong order
print(sorted(["$100", "$20"]))          # ['$100', '$20']
print(sorted(["$100", "$20"], key=lambda t: float(t[1:])))              # ['$20', '$100']


# =====================================================
# Concept 19: Pagination Checks
# =====================================================
"""
Definition:
When results come in pages, check: every page except the last has the
full size, the last page is not empty, no item appears twice, no item
is missing, and the total matches the number the page reports.
"""

# Program 1: A correct list of pages
pages = [list(range(1, 11)), list(range(11, 21)), list(range(21, 24))]
all_items = [x for page in pages for x in page]
print([len(p) for p in pages])          # [10, 10, 3]
print(len(all_items), len(set(all_items)))      # 23 23 (no duplicates)
print(all(len(p) == 10 for p in pages[:-1]) and 0 < len(pages[-1]) <= 10)       # True

# Program 2: A bug, page 2 starts one item too early
buggy = [list(range(1, 11)), list(range(10, 20)), list(range(21, 24))]
all_items = [x for page in buggy for x in page]
seen = set()
repeated = []
for x in all_items:
    if x in seen:
        repeated.append(x)
    seen.add(x)
print("repeated:", repeated)            # [10]
print("missing:", sorted(set(range(1, 24)) - set(all_items)))   # [20]

# Program 3: The number of pages for 23 items with 10 per page
total_items, page_size = 23, 10
print(-(-total_items // page_size), (total_items + page_size - 1) // page_size)     # 3 3

# Program 4: Take one page out of a list
items = list(range(1, 24))
page_number = 3
start = (page_number - 1) * page_size
print(items[start:start + page_size])   # [21, 22, 23]


# =====================================================
# Concept 20: Real Playwright Lists (all_inner_texts and more)
# =====================================================
"""
Definition:
Playwright returns lists of texts from a page:
locator.all_inner_texts()    the VISIBLE text of every match
locator.all_text_contents()  the raw textContent of every match
locator.all()                a list of locators (one for every match)
locator.count()              the number of matches
These methods do NOT wait and do NOT fail when nothing matches, they
return an empty list. So a test must check for an empty list itself
(or use expect(...).to_have_count() / to_have_text([...]), which wait).
The page below is built from a string with page.set_content(), so no
internet is needed.
"""

SHOP_HTML = """<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Shop</title></head>
<body>
<h1>Shop</h1>
<ul id="items"><li>Pen</li><li>Notebook</li><li>Bag</li><li>Cap&nbsp;</li></ul>
<ul id="prices"><li>$9.99</li><li>$45.00</li><li>$1,234.50</li></ul>
<table id="users">
  <thead><tr><th>Name</th><th>Status</th></tr></thead>
  <tbody>
    <tr><td>Ali</td><td>Active</td></tr>
    <tr><td>Sara</td><td>Inactive</td></tr>
    <tr><td>Bilal</td><td>Active</td></tr>
  </tbody>
</table>
<select id="city"><option>Lahore</option><option>Karachi</option><option>Quetta</option></select>
<button>Save</button><button>Cancel</button>
</body></html>"""

try:
    from playwright.sync_api import sync_playwright, expect, Error as PlaywrightError
    PLAYWRIGHT_OK = True
except ImportError:
    PLAYWRIGHT_OK = False
    print("Playwright is not installed. Run: python -m pip install playwright")
    print("Then run: python -m playwright install chromium")

pw = None
browser = None
page = None
if PLAYWRIGHT_OK:
    try:
        pw = sync_playwright().start()
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(SHOP_HTML)
        print("Browser started, page opened")
    except PlaywrightError as e:
        page = None
        print("Could not start the browser. Run: python -m playwright install chromium")
        print(str(e).splitlines()[0])

if page is not None:
    # Program 1: The texts of a list, cleaned with split() and join() (also removes the hidden \xa0)
    texts = page.locator("#items li").all_inner_texts()
    cleaned = [" ".join(t.split()) for t in texts]
    print(cleaned, len(cleaned))        # ['Pen', 'Notebook', 'Bag', 'Cap'] 4
    print(page.locator("#items li").count() == len(cleaned))        # True

    # Program 2: Compare with the expected list
    expected_items = ["Pen", "Notebook", "Bag", "Cap"]
    print(cleaned == expected_items)    # True
    print("missing:", [x for x in expected_items if x not in cleaned])      # []

    # Program 3: A table into a header list and a list of rows
    table_header = page.locator("#users thead th").all_inner_texts()
    table_rows = [row.locator("td").all_inner_texts() for row in page.locator("#users tbody tr").all()]
    print(table_header)                 # ['Name', 'Status']
    print(table_rows)                   # [['Ali', 'Active'], ['Sara', 'Inactive'], ['Bilal', 'Active']]
    status_column = table_header.index("Status")
    print([r[status_column] for r in table_rows].count("Active"))   # 2

    # Program 4: Price texts into numbers and an order check
    price_texts = page.locator("#prices li").all_inner_texts()
    prices = [float(t.replace("$", "").replace(",", "")) for t in price_texts]
    print(price_texts, prices)          # ['$9.99', '$45.00', '$1,234.50'] [9.99, 45.0, 1234.5]
    print(prices == sorted(prices))     # True

    # Program 5: Options of a dropdown and the buttons of a page
    options = page.locator("#city option").all_text_contents()
    print(options, "Karachi" in options)        # ['Lahore', 'Karachi', 'Quetta'] True
    print(page.get_by_role("button").all_inner_texts())             # ['Save', 'Cancel']

    # Program 6: Nothing matches, you get an EMPTY list (no error, no waiting)
    nothing = page.locator(".does-not-exist").all_inner_texts()
    print(nothing, page.locator(".does-not-exist").count())         # [] 0
    if not nothing:
        print("FAIL: no elements found, the selector may be wrong")

    # Program 7: expect() waits and compares a whole list
    expect(page.locator("#prices li")).to_have_text(["$9.99", "$45.00", "$1,234.50"])
    expect(page.locator("#prices li")).to_have_count(3)
    expect(page.locator("#city option")).to_have_text(["Lahore", "Karachi", "Quetta"])
    print("list assertions passed")

    # Program 8: A failing list assertion (expected, it raises AssertionError)
    try:
        expect(page.locator("#prices li")).to_have_text(["$9.99", "$45.00"], timeout=1000)
    except AssertionError:
        print("assertion failed as expected: the page has 3 prices, not 2")

if browser is not None:
    browser.close()
if pw is not None:
    pw.stop()


# =====================================================
# Concept 21: Building a Report
# =====================================================
"""
Definition:
Collect the lines of a report in a LIST, then join them once with
"\\n".join(lines). Aligned columns come from ljust / rjust or f-string
widths. The same data can become text, a Markdown table, JSON or a
file. Always write files with encoding="utf-8".
"""

# Program 1: A text report
report = [" TEST REPORT ".center(40, "=")]
for name, status, seconds in RESULTS:
    report.append(f"{name:<10}{status:<6}{seconds:>6.1f}s")
report.append("-" * 40)
counts = {}
for name, status, seconds in RESULTS:
    counts[status] = counts.get(status, 0) + 1
report.append("  ".join(f"{k}: {v}" for k, v in counts.items()))
print("\n".join(report))
# ============= TEST REPORT ==============
# login     PASS     2.3s   ... one line per test ...
# PASS: 3  FAIL: 2  SKIP: 1

# Program 2: Write the report to a file and read it back
with open("demo_report.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(report))
with open("demo_report.txt", "r", encoding="utf-8") as f:
    print(len(f.read().splitlines()) == len(report))        # True
os.remove("demo_report.txt")

# Program 3: The same summary as JSON
summary = {"passed": counts["PASS"], "failed": counts["FAIL"], "skipped": counts["SKIP"]}
print(json.dumps(summary))              # {"passed": 3, "failed": 2, "skipped": 1}

# Program 4: A Markdown table
lines = ["| Test | Status |", "|------|--------|"] + [f"| {n} | {s} |" for n, s, _ in RESULTS]
print(len(lines), lines[2])             # 8 | login | PASS |


# =====================================================
# Concept 22: Keeping Test Data Safe (copy, deepcopy, aliasing)
# =====================================================
"""
Definition:
Shared test data (a base user, default settings, a list of rows) must
not be changed by one test, or the next test starts with dirty data
and fails for no real reason. Use deepcopy for nested data, copy for
flat lists, and never let the "expected" list be the SAME object as
the "actual" list. Also avoid a mutable default argument.
"""

# Program 1: A shallow copy shares the inner list
BASE_USER = {"name": "ali", "roles": ["tester"]}
test_user = BASE_USER.copy()
test_user["roles"].append("admin")
print(BASE_USER)                        # {'name': 'ali', 'roles': ['tester', 'admin']} (dirty!)

# Program 2: A deep copy keeps the base clean
BASE_USER = {"name": "ali", "roles": ["tester"]}
test_user = copy.deepcopy(BASE_USER)
test_user["roles"].append("admin")
print(BASE_USER, test_user)
# {'name': 'ali', 'roles': ['tester']} {'name': 'ali', 'roles': ['tester', 'admin']}

# Program 3: A test that can never fail (expected is the same list as actual)
actual_menu = ["Home", "Product", "Contact"]
expected_menu = actual_menu
print(expected_menu == actual_menu)     # True (always!)
expected_menu = ["Home", "Products", "Contact"]
print(expected_menu == actual_menu)     # False (the real bug is found)

# Program 4: A snapshot before an action
items_on_page = ["Pen", "Notebook"]
snapshot = items_on_page.copy()
items_on_page.append("Bag")             # the action under test
print([x for x in items_on_page if x not in snapshot])          # ['Bag']

# Program 5: A shared list changed through an alias
all_tests = ["a", "b", "c"]
run_list = all_tests
run_list.pop()
print(all_tests)                        # ['a', 'b'] (the shared list lost a test)
all_tests = ["a", "b", "c"]
run_list = all_tests.copy()
run_list.pop()
print(all_tests)                        # ['a', 'b', 'c']

# Program 6: A mutable default argument leaks failures between calls
def record_failure(message, failures=[]):
    failures.append(message)
    return failures

print(record_failure("test_login failed"))      # ['test_login failed']
print(record_failure("test_cart failed"))       # ['test_login failed', 'test_cart failed'] (leak)

def record_failure_safe(message, failures=None):
    if failures is None:
        failures = []
    failures.append(message)
    return failures

print(record_failure_safe("test_login failed"))     # ['test_login failed']
print(record_failure_safe("test_cart failed"))      # ['test_cart failed']


# =====================================================
# Concept 23: Common Mistakes in Test Code with Lists
# =====================================================
"""
Definition:
Mistakes that make tests lie (pass when they should fail, or fail
when they should pass):
1) all([]) is True, so an empty list "passes" an all() check
2) reading a column by a fixed index
3) zip() silently drops items
4) comparing prices as text
5) set comparison hides duplicates
6) removing items while looping
7) not stripping the text of a page
"""

# Program 1: An empty list passes all()
found_buttons = []
print(all(b == "Save" for b in found_buttons))                  # True (wrong!)
print(bool(found_buttons) and all(b == "Save" for b in found_buttons))      # False (right)

# Program 2: A fixed index breaks when the column order changes
header_new = ["Name", "Status", "Email"]
row = ["Ali", "Active", "ali@example.com"]
print(row[2])                           # ali@example.com (wrong, we wanted the status)
print(row[header_new.index("Status")])  # Active (right)

# Program 3: zip hides a missing item
expected = ["Home", "Products", "Contact"]
actual = ["Home", "Products"]
print(all(e == a for e, a in zip(expected, actual)))            # True (wrong!)
print(len(expected) == len(actual))     # False (the problem is found here)

# Program 4: Prices compared as text
print(sorted(["$100", "$20"]))          # ['$100', '$20'] (text order)

# Program 5: Sets hide duplicates
print(set(["a", "a", "b"]) == set(["a", "b"]))                  # True
print(sorted(["a", "a", "b"]) == sorted(["a", "b"]))            # False

# Program 6: Removing while looping
data = ["PASS", "SKIP", "SKIP", "FAIL"]
for x in data:
    if x == "SKIP":
        data.remove(x)
print(data)                             # ['PASS', 'SKIP', 'FAIL'] (one SKIP is left)
print([x for x in ["PASS", "SKIP", "SKIP", "FAIL"] if x != "SKIP"])     # ['PASS', 'FAIL']

# Program 7: Text from a page is not clean
print("Login " == "Login", "Login\xa0".strip() == "Login")       # False True


# =====================================================
# Concept 24: Mini Project, a Tiny Test Runner
# =====================================================
"""
Definition:
Everything together: a test plan (a list of dictionaries), a loop that
runs the checks, a list of results, a summary and an exit code.
The "application" is a dictionary, so the project runs anywhere.
Lists compare differently from simple values, so a failed list check
reports the missing items, the extra items, or "different order".
"""

APP = {
    "title": "Login - MyApp",
    "users": {"admin": "Admin@123"},
    "menu": ["Home", "Products", "Contact"],
    "items": ["Pen", "Notebook", "Bag"],
}

TEST_PLAN = [
    {"id": "TC_001", "name": "title is correct", "tags": ["smoke"],
     "actual": APP["title"], "expected": "Login - MyApp"},
    {"id": "TC_002", "name": "menu has 3 items", "tags": ["smoke"],
     "actual": len(APP["menu"]), "expected": 3},
    {"id": "TC_003", "name": "menu texts", "tags": ["ui"],
     "actual": ["Home", "Product", "Contact"], "expected": APP["menu"]},
    {"id": "TC_004", "name": "items are sorted", "tags": ["ui"],
     "actual": APP["items"], "expected": sorted(APP["items"])},
    {"id": "TC_005", "name": "admin can log in", "tags": ["smoke"],
     "actual": APP["users"].get("admin") == "Admin@123", "expected": True},
    {"id": "TC_006", "name": "export a big report", "tags": ["slow"],
     "actual": None, "expected": None},
]

# Program 1: Run the plan and collect the results
run_results = []
for t in TEST_PLAN:
    if "slow" in t["tags"]:
        run_results.append({"id": t["id"], "status": "SKIP", "message": "skipped (tag: slow)"})
        continue
    if t["actual"] == t["expected"]:
        run_results.append({"id": t["id"], "status": "PASS", "message": ""})
        continue
    actual, expected = t["actual"], t["expected"]
    if isinstance(actual, list) and isinstance(expected, list):
        missing = [x for x in expected if x not in actual]
        extra = [x for x in actual if x not in expected]
        message = "same items, different order" if not missing and not extra else f"missing {missing}, extra {extra}"
    else:
        message = f"expected {expected!r}, got {actual!r}"
    run_results.append({"id": t["id"], "status": "FAIL", "message": message})

for r in run_results:
    print(f"{r['id']}  {r['status']:<5} {r['message']}")
# TC_001  PASS
# TC_002  PASS
# TC_003  FAIL  missing ['Products'], extra ['Product']
# TC_004  FAIL  same items, different order
# TC_005  PASS
# TC_006  SKIP  skipped (tag: slow)

# Program 2: The summary
final_counts = {}
for r in run_results:
    final_counts[r["status"]] = final_counts.get(r["status"], 0) + 1
executed = len(run_results) - final_counts.get("SKIP", 0)
print(final_counts)                     # {'PASS': 3, 'FAIL': 2, 'SKIP': 1}
print(f"pass rate: {final_counts.get('PASS', 0) / executed:.0%} of {executed} executed tests")      # 60% of 5

# Program 3: The failed ids and the exit code
failed_ids = [r["id"] for r in run_results if r["status"] == "FAIL"]
print("failed:", failed_ids)            # ['TC_003', 'TC_004']
print("exit code:", 1 if failed_ids else 0)     # 1

# Program 4: A failed run explained in one line
print(f"RESULT: {'FAILED' if failed_ids else 'PASSED'} - {len(failed_ids)} failed, "
      f"{final_counts.get('SKIP', 0)} skipped")     # RESULT: FAILED - 2 failed, 1 skipped