export const signupAPI = async (idToken: string) => {
	const result = await fetch('http://localhost:8000/signup', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify({idToken}),
	});
	return result;
};
