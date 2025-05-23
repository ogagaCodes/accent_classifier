import React from 'react';
import { useAnalyze } from '../hooks/useAnalyze';

const ResultsPanel: React.FC = () => {
  const { result } = useAnalyze();
  if (!result) return null;

  return (
    <div className="w-full max-w-md bg-white p-6 rounded-lg shadow mt-6">
      <h2 className="text-xl font-bold mb-4">Analysis Results</h2>
      <p><strong>Accent:</strong> {result.accent}</p>
      <p><strong>Confidence:</strong> {result.confidence}%</p>
      <p className="mt-2"><strong>Summary:</strong> {result.summary}</p>
    </div>
  );
};

export default ResultsPanel;