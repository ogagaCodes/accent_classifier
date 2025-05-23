import React, { useState } from 'react';
import { useAnalyze } from '../hooks/useAnalyze';

const VideoForm: React.FC = () => {
  const [url, setUrl] = useState('');
  const { analyze, loading, error } = useAnalyze();

  return (
    <form
      onSubmit={e => { e.preventDefault(); analyze(url); }}
      className="w-full max-w-md bg-white p-6 rounded-lg shadow">
      <input
        type="url"
        placeholder="Enter video URL"
        value={url}
        onChange={e => setUrl(e.target.value)}
        className="w-full p-3 border border-gray-300 rounded mb-4"
        required
      />
      <button
        type="submit"
        disabled={loading}
        className="w-full p-3 bg-blue-600 text-white rounded hover:bg-blue-700">
        {loading ? 'Analyzing...' : 'Analyze'}
      </button>
      {error && <p className="mt-2 text-red-500">{error}</p>}
    </form>
  );
};

export default VideoForm;