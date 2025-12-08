const calculateNumber = require("./0-calcul");
const assert = require("assert");

describe("Sum two integers", function () {
  it("Must returns the sum of the two integers", function () {
    assert.strictEqual(calculateNumber(1, 1), 2);
  });
});
