import { createUserWithEmailAndPassword } from 'firebase/auth';
import { signupAPI } from '@/api/signup';
import { auth } from '@/lib/firebase';

type Props = {
	email: string;
	password: string;
};

export const signUp = async ({ email, password }: Props) => {
	try {
		const result = await createUserWithEmailAndPassword(auth, email, password);
		const idToken = await result.user.getIdToken();
		const signUpResult = await signupAPI(idToken);
		if (!signUpResult.ok) {
			return { status: false };
		}
		return { status: true };
	} catch {
		return { status: false };
	}
};
