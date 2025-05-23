import { render, screen } from '@testing-library/react';
import ResultsPanel from '../components/ResultsPanel';
import { AnalyzeProvider, AnalyzeContext } from '../context/AnalyzeContext';
import React from 'react';

test('shows results', () => {
  const mockContext = { result: { accent: 'British', confidence: 90, summary: 'Hello' }, loading: false, error: null, analyze: jest.fn() };
  render(
    <AnalyzeContext.Provider value={mockContext}>
      <ResultsPanel />
    </AnalyzeContext.Provider>
  );
  expect(screen.getByText(/British/)).toBeInTheDocument();
  expect(screen.getByText(/90%/)).toBeInTheDocument();
  expect(screen.getByText(/Hello/)).toBeInTheDocument();
});