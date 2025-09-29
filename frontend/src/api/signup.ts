export const signupAPI = async (idToken: string) => {
	const result = await fetch('http://localhost:8000/signup', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			Authorization: `Bearer ${idToken}`,
		},
		body: JSON.stringify({ idToken }),
	});
	return result;
};
