const { defineConfig } = require("cypress");

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
      // Tắt cờ tự động hóa từ gốc của chrome
      // on("before:browser:launch", (browser = {}, launchOptions) => {
      //   if (browser.family === "chromium" && browser.name !== "electron") {
      //     launchOptions.args.push("--disable-blink-features=AutomationControlled");
      //   }
      //   return launchOptions;
      // });
    },
  },
});
