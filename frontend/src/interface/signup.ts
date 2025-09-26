import { createUserWithEmailAndPassword } from "firebase/auth";
import { auth } from "@/lib/firebase"
import { signupAPI } from "@/api/signup";

type Props = {
    email: string,
    password: string
}

export const signUp = async ({email, password}: Props) => {
    try {
        const result = await createUserWithEmailAndPassword(auth, email, password)
        const idToken = await result.user.auth.currentUser.getIdToken()
        const signUpResult = await signupAPI(idToken)
        if(!signUpResult.ok) {
            return {status: false}
        }
        return {status: true}

    } catch {
        return {status: false}
    }
}