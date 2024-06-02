// Creating monaco text editor component
import React from "react";
import Editor, { OnChange, OnMount } from "@monaco-editor/react";

interface CodeEditorProps {
  code: string;
  setCode: (code: string) => void;
}

const CodeEditor: React.FC<CodeEditorProps> = ({ code, setCode }) => {
  const handleEditorChange: OnChange = (value) => {
    setCode(value || "");
  };

  const handleEditorDidMount: OnMount = (editor) => {
    editor.getModel()?.updateOptions({ tabSize: 2 });
  };

  return (
    <Editor
      height="60vh"
      width="80vh"
      language="python"
      value={code}
      onChange={handleEditorChange}
      onMount={handleEditorDidMount}
      theme="vs-dark"
    />
  );
};

export default CodeEditor;
