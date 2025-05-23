import { render, screen } from '@testing-library/react';
import App from '../App';
import { AnalyzeProvider } from '../context/AnalyzeContext';

test('renders title', () => {
  render(
    <AnalyzeProvider><App /></AnalyzeProvider>
  );
  expect(screen.getByText(/Video Accent Analyzer/i)).toBeInTheDocument();
});