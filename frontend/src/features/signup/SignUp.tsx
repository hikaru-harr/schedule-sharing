import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';
import { z } from 'zod';
import { Button } from '@/components/ui/button';
import {
	Form,
	FormControl,
	FormDescription,
	FormField,
	FormItem,
	FormLabel,
	FormMessage,
} from '@/components/ui/form';
import { Input } from '@/components/ui/input';

const signUpFormSchema = z.object({
	email: z.email(),
	password: z.string(),
});

type SignUpFormType = z.infer<typeof signUpFormSchema>;

function SignUp() {
	const signUpForm = useForm<SignUpFormType>({
		resolver: zodResolver(signUpFormSchema),
		defaultValues: {
			email: '',
			password: '',
		},
	});

	const onSignUpSubmit = (data: SignUpFormType) => {
		console.log(data);
	};

	return (
		<div className="w-xl mx-auto mt-[60px]">
			<h1 className="text-2xl text-center">SignUp</h1>
			<Form {...signUpForm}>
				<form onSubmit={signUpForm.handleSubmit(onSignUpSubmit)} className="mt-4 space-y-4">
					<FormField
						control={signUpForm.control}
						name="email"
						render={({ field }) => (
							<FormItem>
								<FormLabel>Email</FormLabel>
								<FormControl>
									<Input placeholder="example@.com" type="email" {...field} />
								</FormControl>
								<FormMessage />
							</FormItem>
						)}
					/>
					<FormField
						control={signUpForm.control}
						name="password"
						render={({ field }) => (
							<FormItem>
								<FormLabel>Password</FormLabel>
								<FormControl>
									<Input placeholder="********" type="password" {...field} />
								</FormControl>
								<FormMessage />
							</FormItem>
						)}
					/>
					<Button className="w-full">SIGNUP</Button>
				</form>
			</Form>
		</div>
	);
}

export default SignUp;
