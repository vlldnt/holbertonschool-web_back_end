import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()]).then((resolve) => {
    const [picture, user] = resolve;
    console.log(`${picture.body} ${user.firstName} ${user.lastName}`);
  }).catch(() => console.log('Signup system offline'));
}
