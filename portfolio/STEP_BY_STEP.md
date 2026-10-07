# Build an ETF research project for internship applications

The goal is to produce evidence that you can collect data, reason statistically, write correct Python, explain limitations, and finish a reproducible project. A good project strengthens an application; no project provides a defensible hiring-success percentage or guarantees an interview.

This guide targets data-analysis, investment/risk-analysis, and junior quantitative-research internships. The supplied code is a starting point. Before claiming ownership on your CV, understand it, make an extension of your own, run real data, and write your own conclusions. Disclose assistance if an employer asks or its rules require it.

## 1. Choose a research question

Use this project title:

**ETF Portfolio Optimization and Risk Analysis with Walk-Forward Backtesting**

Research question:

> Do constrained mean–variance portfolios improve risk-adjusted performance over equal-weight and 60/40 allocations after transaction costs?

Do not set “beat the market” as a required result. The optimizer may lose to a simple baseline. Explaining why is valid research.

| Portfolio | Purpose |
| --- | --- |
| Equal weight | A simple diversified baseline: 1/6 in each ETF |
| 60/40 | A familiar benchmark: 60% SPY, 40% AGG |
| Minimum variance | Uses estimated covariance to minimize portfolio variance |
| Mean–variance | Trades estimated expected return against a variance penalty |

The optimized portfolios are long-only, sum to 100%, and have a 40% target limit per ETF. The 60/40 benchmark uses its own fixed allocation; state that difference when interpreting results. A matched-constraint benchmark is a useful extension.

**Checkpoint:** Explain the question, the four strategies, and the difference between fitting weights and testing them on later returns in one minute.

## 2. Know the prerequisites

You do not need to master every finance topic before beginning. Learn these in the order you encounter them:

| Skill | You must be able to do |
| --- | --- |
| Python | Write functions, use modules, read exceptions, create a virtual environment |
| pandas/NumPy | Work with indexed tables, missing data, vectors, covariance, matrix multiplication |
| Statistics | Distinguish mean, variance, standard deviation, covariance, correlation, and estimation error |
| Finance | Explain simple returns, diversification, rebalancing, drawdown, and the risk-free benchmark |
| Git | Commit meaningful changes, use branches, read a diff, reproduce a previous version |
| SQL | Group data, join tables, and use a window function for a running maximum |

For quantitative research roles, also practice probability, linear algebra, statistics, and coding interviews. For data analyst roles, spend extra time on SQL and communicating decisions. For risk roles, emphasize drawdown, tail risk, scenario analysis, and model limitations.

## 3. Set up the project on Windows

