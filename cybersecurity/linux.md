# Linux Command Exercises with Python `subprocess`

Ten real-world exercises using `ls`, `cat`, `grep`, `find`, and `awk`, driven from Python with `subprocess`. Difficulty goes from easy to medium.

**Rules for every exercise**

- Use the list form (`["grep", "-c", "ERROR", path]`), never `shell=True`.
- Use `text=True` and `capture_output=True` unless the exercise says otherwise.
- First try the command in the terminal, then write the Python version.

---

## Setup: create sample data

Run this once to get files to practice on:

```bash
mkdir -p lab/logs lab/project/src && cd lab

# app.log
cat > logs/app.log <<'EOF'
2026-09-20 08:01:12 INFO  server started
2026-09-20 08:05:40 WARN  disk usage at 85%
2026-09-20 08:07:03 ERROR database connection failed
2026-09-20 08:07:09 ERROR database connection failed
2026-09-20 08:15:22 INFO  user login: alice
EOF

# access.log  (IP, date, request, status, bytes)
cat > logs/access.log <<'EOF'
10.0.0.5 - - [20/Sep/2026] "GET /index.html" 200 1024
10.0.0.7 - - [20/Sep/2026] "GET /login" 302 512
10.0.0.5 - - [20/Sep/2026] "POST /api/data" 500 2048
10.0.0.9 - - [20/Sep/2026] "GET /index.html" 200 1024
10.0.0.5 - - [20/Sep/2026] "GET /about" 404 256
EOF

# auth.log
cat > logs/auth.log <<'EOF'
Sep 20 09:00:01 srv sshd[101]: Failed password for root from 203.0.113.9 port 4022
Sep 20 09:00:05 srv sshd[101]: Failed password for admin from 203.0.113.9 port 4023
Sep 20 09:01:10 srv sshd[102]: Accepted password for alice from 10.0.0.5 port 5100
Sep 20 09:02:44 srv sshd[103]: Failed password for root from 198.51.100.4 port 6001
EOF

# project files
printf 'def main():\n    # TODO: add logging\n    pass\n' > project/src/main.py
printf 'def helper():\n    # TODO: write tests\n    # FIXME: handle None\n    pass\n' > project/src/utils.py
printf 'DB_HOST=localhost\nDB_PORT=5432\nDEBUG=true\n' > project/config.env
```

---

## Easy

### 1. Newest files (`ls`)

List the 5 most recently modified files in `logs/` using `ls -1t`, and print them numbered.

- **Practices:** `run()`, `stdout.splitlines()`, `enumerate`
- **Shell equivalent:** `ls -1t logs | head -5`
- **Bonus:** also show sizes using `ls -lh` and print only the size and name columns.

### 2. Config reader (`cat`)

Use `cat project/config.env` to read the file, turn each `KEY=VALUE` line into a Python `dict`, and print the DB port as an integer.

- **Practices:** capturing `stdout`, `split("=", 1)`, type conversion
- **Bonus:** handle a missing file by catching `CalledProcessError` and printing the `stderr` message.

### 3. Count errors (`grep -c`)

Count the `ERROR` lines in `logs/app.log` with `grep -c ERROR`. Print `No errors` if there are none.

- **Practices:** `returncode`
- **Watch out:** `grep` returns `0` when it finds a match, `1` when it finds **no** match (not a failure!), and `2` for a real error such as a missing file. Do **not** use `check=True` blindly here. Handle all three cases.

### 4. TODO finder (`grep -rn`)

Search all of `project/` for `TODO` and `FIXME` with `grep -rnE "TODO|FIXME" project/`. Print a neat table: `file | line number | text`.

- **Practices:** splitting output on `:` (use `maxsplit=2`), formatted printing
- **Bonus:** exclude a `.git` folder with `--exclude-dir=.git`.

### 5. Find big or specific files (`find`)

Use `find logs -type f -name "*.log"` to list all log files. Then print the count and the total size (use `os.path.getsize` for the size).

