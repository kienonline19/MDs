/// <reference types="cypress"/>

// Cypress.on('uncaught:exception', (err, runnable) => {
//     if(err.message.includes('ResizeObserver loop')){
//         return false;
//     }
// });

const input = 'textarea[aria-label="Ask anything privately"]';
const ask = 'button[aria-label="Ask"]'

const suggestions = '[role="tab"][aria-label="Open chat suggestions"]';

describe("Duck.ai - 5 UI Practice tests", {

    testIsolation: true,
    defaultCommandTimeout: 15000,
    viewportWidth: 1200,
    viewportHeight: 900
}, () => {
    beforeEach(() => {
        cy.visit("https://duck.ai/", {
            onBeforeLoad(win) {
                Object.defineProperty(win.navigator, 'webdriver', {
                    get: () => undefined
                }); 
            }
        });
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

        cy.get('button[aria-label="Close panel"]').should("be.visible").click();
        cy.get(suggestions).should("have.attr", "aria-selected", "false");
    });

    it("5 - hides and shows the sidebar", () => {
        cy.get('button[aria-label^="Hide sidebar"]').click();
        cy.get('button[aria-label^="Show sidebar"]').should("be.visible");

        cy.wait(500);

        cy.get('button[aria-label^="Show sidebar"]').click();
        cy.get('button[aria-label^="Hide sidebar"]').should("be.visible");
    });
});