console.log('Welcome to Holberton School, what is your name?');
process.stdin.on('data', (data) => {
  process.stdout.write(`Your name is: ${data.toString()}`);
});

process.on('SIGINT', () => {
  console.log('This important software is now closing');
  process.exit();
});
