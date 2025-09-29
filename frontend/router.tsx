import { createBrowserRouter } from 'react-router';
import Login from './src/screens/Login';
import SignUpScreen from './src/screens/SignUpScreen';

export const router = createBrowserRouter([
	{
		path: '/signup',
		element: <SignUpScreen />,
	},
	{
		path: '/login',
		element: <Login />,
	},
]);
