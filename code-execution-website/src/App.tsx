import React, { useState } from "react";
import axios from "axios";
import CodeEditor from "./components/CodeEditor";

const App: React.FC = () => {
  const [code, setCode] = useState<string>("");
  const [output, setOutput] = useState<string>("");

  // handles submit function, sends post request to backend FastAPI
  const handleSubmit = async () => {
    try {
      const response = await axios.post("http://localhost:8000/submit/", {
        code,
        output: "",
      });
      setOutput("code submitted successfully");
    } catch (error) {
      console.error("Failed to submit code:", error);
      setOutput("Error executing code.");
    }
  };

  // handles test function, sends post request to backend FastAPI
  const handleTest = async () => {
    try {
      const response = await axios.post("http://localhost:8000/test/", {
        code,
        output: "",
      });
      setOutput(response.data.output);
    } catch (error) {
      console.error("Failed to test code:", error);
      setOutput("Error executing code.");
    }
  };

  // HTML for React webpage
  return (
    <div className="container mx-auto p-4 flex flex-col md:flex-row items-start gap-4">
      <div className="w-full md:w-3/3">
        <div className="bg-white rounded-lg shadow-md p-6">
          <h1 className="text-xl font-bold mb-4">Python Code Executor</h1>
          <CodeEditor code={code} setCode={setCode} />
          <div className="my-4 space-x-4">
            <button
              onClick={handleTest}
              className="bg-green-500 text-white px-4 py-2 mt-4 rounded hover:bg-green-600 transition-colors duration-300"
            >
              Test
            </button>
            <button
              onClick={handleSubmit}
              className="bg-green-500 text-white px-4 py-2 mt-4 rounded hover:bg-green-600 transition-colors duration-300"
            >
              Submit
            </button>
          </div>
        </div>
      </div>
      <div className="w-full md:w-1/3">
        <div className="bg-gray-200 rounded-lg shadow-md p-6">
          <h1 className="text-xl font-bold mb-4">Output</h1>
          <pre className="text-gray-800 whitespace-pre-wrap">{output}</pre>
        </div>
      </div>
    </div>
  );
};

export default App;
