import calculateNumber from "./0-calcul.js";
import assert from "assert";

describe("Sum two integers", function () {
  it("Must returns the sum of the two integers", function () {
    assert.strictEqual(calculateNumber(1, 1), 2);
  });
});
