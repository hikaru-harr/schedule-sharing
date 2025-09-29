import { z } from 'zod';

export const signUpFormSchema = z.object({
	email: z.email(),
	password: z.string(),
});

export type SignUpFormType = z.infer<typeof signUpFormSchema>;
