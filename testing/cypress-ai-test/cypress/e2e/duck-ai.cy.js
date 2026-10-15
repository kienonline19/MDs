describe('Duck.ai', () => {
	it('Select a model, submits a question, and verifies the answer', () => {
		// 1. Open the website 
		cy.visit('https://duck.ai/', { // Ghi đè biến webdriver ngay trước khi web chạy
			onBeforeLoad(win) {
				Object.defineProperty(win.navigator, 'webdriver', {
					get: () => undefined,
				});
			},
		});
		// cy.visit('https://duck.ai/');

		// 2. Open the model list
		cy.get('[data-testid="model-picker-button"]').should('be.visible').click();

		// 3. Select Mistral Small 4
		cy.contains('[role="menuitemradio"]', 'Mistral').click();

		// 4. Verify the correct model is selected
		cy.get('[data-testid="model-picker-button"]').should('contain.text', 'Mistral');

		// 5. Enter question
		/*
			<textarea name="user-prompt" aria-label="Ask anything privately" class="Pjdc_gGEjnjd_NraQ4DV ir13N7GbOMQ1hsegKnJz" rows="1" inputmode="text" autocomplete="off" placeholder="Ask anything privately" style="height: 56px;"></textarea>
		*/
		cy.get('textarea[name="user-prompt"]')
			.should('be.visible')
			.type(
				'Join the words CYPRESS and OK with an underscore. ' +
				'Reply with only the result, without formatting.', { delay: 50 } // ms - giống người thật 10ms: giống máy
			);

		// 6. Click Send Button
		cy.get('button[aria-label="Ask"]')
			.should('not.be.disabled')
			.click();

		// 7. Wait up to 60 seconds to see the answer
		cy.contains(/^CYPRESS_OK$/, { timeout: 60000 }).should('be.visible'); // timeout (ms) 1s = 1000ms
	})
})