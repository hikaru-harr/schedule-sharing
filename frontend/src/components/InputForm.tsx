import type { Control, FieldPath, FieldValues } from 'react-hook-form';
import {
	FormControl,
	FormDescription,
	FormField,
	FormItem,
	FormLabel,
	FormMessage,
} from '@/components/ui/form';
import { Input } from './ui/input';

type Props<TFieldValues extends FieldValues, TName extends FieldPath<TFieldValues>> = {
	control: Control<TFieldValues>;
	name: TName;
	type?: 'text' | 'email' | 'password';
	placeholder?: string;
	label?: string;
	description?: string;
	disabled?: boolean;
};

function InputForm<TFieldValues extends FieldValues, TName extends FieldPath<TFieldValues>>({
	control,
	name,
	label,
	type = 'text',
	placeholder,
}: Props<TFieldValues, TName>) {
	return (
		<FormField
			control={control}
			name={name}
			render={({ field }) => (
				<FormItem>
					<FormLabel>{label}</FormLabel>
					<FormControl>
						<Input placeholder={placeholder} type={type} {...field} />
					</FormControl>
					<FormDescription />
					<FormMessage />
				</FormItem>
			)}
		/>
	);
}

export default InputForm;
