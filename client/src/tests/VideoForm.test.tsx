import { render, fireEvent, screen } from '@testing-library/react';
import VideoForm from '../components/VideoForm';
import { AnalyzeProvider } from '../context/AnalyzeContext';

test('submits URL', () => {
  render(
    <AnalyzeProvider><VideoForm /></AnalyzeProvider>
  );
  const input = screen.getByPlaceholderText(/Enter video URL/i);
  fireEvent.change(input, { target: { value: 'http://test.mp4' } });
  fireEvent.click(screen.getByRole('button'));
  expect(screen.getByRole('button')).toBeDisabled();
});