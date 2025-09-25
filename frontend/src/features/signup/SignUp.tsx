import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';
import InputForm from '@/components/InputForm';
import { Button } from '@/components/ui/button';
import { Form } from '@/components/ui/form';
import { type SignUpFormType, signUpFormSchema } from '@/types/signup';
import useSignUpHook from './useSignUpHook';

function SignUp() {
	const signUpForm = useForm<SignUpFormType>({
		resolver: zodResolver(signUpFormSchema),
		defaultValues: {
			email: '',
			password: '',
		},
	});
	
	const { onSignUpSubmit } = useSignUpHook();

	return (
		<div className="w-xl mx-auto mt-[60px]">
			<h1 className="text-2xl text-center">SignUp</h1>
			<Form {...signUpForm}>
				<form onSubmit={signUpForm.handleSubmit(onSignUpSubmit)} className="mt-4 space-y-4">
					<InputForm
						control={signUpForm.control}
						name="email"
						label="Email"
						type="email"
						placeholder="example@.com"
					/>
					<InputForm
						control={signUpForm.control}
						name="password"
						label="Password"
						type="password"
						placeholder="********"
					/>
					<Button className="w-full">SIGNUP</Button>
				</form>
			</Form>
		</div>
	);
}

export default SignUp;
