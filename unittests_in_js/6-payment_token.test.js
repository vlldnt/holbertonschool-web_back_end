const getPaymentTokenFromAPI = require("./6-payment_token");
const { expect } = require("chai");

describe("getPaymentTokenFromAPI", () => {
  it("should return the correct data when success is true", (done) => {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        expect(response).to.deep.equal({
          data: "Successful response from the API",
        });
        done();
      })
      .catch((err) => done(err));
  });
});
