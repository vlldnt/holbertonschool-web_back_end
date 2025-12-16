import createPushNotificationsJobs from "./8-job";
import kue from "kue";
import { expect } from "chai";

const queue = kue.createQueue();

describe("createPushNotificationsJobs", () => {
  before(() => {
    queue.testMode.enter();
  });

  after(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it("should display an error message if jobs is not an array", () => {
    expect(() => createPushNotificationsJobs("not an array", queue)).to.throw(
      "Jobs is not an array"
    );
  });
  it("should display an error message if jobs is not an array 2", () => {
    expect(() => createPushNotificationsJobs(2, queue)).to.throw(
      "Jobs is not an array"
    );
  });
  it("should display an error message if jobs is an object", () => {
    expect(() => createPushNotificationsJobs({ hello: "hello", value: 2 }, queue)).to.throw(
      "Jobs is not an array"
    );
  });

  it("should create two new jobs to the queue", () => {
    const jobs = [
      {
        phoneNumber: "4153518780",
        message: "This is the code 1234 to verify your account",
      },
      {
        phoneNumber: "4153518781",
        mess: "This is the code 4562 to verify your account",
      },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);

    expect(queue.testMode.jobs[0].type).to.equal("push_notification_code_3");
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
    expect(queue.testMode.jobs[0].data.phoneNumber).to.equal("4153518780");
    expect(queue.testMode.jobs[0].data.message).to.equal("This is the code 1234 to verify your account");
    
    expect(queue.testMode.jobs[1].type).to.equal("push_notification_code_3");
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
    expect(queue.testMode.jobs[1].data.phoneNumber).to.equal("4153518781");
    expect(queue.testMode.jobs[1].data.mess).to.equal("This is the code 4562 to verify your account");
  });
});
