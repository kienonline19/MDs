# 5 Cypress Tests for Duck.ai (TypeScript)

These beginner UI tests use controls inspected on the English Duck.ai page on 15 October 2026. They cover page loading, empty-input validation, typing/clearing, a suggestions panel, and sidebar navigation. They do not submit a prompt to a model.

**Validation:** Selectors and the interactions were inspected in a live browser; the spec was syntax-checked. This is not a completed Cypress run. Site experiments, localization, consent screens, or human-verification challenges may change what your Cypress browser sees.

## Run in your existing project

In the Cypress Real World App repository, create `cypress/tests/ui/duck-ai.spec.ts`. In a standard Cypress project, use `cypress/e2e/duck-ai.cy.ts` instead. Keep these tests in a separate spec from tests of your local app.

Copy the complete spec below. All commands are built into Cypress; no RWA custom commands or extra testing plugins are needed.

```typescript
/// <reference types="cypress" />

const input = 'textarea[aria-label="Ask anything privately"]';
const ask = 'button[aria-label="Ask"]';
const suggestions = '[role="tab"][aria-label="Open chat suggestions"]';

describe("Duck.ai - 5 UI practice tests", {
  testIsolation: true,
  defaultCommandTimeout: 15000,
  viewportWidth: 1280,
  viewportHeight: 900,
}, () => {
  beforeEach(() => {
    cy.visit("https://duck.ai/");
    cy.get(input).should("be.visible");
  });

  it("1 - displays the chat page", () => {
    cy.title().should("include", "Duck.ai");
    cy.get(input).should("be.enabled");
    cy.get(ask).should("be.visible");
  });

  it("2 - disables Ask when the message is empty", () => {
    cy.get(input).should("have.value", "");
    cy.get(ask).should("be.disabled");
  });

  it("3 - enables Ask after typing and disables it after clearing", () => {
    const message = "Explain what an API is in one sentence.";

    cy.get(input).type(message);
    cy.get(input).should("have.value", message);
    cy.get(ask).should("not.be.disabled");

    cy.get(input).clear();
    cy.get(input).should("have.value", "");
    cy.get(ask).should("be.disabled");
  });

  it("4 - opens and closes chat suggestions", () => {
    cy.get(suggestions).click();
    cy.get(suggestions).should("have.attr", "aria-selected", "true");
    cy.get('button[aria-label="Close panel"]').should("be.visible");

    cy.get('button[aria-label="Close panel"]').click();
    cy.get(suggestions).should("have.attr", "aria-selected", "false");
  });

  it("5 - hides and shows the sidebar", () => {
    cy.get('button[aria-label^="Hide sidebar"]').click();
    cy.get('button[aria-label^="Show sidebar"]').should("be.visible");

    cy.get('button[aria-label^="Show sidebar"]').click();
    cy.get('button[aria-label^="Hide sidebar"]').should("be.visible");
  });
});
```

Open the runner from the project root:

```bash
npx cypress open --e2e --config baseUrl=https://duck.ai
```

The CLI base URL overrides the local-app base URL for this run, so Cypress does not need the RWA server just to check its configured base URL. Select Chrome and open only the Duck.ai spec. A standard project must already have Cypress and TypeScript installed and E2E setup completed.

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

If your browser shows a consent screen or CAPTCHA, the page is not in the state these tests expect. A timeout in that situation does not establish a defect in the chat UI. Do not add a blanket `uncaught:exception` handler returning `false` to hide all errors; inspect the actual failure first.

Sources: [Duck.ai](https://duck.ai/), [Cypress visit](https://docs.cypress.io/api/commands/visit), [type](https://docs.cypress.io/api/commands/type), [clear](https://docs.cypress.io/api/commands/clear), [should](https://docs.cypress.io/api/commands/should).