1. Extract `etf-risk-lab.zip` to a folder such as `C:\Users\YOUR_NAME\Documents\etf-risk-lab`.
2. Open that folder in VS Code. The root should contain `run.py`, `README.md`, and `config.json`.
3. Open **Terminal > New Terminal** and select **Command Prompt** for the commands below.
4. Run `py -0p` to list Python installations. Use Python 3.12 for the validated dependency set. If 3.12 is missing, install it from [python.org](https://www.python.org/downloads/).
5. Run:

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate
python --version
python -m pip install -r requirements.txt
```

6. In VS Code, run **Python: Select Interpreter** and choose `.venv\Scripts\python.exe`.
7. Run the offline checks:

```bat
python -m pytest -q
python run.py demo
```

Open `reports/synthetic_demo/report.md`. The figures use invented data and are explicitly labeled. The demo verifies the workflow; its financial numbers are not evidence about ETFs.

If PowerShell blocks activation, you can select Command Prompt or run the virtual-environment interpreter directly:

```bat
.venv\Scripts\python.exe -m pytest -q
.venv\Scripts\python.exe run.py demo
```

**Checkpoint:** All tests pass and three PNG figures, a Markdown report, CSV files, `run.json`, and `research.sqlite` appear.

## 4. Obtain real data

The example universe is deliberately small and all ETF prices are USD-denominated. USD-listed international equity ETFs still carry underlying economic currency exposure.

| Ticker | Exposure used in this project |
| --- | --- |
| SPY | Large US equities |
| EFA | Developed-market equities outside the US and Canada |
| EEM | Emerging-market equities |
| AGG | US investment-grade aggregate bonds |
| GLD | Gold |
| VNQ | US real estate equities/REIT exposure |

The default download covers **2010–2022**. Development evaluation covers **2015–2022**, with earlier data available for a rolling training window. The end date is exclusive.

```bat
python run.py download
```

This does the following:

1. Downloads raw OHLCV, adjusted close, dividends, and splits from Yahoo through yfinance.
2. Validates ticker coverage, finite positive prices, unique dates, and the common US trading calendar.
3. Downloads the French daily factor ZIP and extracts `RF`, dividing percentage values by 100.
4. Requires matching daily RF observations. It does not silently fill missing ETF prices or missing RF.
5. Saves local raw data, validated `prices.csv` / `rf.csv`, and a manifest containing sources, dates, and SHA-256 hashes.

Raw `Close` often omits distributions. The pipeline uses `Adj Close` as a total-return proxy. Do not add dividends again or subtract the current fund expense ratio a second time. Check adjustment conventions when changing providers.

**If Yahoo fails:** a 429 means rate-limited access. Retry later, use the supported Tiingo option, or import suitable data. The program does not silently substitute synthetic data.

For [Tiingo](https://www.tiingo.com/documentation/end-of-day), obtain your own token and check your plan's limits:

```bat
set TIINGO_API_KEY=YOUR_KEY
python run.py download --provider tiingo
```

The token is read from the environment and sent in an authorization header. Do not save it in `config.json` or GitHub. The Tiingo provider uses `adjClose`, validates the same session calendar, and saves raw responses for inspection.

To import another provider's data:

```bat
python run.py import-csv --prices my_prices.csv --rf my_rf.csv --source "Provider name; split and dividend adjusted"
```

`my_prices.csv` needs columns `Date,SPY,EFA,EEM,AGG,GLD,VNQ`. `my_rf.csv` needs `Date,RF`, where `RF` contains **daily decimal returns**, for example `0.0001`. These are file-format examples, not real observations. FRED Treasury yields are annualized percentage yields and cannot be dropped directly into this RF column.

The manifest identifies user-imported data but cannot prove its source or adjustment quality. Cross-check a few dates and large returns against the original provider. Cached data does not refresh automatically; an explicit new download replaces the working cache. Preserve an experiment's data and manifest before refreshing.

**Checkpoint:** All six ETFs cover the requested sessions, no invalid prices remain, and you can explain both data sources and their limitations. `large_return_flags_over_20pct` flags observations for manual inspection; it does not automatically delete them.

## 5. Calculate and understand the basic quantities

Run:

```bat
python examples/01_basics.py
```

The essentials are:

```python
returns = prices.pct_change(fill_method=None).iloc[1:]

annualized_mean = returns.mean() * 252
annualized_volatility = returns.std(ddof=1) * (252 ** 0.5)
annualized_covariance = returns.cov() * 252
correlations = returns.corr()
```

For an adjusted price series, the simple daily return is:

\[
r_t = \frac{P_t}{P_{t-1}} - 1
\]

`pct_change` returns a decimal: `0.01` means 1%. Correlate **returns**, not price levels. An annualized arithmetic mean is an expected-return estimate; it is not the CAGR actually earned over the period.

Portfolio mean and variance are:

\[
\mu_p=w^\top\mu, \qquad \sigma_p^2=w^\top\Sigma w
\]

`w` is the vector of portfolio weights, `mu` the expected-return vector, and `Sigma` the covariance matrix. Covariance, not just each ETF's volatility, determines diversification benefits.

The 252-session annualization is a conventional approximation; serial dependence can make square-root-of-time scaling misleading. Record the convention instead of treating it as a universal identity.

**Checkpoint:** Explain why two volatile assets can produce a less volatile portfolio and why a large historical mean return is an uncertain forecast.

## 6. Understand the optimizers

The included implementation is `etf_lab/portfolios.py`. It uses SciPy directly so the objective and constraints remain visible.

Minimum variance:

\[
\min_w w^\top\Sigma w
\]

Mean–variance utility:

\[
\max_w w^\top\mu-\frac{\gamma}{2}w^\top\Sigma w
\]

Both optimized strategies obey:

\[
\sum_i w_i=1, \qquad 0\leq w_i\leq0.40
\]

`gamma=5` is the predeclared default risk-aversion coefficient. Higher gamma places more emphasis on variance. Annualized means and covariances are used consistently. The 40% cap is a modeling choice, not an established best allocation.

The default covariance estimator is Ledoit–Wolf shrinkage. The sample mean is also shrunk 50% toward the cross-sectional mean, with that coefficient fixed in advance. With fully invested portfolios, the common mean component is constant across feasible weights; this reduces the influence of differences in estimated means. Neither choice guarantees better future performance.

Here is a small standalone minimum-variance example:

```python
import numpy as np
from scipy.optimize import minimize

# 'history' must contain only returns observed before execution.
cov = history.cov().to_numpy() * 252
n = len(history.columns)

solution = minimize(
    fun=lambda w: w @ cov @ w,
    x0=np.full(n, 1 / n),
    method="SLSQP",
    bounds=[(0, 0.40)] * n,
    constraints=[{"type": "eq", "fun": lambda w: w.sum() - 1}],
)

if not solution.success:
    raise RuntimeError(solution.message)

weights = solution.x
```

This snippet requires a feasible universe, such as the six ETFs used here. The actual project additionally checks feasibility and solver output and uses the configured covariance estimator.

**Checkpoint:** Explain the objective, why weights add to one, the cap, solver failure handling, and the difference between minimum variance and maximum Sharpe. Maximum Sharpe is an optional extension; it is not the supplied mean–variance objective.

## 7. Understand the time sequence before running a backtest

Example: the first trading session in a new month is Tuesday.

| Moment | What is allowed |
| --- | --- |
| Monday close | Latest information available to the signal |
| Before Tuesday's execution | Fit on the most recent 756 daily returns ending Monday |
| Tuesday close | Existing holdings earn Tuesday's return; execute the previously determined target and charge costs |
| Wednesday close | The new allocation earns its first close-to-close ETF return |

The code deliberately waits until the next session's close. A signal that uses Tuesday's closing price cannot earn Tuesday's already-finished return.

Between rebalances, weights drift:

\[
w_{i,t}^{\mathrm{pretrade}}=
\frac{w_{i,t-1}(1+r_{i,t})}{1+r_{p,t}^{\mathrm{gross}}}
\]

Keeping weights constant every day would imply daily rebalancing. The project instead updates weights using relative asset growth.

Transaction costs are charged on buys **plus** sells. Selling 10% and buying 10% trades 20% of NAV, so a 10 bps cost rate costs about 0.02% of NAV before the small funding adjustment. A purchase of 100% from cash also pays costs.

The implementation solves for post-fee investable wealth so holdings plus fees exactly fit the budget. It does not just subtract an arbitrary fee while pretending the same money remains invested.

**Checkpoint:** Hand-calculate a two-asset, two-day portfolio with a rebalance. Explain what would change if execution were at the next open instead of the close; that would require appropriate open-price and overnight-return accounting.

## 8. Run the development backtest

```bat
python run.py backtest
```

Outputs are in `reports/development/`:

| Output | What it demonstrates |
| --- | --- |
| `report.md` | A readable summary and disclosed assumptions |
| `metrics.csv` | Comparable strategy statistics |
| `performance.png` | Growth and drawdowns after costs |
| `correlations.png` | Return relationships during the evaluation period |
| `allocations.png` | Allocation drift and monthly changes |
| `*_ledger.csv` | Daily gross/net returns, equity, cost, and traded notional |
| `*_rebalances.csv` | Signal date, execution date, training window, and target weights |
| `run.json` | Parameters, source manifest, package versions, and code hashes |
| `research.sqlite` | SQL-accessible results |

The evaluation-period correlation chart is descriptive only; it is never used to fit earlier weights.

Report at least:

- CAGR: compounded growth per year using the stated 252-session convention.
- Annualized volatility: sample standard deviation of daily net returns times the square root of 252.
- Sharpe: annualized mean daily excess return divided by its sample standard deviation.
- Sortino: mean daily excess return divided by downside deviation, consistently annualized.
- Maximum drawdown: worst fall from a previous wealth peak, including the initial wealth of 1.
- Calmar: CAGR divided by absolute maximum drawdown, undefined when the denominator is zero.
- Historical daily 95% VaR and expected shortfall: descriptive lower-tail loss measures.
- Annual traded notional/NAV: buys plus sells, including entry, normalized by evaluation years.

An undefined ratio is not zero. Historical VaR is not a guarantee of a maximum future loss. Do not rank portfolios by CAGR alone or select the best retrospective Sharpe without accounting for the selection process.

**Checkpoint:** Write three observations and at least two limitations from your actual real-data report, even if the optimizer does not win.

## 9. Make one research extension your own

Choose one main question before changing settings. Avoid testing many combinations until something looks impressive.

**Recommended extension: How sensitive are the conclusions to transaction costs and covariance estimation?**

Keep all other settings fixed and compare:

```bat
python run.py backtest --cost-bps 0 --out reports/cost_0
python run.py backtest --cost-bps 25 --out reports/cost_25
python run.py backtest --covariance sample --out reports/sample_covariance
```

The 0, 10, and 25 bps cases are sensitivity scenarios, not estimates of your actual broker's execution costs. These costs combine commissions, spread, and slippage into one simple parameter.

Record what changed and why. A useful finding could be that an apparent performance advantage vanishes after costs, or that estimated weights change substantially under a small modeling change.

Optional later extensions, after the basic version is correct:

- A matched-constraint benchmark to separate the effect of the optimizer from allocation restrictions.
- A training-window efficient frontier, explicitly labeled in-sample.
- Maximum Sharpe with a documented, historically available risk-free assumption.
- Rolling volatility and subperiod analysis of 2020 and 2022, identified as retrospective descriptions.
- Block-bootstrap uncertainty intervals for performance differences, with justified block length and preserved temporal dependence.
- A simple dashboard once the methodology and results are stable.

**Checkpoint:** Present one hypothesis, one controlled comparison, its observed result, and an alternative explanation.

## 10. Reserve a final evaluation period

Use 2015–2022 for development. Before inspecting final-period performance, freeze the universe, feature choices, objectives, risk aversion, lookback, caps, cost assumptions, and reporting metrics.

Record a Git commit or tag and a short experiment plan. Then download the later data:

```bat
python run.py download --end 2026-01-01
python run.py backtest --test-start 2023-01-01 --test-end 2026-01-01 --out reports/final_evaluation
```

If using Tiingo, add `--provider tiingo` to the download command. This final evaluation starts all portfolios from the same initial cash balance and still fits each month's parameters using only earlier observations. Rolling refitting during 2023–2025 is allowed because the refitting rule is frozen.

The final period is not a source of new hyperparameter choices. If you change the method after seeing it, disclose that it became development data. If you already explored these years extensively, do not describe them as pristine holdout data; use a later genuinely unseen period or disclose the limitation.

A fixed universe chosen today still creates selection/survival bias. Chronological splitting alone does not remove it. The French factor dataset and vendor histories are revised sources, not point-in-time archives.

**Checkpoint:** A reviewer can trace every final result to a frozen configuration and a dataset snapshot.

## 11. Demonstrate SQL and testing skills

The pipeline produces a SQLite database with `daily_performance`, `end_weights`, and `rebalances` tables. Read `sql/analysis.sql` for four working query examples.

For example, to query it with Python:

```python
import sqlite3
import pandas as pd

with sqlite3.connect("reports/development/research.sqlite") as connection:
    result = pd.read_sql_query("""
        SELECT strategy, substr(Date, 1, 4) AS year,
               SUM(traded_notional) AS traded_notional_per_nav
        FROM daily_performance
        GROUP BY strategy, substr(Date, 1, 4)
        ORDER BY strategy, year
    """, connection)

print(result)
```

Understand the tests instead of memorizing their count. The suite checks entry costs, a full asset switch, weight drift, a hand-calculated minimum-variance solution, no use of the execution day's return in the signal, invariance to changes in future prices, missing observations, RF units, drawdown from starting wealth, and cache integrity.

CI runs tests on deterministic inputs, not live Yahoo calls. This separates software failures from a provider outage. The workflow is included, but its successful execution on your own GitHub repository is something you must verify after pushing.

**Checkpoint:** Add one meaningful test for your extension and explain a real bug that it would catch.

## 12. Prepare the GitHub repository

Do not publish the unmodified starter as a finished research result. Customize the README to state your question, your changes, your evidence, and what remains incomplete.

1. Create an empty repository named `etf-risk-lab` on GitHub. Choose your desired visibility. Do not add a second README during creation.
2. In the local project folder, use:

```bat
git init
git add .
git status
git commit -m "Add ETF research pipeline and accounting tests"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/etf-risk-lab.git
git push -u origin main
```

3. Replace `YOUR_USERNAME` with your actual GitHub username. Git may ask you to sign in using its normal credential flow.
4. Verify that `.venv`, API keys, and raw vendor data are absent from the staged files. The provided `.gitignore` excludes generated results as well.
5. Review the Actions tab and fix any failing workflow.
6. Select a small set of your own permitted derived charts and a written research note for the README. To commit intentionally selected outputs, copy them into a new `docs/results/` folder after reviewing data usage rights. Do not remove all ignore rules just to publish one figure.
7. Commit your own research changes in understandable steps. Do not manufacture a history of work you did not do.

A strong README should let a reviewer answer these questions quickly:

- What question did you study?
- Where did the data come from, and what period is covered?
- What did you implement yourself or materially improve?
- How did you prevent using future information?
- What were the actual results after costs, compared with baselines?
- What are the limitations and one next experiment?
- How can someone reproduce the work?

**Checkpoint:** A fresh environment can follow your README and reproduce the same analysis from the documented cached data version, subject to source access and licensing.

## 13. Write the research note and prepare a five-minute demonstration

Use `reports/research_note_template.md`. Keep the completed note about one to two pages. Include one comparison table and two or three relevant figures.

Suggested demonstration:

| Time | Explain |
| --- | --- |
| 0:00–0:40 | The research question and why the baselines matter |
| 0:40–1:30 | Sources, adjusted prices, and one validation check |
| 1:30–2:30 | Objectives, constraints, execution timing, and costs |
| 2:30–3:40 | Your actual results and controlled extension |
| 3:40–4:30 | A limitation, failed idea, or result you did not expect |
| 4:30–5:00 | Tests, reproducibility, and one justified next step |

Be ready to answer:

1. Why analyze return correlations instead of price correlations?
2. How is CAGR different from an annualized arithmetic mean?
3. Why can a mean–variance optimizer produce unstable weights?
4. How does shrinkage change your estimate, and what assumption does it add?
5. Which exact date's information determines a rebalance?
6. How does monthly rebalancing differ from constant daily weights?
7. Why include entry costs, and how are buys/sells counted?
8. Why is the French RF series used for evaluation instead of forecasting?
9. How could your universe introduce survivorship bias?
10. What did a simple baseline do better than the optimized portfolios?
11. What result changed under your sensitivity experiment?
12. What would you change if you had point-in-time data and realistic execution records?

## 14. Use the project in applications

The best improvement to your chances is matching credible evidence to the role. There is no universal “best acceptance rate” obtainable from one project.

| Target role | Emphasize | Additional preparation |
| --- | --- | --- |
| Data analyst intern | API ingestion, validation, SQL, clear charts, business conclusions | SQL joins/window functions, Excel/BI as requested |
| Risk/investment analyst intern | Covariance, drawdown, tail risk, costs, benchmarks, limits | Finance concepts and written interpretation |
| Quant research intern | Statistical assumptions, optimization, time ordering, controlled experiments | Probability, statistics, linear algebra, coding interviews |
| Python/data engineering intern | Modular code, tests, schema validation, caching, reproducibility | Data structures, APIs, databases, robust error handling |

For perspective, Jane Street's quantitative research internship description emphasizes Python, mathematical reasoning, experiment design, time-series work, and communication. That is an example of relevant skills, not a claim that this starter meets every requirement of a highly selective quant firm. Use the actual job description for each application.

CV bullet templates — use only after doing and verifying the work:

> Built a Python research pipeline for six ETFs using adjusted prices, calendar validation, and versioned data snapshots; compared equal-weight, 60/40, minimum-variance, and mean–variance portfolios in a rolling monthly backtest.

> Implemented transaction-cost accounting, allocation drift, SQL reporting, and automated tests for timing and data integrity; evaluated [YOUR EXPERIMENT] over [YOUR VERIFIED PERIOD] and reported [YOUR ACTUAL FINDING].

Replace bracketed fields with facts. Do not invent a return improvement, Sharpe ratio, speedup, user count, or hiring outcome. If the project is unfinished, describe the implemented portion and its current status.

Suggested application routine:

1. Pick one primary role family and one adjacent family.
2. Review a small set of actual openings for degree/enrollment requirements, location, work authorization, language, dates, and requested skills.
3. Maintain a simple tracker: company, role, link, deadline, eligibility, tailored CV date, application date, reply, next action.
4. Tailor your CV's project bullets to the role using truthful terminology from its description.
5. Link a readable README and a short demonstration. Make the evidence accessible in a few clicks.
6. Send a manageable number of well-matched applications each week; begin once the real-data version and explanation are ready instead of adding features indefinitely.
7. Practice explaining and modifying the code without relying on memorized answers.
8. Use the response pattern to diagnose problems: few callbacks may indicate targeting/CV issues; interviews without offers may indicate gaps in explanation, coding, or fundamentals. Small samples do not establish a precise success probability.

## Suggested four-week schedule

This is an estimate for someone already comfortable with basic Python, around 8–12 hours per week. Add time if pandas, linear algebra, or finance is new.

| Week | Work | Deliverable |
| --- | --- | --- |
| 1 | Setup, data acquisition/validation, returns, volatility, correlations | Working ingestion and a short data-quality note |
| 2 | Baselines, optimizer, timing, costs, accounting tests | Auditable development backtest |
| 3 | Controlled extension, frozen design, final evaluation | Tables, figures, and evidence-backed findings |
| 4 | README, research note, SQL, demonstration, role-specific CV | A reviewed repository and tailored applications |

Apply when you can explain the project clearly and support its claims. A complicated dashboard is optional; correctness and reasoning are the core evidence.

## Sources and further reading

Documentation checked on 2026-10-03. Provider availability, terms, packages, and job listings can change.

- [yfinance download parameters](https://ranaroussi.github.io/yfinance/reference/api/yfinance.download.html)
- [yfinance usage notice](https://ranaroussi.github.io/yfinance/)
- [Tiingo end-of-day fields and adjustment methodology](https://www.tiingo.com/documentation/end-of-day)
- [French Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html)
- [French factor construction and RF source](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/f-f_factors.html)
- [SciPy SLSQP](https://docs.scipy.org/doc/scipy/reference/optimize.minimize-slsqp.html)
- [scikit-learn Ledoit–Wolf](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html)
- [pandas-market-calendars](https://pandas-market-calendars.readthedocs.io/en/latest/usage.html)
- [GitHub setup-python](https://github.com/actions/setup-python)
- [GitHub checkout](https://github.com/actions/checkout)
- [Example quant research internship requirements](https://www.janestreet.com/join-jane-street/position/8498547002/)
