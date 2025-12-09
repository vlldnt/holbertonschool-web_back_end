const sendPaymentRequestToApi = require("./5-payment");
const Utils = require("./utils");
const assert = require("assert");
const sinon = require("sinon");

describe("Un Unittest in JS", function () {
  let spy;

  beforeEach(function () {
    spy = sinon.spy(console, "log");
  });

  afterEach(function () {
    spy.restore();
  });

  it("should log the total (120) and once called function", function () {
    sendPaymentRequestToApi(100, 20);
    assert(spy.calledOnceWithExactly("The total is: 120"));
    assert.strictEqual(spy.calledOnce, true);
  });

  it("should log the total (20) and once called function", function () {
    sendPaymentRequestToApi(10, 10);
    assert(spy.calledOnceWithExactly("The total is: 20"));
    assert.strictEqual(spy.calledOnce, true);
  });
});
