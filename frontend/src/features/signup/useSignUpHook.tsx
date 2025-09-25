import { useState } from 'react';
import { useNavigate } from 'react-router';
import { signupAPI } from '@/api/signup';
import type { SignUpFormType } from '@/types/signup';

const useSignUpHook = () => {
	const navigate = useNavigate();

	const [requestState, setRequestState] = useState({ loading: false, error: false });

	const onSignUpSubmit = async (data: SignUpFormType) => {
		setRequestState({ ...requestState, loading: true });

		const result = await signupAPI(data);

		if (!result) {
			setRequestState({ loading: false, error: true });
			return;
		}
		navigate('/login');
	};
	return {
		requestState,
		onSignUpSubmit,
	};
};

export default useSignUpHook;
