# =====================================================
# Playwright Automation Testing 1  (Concepts 20, 21, 22)
# =====================================================

import re
from urllib.parse import urlparse, parse_qs
import re
import io
import os
import csv
import json
import time
import base64
import random
import secrets
import string
import textwrap
import unicodedata
from http import HTTPStatus
from urllib.parse import urlparse, parse_qs, urlencode

r"""
Setup notes:
1) Install once:  pip install playwright   then   playwright install chromium
2) We use the SYNC API of Playwright, which is the easiest to read.
3) The page below is a tiny FAKE login page kept inside this file.
   page.route() answers every request to https://example.com/** with
   this HTML, so a real browser opens it without internet.
4) Results marked "typical" can differ a little between browser versions.
5) All usernames and passwords here are fake demo values.
"""

try:
    from playwright.sync_api import sync_playwright, expect, Error as PlaywrightError
    PLAYWRIGHT_OK = True
except ImportError:
    PLAYWRIGHT_OK = False
    print("Playwright is not installed. Run: pip install playwright")
    print("Then run:  playwright install chromium")

LOGIN_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Login - MyApp</title>
<style>#loud { text-transform: uppercase; }</style>
</head>
<body>
<h1 id="heading">Welcome, Ali!</h1>
<a id="home" href="/home?user=123">Home</a>
<label for="username">Username</label>
<input id="username" placeholder="Enter username">
<label for="password">Password</label>
<input id="password" type="password">
<button id="login">  Log   In  </button>
<p id="loud">Total price</p>
<div id="message" role="alert"></div>
<ul id="items"><li>Pen</li><li>Notebook</li><li>Bag</li></ul>
<p id="urdu">خوش آمدید</p>
<script>
document.getElementById('login').addEventListener('click', function () {
  var u = document.getElementById('username').value;
  var p = document.getElementById('password').value;
  var m = document.getElementById('message');
  if (u === 'admin' && p === 'Admin@123') {
    m.textContent = 'Login successful';
  } else {
    m.textContent = 'Error: Invalid username or password (Code: AUTH_401)';
  }
});
</script>
</body>
</html>"""

LOGIN_URL = "https://example.com/login?next=home"

# Start the browser once, all three concepts below share the same page
page = None
browser = None
pw = None
if PLAYWRIGHT_OK:
    try:
        pw = sync_playwright().start()
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page()
        page.route("https://example.com/**",
                   lambda route: route.fulfill(status=200,
                                               content_type="text/html; charset=utf-8",
                                               body=LOGIN_HTML))
        page.goto(LOGIN_URL)
        print("Browser started, page opened")
    except PlaywrightError as e:
        page = None
        print("Could not start the browser. Did you run: playwright install chromium ?")
        print(str(e).splitlines()[0])


# =====================================================
# Concept 20: Reading Strings from a Real Page
# =====================================================
"""
Definition:
Playwright gives you page data as normal Python strings:
page.title()                 -> the title
page.url                     -> the current URL
locator.inner_text()         -> the text AS THE USER SEES IT (CSS applied, spaces collapsed)
locator.text_content()       -> the RAW text from the HTML
locator.input_value()        -> what is typed inside an input
locator.get_attribute(name)  -> an attribute such as href
locator.all_inner_texts()    -> a list with the text of every matching element
Once you have the string, every string tool from this course works on it.
"""

if page is not None:
    # Program 1: Title and URL
    title = page.title()
    print(repr(title))                                  # 'Login - MyApp'
    print(title == "Login - MyApp")                     # True
    print(page.url)                                     # https://example.com/login?next=home
    print(page.url.startswith("https://"), "login" in page.url)   # True True

    # Program 2: Split the URL with urlparse, and read a link's full address
    parts = urlparse(page.url)
    print(parts.netloc, parts.path, parse_qs(parts.query))        # example.com /login {'next': ['home']}
    full_link = page.locator("#home").evaluate("el => el.href")   # the browser gives the full URL
    print(page.locator("#home").get_attribute("href"))            # /home?user=123 (as written in HTML)
    print(full_link)                                              # https://example.com/home?user=123
    print(parse_qs(urlparse(full_link).query)["user"][0])         # 123

    # Program 3: inner_text() vs text_content() on the same element
    print(repr(page.locator("#heading").inner_text()))            # 'Welcome, Ali!'
    print(repr(page.locator("#loud").inner_text()))               # 'TOTAL PRICE' (typical: CSS makes it uppercase)
    print(repr(page.locator("#loud").text_content()))             # 'Total price' (raw HTML text)

    # Program 4: Whitespace in a button, then clean it like in the earlier concepts
    raw_text = page.locator("#login").text_content()
    print(repr(raw_text))                                         # '  Log   In  ' (raw)
    cleaned = " ".join(raw_text.split())
    print(repr(cleaned), cleaned == "Log In")                     # 'Log In' True
    print(repr(page.locator("#login").inner_text()))              # 'Log In' (typical)

    # Program 5: A list of texts and Urdu text
    items = page.locator("#items li").all_inner_texts()
    print(items, len(items))                                      # ['Pen', 'Notebook', 'Bag'] 3
    print(sorted(items) == ["Bag", "Notebook", "Pen"])            # True
    urdu = page.locator("#urdu").inner_text()
    print(len(urdu), urdu == "خوش آمدید")                         # 9 True


# =====================================================
# Concept 21: Typing, Clicking and Validating Messages
# =====================================================
"""
Definition:
page.fill(selector, text)  types text into an input.
page.click(selector)       clicks an element.
Locators by meaning are more stable than CSS ids:
page.get_by_label("Username"), page.get_by_role("button", name="Log In"),
page.get_by_text("Welcome", exact=True).
After the action, read the message as a string and check it with the
string tools: ==, in, startswith, re.fullmatch().
"""

if page is not None:
    # Program 1: A wrong login and the error message
    page.goto(LOGIN_URL)
    page.fill("#username", "admin")
    page.fill("#password", "wrong")
    page.click("#login")
    message = page.inner_text("#message")
    print(repr(message))                       # 'Error: Invalid username or password (Code: AUTH_401)'
    print("Invalid username or password" in message)         # True
    error_pattern = re.compile(r"Error: Invalid username or password \(Code: AUTH_\d+\)")
    print(bool(error_pattern.fullmatch(message)))            # True

    # Program 2: A correct login using locators by meaning
    page.goto(LOGIN_URL)
    page.get_by_label("Username").fill("admin")
    page.get_by_label("Password").fill("Admin@123")
    page.get_by_role("button", name="Log In").click()
    message = page.get_by_role("alert").inner_text()
    print(repr(message), message == "Login successful")      # 'Login successful' True

    # Program 3: Find elements by their text
    print(page.get_by_text("Welcome, Ali!", exact=True).count())     # 1
    print(page.get_by_role("heading").inner_text().startswith("Welcome"))   # True
    print(page.get_by_text("pen", exact=True).count())               # 0 (exact text is case-sensitive)
    print(page.get_by_text("Pen", exact=True).count())               # 1

    # Program 4: Urdu text typed into an input and read back
    page.fill("#username", "علی")
    typed = page.input_value("#username")
    print(typed, len(typed), typed == "علی")                  # علی 3 True

    # Program 5: Data driven login test (a list of rows, one check per row)
    rows = [
        ("admin", "Admin@123", "Login successful"),
        ("admin", "wrong", "Invalid username or password"),
        ("", "Admin@123", "Invalid username or password"),
        ("  admin  ", "Admin@123", "Invalid username or password"),   # spaces are not trimmed by this page
    ]
    for username, password, expected_part in rows:
        page.goto(LOGIN_URL)
        page.fill("#username", username)
        page.fill("#password", password)
        page.click("#login")
        actual = page.inner_text("#message")
        status = "PASS" if expected_part in actual else "FAIL"
        print(f"{status}  user={username!r:<11} -> {actual[:32]!r}")


# =====================================================
# Concept 22: expect() Assertions with Strings
# =====================================================
"""
Definition:
expect(...) is Playwright's assertion helper. It WAITS (auto-retries)
until the text is right or the timeout ends, so it is much more
reliable than reading the text once yourself.
expect(page).to_have_title(text_or_regex)
expect(page).to_have_url(text_or_regex)
expect(locator).to_have_text(text_or_regex, ignore_case=True)   (the whole text)
expect(locator).to_contain_text(part)                           (only a part)
expect(locator).to_have_value(text)   expect(locator).to_have_attribute(name, value)
A failed expect() raises AssertionError. Playwright normalizes
whitespace when it compares text, so extra spaces rarely matter.
"""

if page is not None:
    # Program 1: Title and URL, exact text and regex
    page.goto(LOGIN_URL)
    expect(page).to_have_title("Login - MyApp")
    expect(page).to_have_title(re.compile(r"^Login - \w+$"))
    expect(page).to_have_url(re.compile(r"https://example\.com/login\?next=\w+"))
    print("Title and URL assertions passed")

    # Program 2: Different ways to check a text
    page.fill("#username", "admin")
    page.fill("#password", "Admin@123")
    page.click("#login")
    message = page.locator("#message")
    expect(message).to_have_text("Login successful")                # the whole text
    expect(message).to_have_text("LOGIN SUCCESSFUL", ignore_case=True)
    expect(message).to_contain_text("successful")                   # only a part
    expect(message).to_have_text(re.compile(r"^Login \w+$"))        # a pattern
    expect(page.locator("#login")).to_have_text("Log In")           # extra spaces are normalized
    print("Text assertions passed")

    # Program 3: Values and attributes
    page.fill("#username", "tester")
    expect(page.locator("#username")).to_have_value("tester")
    expect(page.locator("#home")).to_have_attribute("href", "/home?user=123")
    expect(page.locator("#items li")).to_have_text(["Pen", "Notebook", "Bag"])   # a whole list
    print("Value, attribute and list assertions passed")

    # Program 4: A failing assertion and a readable failure message
    page.goto(LOGIN_URL)
    page.click("#login")                         # no username or password typed
    try:
        expect(page.locator("#message")).to_have_text("Login successful", timeout=1500)
    except AssertionError as e:
        print("Assertion FAILED (this is expected here)")
        print(str(e).splitlines()[0])
    actual = page.inner_text("#message")
    print(f"expected={'Login successful'!r} actual={actual!r}")

    # Program 5: Our own normalized comparison when we read the text ourselves
    normalize = lambda text: " ".join(text.split()).casefold()
    print(normalize(page.inner_text("#message")) == normalize("ERROR: invalid username or password (code: auth_401)"))   # True
    print(normalize(page.inner_text("#heading")) == "welcome, ali!")      # True

# Close the browser at the very end
if browser is not None:
    browser.close()
if pw is not None:
    pw.stop()
print("Playwright section finished")