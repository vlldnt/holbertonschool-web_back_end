const calculateNumber = require("./1-calcul");
const assert = require("assert");

describe("Test 3 functions sum sub and div", function () {
  it("Must return the sum of a and b", function () {
    assert.strictEqual(calculateNumber("SUM", 1.4, 4.5), 6);
  });
  it("Must return the sub of a and b", function () {
    assert.strictEqual(calculateNumber("SUBTRACT", 1.4, 4.5), -4);
  });
  it("Must return the div of a and b", function () {
    assert.strictEqual(calculateNumber("DIVIDE", 1.4, 4.5), 0.2);
  });
  it("Must return error", function () {
    assert.strictEqual(calculateNumber("DIVIDE", 1.4, 0), "Error");
  });
});
