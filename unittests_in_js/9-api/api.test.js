const request = require("request");
const { expect } = require("chai");

describe("Test the express app.js", function () {
  it("test the request response", function (done) {
    request("http://localhost:7865/", function (error, response, body) {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });
  it("Testing the correct body", function (done) {
    request("http://localhost:7865", function (error, res, body) {
      expect(body).to.equal("Welcome to the payment system");
      done();
    });
  });
});

describe("Test the cart page", function () {
  it("Testing the params is number", function (done) {
    request("http://localhost:7865/cart/12", function (error, res, body) {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal("Payment methods for cart 12");
      done();
    });
  });
  it("Testing the params not number", function (done) {
    request("http://localhost:7865/cart/Salut", function (error, res, body) {
      expect(res.statusCode).to.equal(404);
      expect(body).to.equal("Id not found");
      done();
    });
  });
});
