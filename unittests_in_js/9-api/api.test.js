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
