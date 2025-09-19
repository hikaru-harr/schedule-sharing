import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import { RouterProvider } from "react-router";
import { router } from "../router.tsx";

const dom = document.getElementById("root");

if (dom) {
	createRoot(dom).render(
		<StrictMode>
			<RouterProvider router={router} />
		</StrictMode>,
	);
}
