import type { SignUpFormType } from '@/types/signup';

export const signupAPI = async (data: SignUpFormType) => {
	const result = await fetch('http://localhost:8000/signup', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(data),
	});
	return result;
};
