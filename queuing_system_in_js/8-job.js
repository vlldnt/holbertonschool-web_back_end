function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error("Jobs is not an array");
  }

  jobs.forEach((job) => {
    const newJob = queue
      .create("push_notification_code_3", job)
      .save((error) => {
        if (!error) {
          console.log(`Notification job created: ${newJob.id}`);
        }
      });

    newJob.on("complete", () => {
      console.log(`Notification job ${newJob.id} completed`);
    });

    newJob.on("fail", (error) => {
      console.log(`Notification job ${newJob.id} failed: ${error}`);
    });

    newJob.on("progress", () => {
      console.log(`Notification job ${newJob.id} ${newJob.prog}% complete`);
    });
  });
}

export default createPushNotificationsJobs;
