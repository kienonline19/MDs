## Syntax explained

| Syntax | Meaning |
| --- | --- |
| `describe(...)` | Groups the five tests. Its configuration sets an independent browser state, desktop viewport, and a 15-second command timeout. |
| `beforeEach(...)` | Opens Duck.ai before each test. |
| `it(...)` | Defines one test case. |
| `cy.visit(url)` | Opens the page. |
| `cy.get(selector)` | Finds an element with a CSS selector. |
| `[aria-label="Ask"]` | Matches an attribute exactly. |
| `[aria-label^="Hide sidebar"]` | Matches an attribute beginning with this text, allowing the keyboard-shortcut suffix to vary. |
| `.type(message)` / `.clear()` | Enters text / removes text from the textarea. |
| `.should("have.value", message)` | Checks an input's current value. |
| `.should("be.disabled")` | Checks that a button cannot be used. |
| `.should("not.be.disabled")` | Checks that a button is enabled. |
| `.click()` | Clicks an interactive control. |
| `.should("have.attr", "aria-selected", "true")` | Checks that the suggestions tab is selected. ARIA attribute values are strings. |
| `const message = "..."` | Declares the sample text; TypeScript infers its string type. |

DOM assertions retry until their condition passes or the timeout is reached. The 15-second setting is a maximum wait, not a fixed delay. Re-querying with `cy.get(...)` after an action avoids relying on a DOM element that may have been replaced.

## Expected results

| Test | Expected result |
| --- | --- |
| 1 | Page title contains Duck.ai; the composer is enabled and Ask is visible. |
| 2 | Empty composer; Ask disabled. |
| 3 | Typed text enables Ask; clearing the text disables it again. |
| 4 | Suggestions tab becomes selected, then unselected when its panel is closed. |
| 5 | Hiding the sidebar reveals Show sidebar; clicking it restores Hide sidebar. |

Sources: [Duck.ai](https://duck.ai/), [Cypress visit](https://docs.cypress.io/api/commands/visit), [type](https://docs.cypress.io/api/commands/type), [clear](https://docs.cypress.io/api/commands/clear), [should](https://docs.cypress.io/api/commands/should).

