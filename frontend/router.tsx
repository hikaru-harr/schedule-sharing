import { createBrowserRouter } from "react-router"
import SignUpScreen from "./src/screens/SignUpScreen"
import Login from "./src/screens/Login"

export const router = createBrowserRouter([
    {
        path: "/signup",
        element: <SignUpScreen />
    },
    {
        path: "/login",
        element: <Login />
    },
])