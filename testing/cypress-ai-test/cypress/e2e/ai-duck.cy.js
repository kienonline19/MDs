/// <reference types="cypress" />

const input = '[data-testid="duckai-chat-input"] textarea';
const ask = 'button[aria-label="Ask"]';
const stop = 'button[aria-label="Stop generating"]';
const picker = '[data-testid="model-picker-button"]';
const chat = { method: "POST", pathname: "/duckchat/v1/chat" };

describe("Duck.ai: simple → medium", {
  testIsolation: true,
  defaultCommandTimeout: 15000,
  viewportWidth: 1280,
  viewportHeight: 900,
}, () => {
  beforeEach(() => {
    cy.visit("https://duck.ai/");
    cy.get(input).should("be.visible");
  });

  // 1. Check the initial input.
  it("shows an empty message input", () => {
    cy.get(input).should("have.value", "");
  });

  // 2. Validate the initial button state.
  it("disables Ask when the input is empty", () => {
    cy.get(ask).should("be.disabled");
  });

  // 3. Check typing.
  it("enables Ask after typing", () => {
    cy.get(input).type("Hello");
    cy.get(ask).should("be.enabled");
  });

  // 4. Check clearing.
  it("disables Ask after clearing the input", () => {
    cy.get(input).type("Hello");
    cy.get(input).clear();
    cy.get(ask).should("be.disabled");
  });

  // 5. Practice keyboard combinations.
  it("inserts a newline with Shift+Enter", () => {
    cy.get(input)
      .type("First line{shift+enter}Second line")
      .should("have.value", "First line\nSecond line");
    cy.get('[data-testid="user-message"]').should("not.exist");
  });

  // 6. Open and close a panel.
  it("opens and closes chat suggestions", () => {
    const tab = '[role="tab"][aria-label="Open chat suggestions"]';
    cy.get(tab).click().should("have.attr", "aria-selected", "true");
    cy.get('button[aria-label="Close panel"]').click();
    cy.get(tab).should("have.attr", "aria-selected", "false");
  });

  it("hides and restores the sidebar", () => {
    const hide = 'button[aria-label^="Hide sidebar"]';
    const show = 'button[aria-label^="Show sidebar"]';

    cy.get(hide).click();
    cy.get(hide).should("not.exist");

    cy.get(show).should("be.visible").click();
    cy.get(show).should("not.exist");

    cy.get(hide).should("be.visible");
  });

  // 8. Select an available model without hard-coding its name.
  it("selects a different model", () => {
    cy.get(picker).click();
    cy.get('[data-testid^="model-picker-row-"][aria-checked="false"]')
      .not('[aria-disabled="true"]')
      .first()
      .then(($option) => {
        const id = $option.attr("data-testid");
        cy.wrap($option).click();
        cy.get(picker).click();
        cy.get(`[data-testid="${id}"]`)
          .should("have.attr", "aria-checked", "true");
      });
  });

  // 9. Check a real browser request and the resulting UI.
  it("sends a message and displays an answer", () => {
    const prompt = "Explain an API in one short sentence.";
    cy.intercept(chat).as("chat");

    cy.get(input).type(prompt);
    cy.get(ask).click();

    cy.wait("@chat", { requestTimeout: 30000, responseTimeout: 120000 })
      .then(({ request, response }) => {
        expect(response?.statusCode).to.equal(200);
        expect(JSON.stringify(request.body)).to.include(prompt);
      });

    cy.get('[data-testid="user-message"]').last().should("contain.text", prompt);
    cy.get('div[data-activeresponse="true"]').last()
      .find("p").invoke("text").should("match", /\S/);
    cy.get(stop).should("be.disabled");
  });

  // 10. Simulate a retryable server error.
  it("shows an error and retry button after HTTP 429", () => {
    cy.intercept({ ...chat, times: 1 }, {
      statusCode: 429,
      headers: { "content-type": "application/json" },
      body: { action: "error", status: 429, type: "ERR_RATE_LIMIT" },
    }).as("limited");

    cy.get(input).type("Say hello.");
    cy.get(ask).click();

    cy.wait("@limited", { requestTimeout: 30000 })
      .its("response.statusCode").should("eq", 429);
    cy.contains('[role="alert"]', /too many requests/i).should("be.visible");
    cy.contains("button", /^Try Again$/).should("be.visible");
    cy.get(stop).should("be.disabled");
  });
});