const sinon = require("sinon");
const sendPaymentRequestToApi = require("./3-payment");
const Utils = require("./utils");
const assert = require("assert");

describe("Send payment Request to Api", function () {
  it("should call Utils.calculateNumber with correct arguments", function () {
    const spy = sinon.spy(Utils, "calculateNumber");
    sendPaymentRequestToApi(100, 20);
    assert(spy.calledOnceWithExactly("SUM", 100, 20));
    spy.restore();
  });
});
