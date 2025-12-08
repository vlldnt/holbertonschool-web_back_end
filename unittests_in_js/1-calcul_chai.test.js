const calculateNumber = require("./1-calcul");
const chai = require("chai");
const expect = chai.expect;

describe("Test 3 functions sum sub and div", function () {
  it("Must return the sum of a and b", function () {
    const result = calculateNumber("SUM", 1.4, 4.5);
    expect(result).to.equal(6);
  });
  it("Must return the sub of a and b", function () {
    const result = calculateNumber("SUBTRACT", 1.4, 4.5);
    expect(result).to.equal(-4);
  });
  it("Must return the div of a and b", function () {
    const result = calculateNumber("DIVIDE", 1.4, 4.5);
    expect(result).to.equal(0.2);
  });
  it("Must return error", function () {
    const result = calculateNumber("DIVIDE", 1.4, 0);
    expect(result).to.equal("Error");
  });
  it("Must throw an error", function () {
    expect(() => calculateNumber("MULTIPLY", 1.4, 3)).to.throw(
      "Calcul not found."
    );
  });
});
