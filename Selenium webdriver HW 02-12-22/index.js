const {Builder, By} = require('selenium-webdriver');

async function searching() {
  let driver = await new Builder().forBrowser('chrome').build();

    await driver.get('https://www.thingiverse.com/');
    await driver
    .findElement(By.className('SearchResult__searchResultItem--c4VZk'))
    .findElement(By.className('ThingCardBody__cardBodyWrapper--ba5pu'))
    .click();
}
searching();
