import React from 'react';
import VideoForm from './components/VideoForm';
import ResultsPanel from './components/ResultsPanel';

const App: React.FC = () => (
  <div className="min-h-screen flex flex-col items-center p-6">
    <h1 className="text-3xl font-extrabold mb-6">Video Accent Analyzer</h1>
    <VideoForm />
    <ResultsPanel />
  </div>
);

export default App;