- **Practices:** `-type`, `-name`, iterating over results
- **Bonus:** add `-size +1k` and compare the results.

---

## Easy to Medium

### 6. Safe old-file cleaner (`find -mtime`)

Find files in `logs/` older than 7 days with `find logs -type f -mtime +7 -print0`. Split the output on `"\0"` (this is safe for filenames with spaces). Add a `--dry-run` flag (using `argparse`) that only prints what would be deleted. Without it, delete the files with `os.remove`.

- **Practices:** `-print0`, `argparse`, dry-run pattern
- **Test:** use `touch -d "10 days ago" logs/old.log` to create an old file.

### 7. Sum the traffic (`awk`)

Use `awk` to add up the last column (bytes) of `logs/access.log`:

```python
["awk", "{ sum += $NF } END { print sum }", "logs/access.log"]
```

Print the result in KB. Then use `awk '$(NF-1) >= 500'` to print only requests that returned a 5xx status code.

- **Practices:** passing an awk program as one list item (no quoting problems), `NF`, `END` blocks
- **Bonus:** compute the average bytes per request.

---

## Medium

### 8. Top visitors (pipeline with `Popen`)

Reproduce this pipeline **without** `shell=True`:

```bash
awk '{print $1}' logs/access.log | sort | uniq -c | sort -rn | head -3
```

Chain the processes using `Popen` (`stdout=PIPE` into the next `stdin`). Close each parent-side pipe with `p.stdout.close()` after passing it on.

- **Practices:** `Popen`, `stdin=`/`stdout=`, `communicate()`
- **Bonus:** solve the same problem with `awk` for extraction only and `collections.Counter` in Python. Which version is easier to read?

### 9. Brute-force detector (`grep` + `awk`)

Find the IPs with failed SSH logins in `logs/auth.log`:

```bash
grep "Failed password" logs/auth.log | awk '{print $(NF-2)}' | sort | uniq -c | sort -rn
```

Run it as a chained `Popen` pipeline. Print any IP with **2 or more** failures as `BLOCK: <ip> (<count> attempts)`.

- **Practices:** `grep` into `awk`, `$(NF-2)`, threshold logic, handling the case where `grep` finds nothing (exit code 1)

### 10. Log report generator (everything together)

Write `report.py` that scans the `logs/` folder and writes `report.md` containing:

1. **Files:** each file with its size (from `ls -lh`) sorted by newest first
2. **Errors:** the count of `ERROR` and `WARN` lines per file (`grep -c`)
3. **Traffic:** the total bytes and the top IP from `access.log` (`awk`)
4. **Recent files:** files changed in the last 24 hours (`find -mmin -1440`)
5. **Preview:** the first lines of `app.log` inside a code block (`cat` or `head`)

Requirements:

- Wrap every command in one helper function `sh(cmd) -> str` that handles the `grep` exit-code-1 case and prints a clear message on real errors.
- The script must not crash if `logs/` is empty or missing.

- **Practices:** helper functions, combining all five commands, error handling, generating a Markdown file

---

## Self-check checklist

- [ ] No `shell=True` anywhere
- [ ] Every command is a list of strings
- [ ] `grep` exit code `1` is treated as "no match", not as a crash
- [ ] `FileNotFoundError` (command missing) and `CalledProcessError` (command failed) are both handled
- [ ] Filenames with spaces work (use `-print0` with `find`)
- [ ] Nothing destructive runs without a dry-run option

## Command cheat sheet

| Command | Useful flags |
|---|---|
| `ls` | `-l` long, `-h` human sizes, `-t` by time, `-1` one per line, `-a` hidden |
| `cat` | `-n` number lines, or pass several files to join them |
| `grep` | `-i` ignore case, `-n` line numbers, `-r` recursive, `-c` count, `-v` invert, `-E` regex |
| `find` | `-name`, `-type f/d`, `-size +1M`, `-mtime +7`, `-mmin -60`, `-print0` |
| `awk` | `$1` first column, `$NF` last column, `-F:` custom separator, `BEGIN{}` / `END{}` |