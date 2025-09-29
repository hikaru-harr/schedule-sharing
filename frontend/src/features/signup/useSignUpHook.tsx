import { useState } from 'react';
import { useNavigate } from 'react-router';
import { signUp } from '@/interface/signup';
import type { SignUpFormType } from '@/types/signup';

const useSignUpHook = () => {
	const navigate = useNavigate();

	const [requestState, setRequestState] = useState({ loading: false, error: false });

	const onSignUpSubmit = async (data: SignUpFormType) => {
		setRequestState({ error: false, loading: true });
		const result = await signUp({ ...data });
		if (result.status) {
			navigate('/login');
			setRequestState({ loading: false, error: false });
		} else {
			setRequestState({ loading: false, error: true });
		}
	};
	return {
		requestState,
		onSignUpSubmit,
	};
};

export default useSignUpHook;
