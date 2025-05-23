import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';
import { AnalyzeProvider } from './context/AnalyzeContext';
import './index.css';

const container = document.getElementById('root');
if (!container) {
  throw new Error('Root container missing in index.html – make sure you have <div id="root"></div>');
}

const root = createRoot(container);
root.render(
  <AnalyzeProvider>
    <App />
  </AnalyzeProvider>
);
